from pylxd import Client as LXDclient
from docker import Client as Dclient

#Some libraries for showing output from the containers
from pprint import pprint
import requests

######## Connect to the LXD container running docker ########

#Get the lxd container
lxd_client = LXDclient()
docker = lxd_client.containers.get("Docker1")

#Get the ip address for the LXD container running docker
def get_lxd_container_ip(container):
    #Get the ethernet address dictionary
    addresses = container.state().network["eth0"]["addresses"]

    #The ip4 address will be in the dictionary where the family key value is "inet"
    for address in addresses:
        if address["family"] == "inet":
            host = address["address"]

    return host

host = get_lxd_container_ip(docker)

#You could also get the host address by parsing the output of the ifconfig command
#run on the the lxd container.
#host = docker.execute(["ifconfig", "eth0"])[0].split("inet addr:")[1].split()[0]

print "Connected to LXD container {} at {}".format(docker.name, host)

def get_docker_port(container):
    ports = docker.execute(["netstat", "-tulpn"])[0].split("\n")

    for line in ports:
        if "docker" in line:
            port = line.split()[3].split(":::")[1]

    return port

#Get the port the docker host is listening on
port = get_docker_port(docker)

######## Connect to the docker host ########

#Connect to the remote docker host in the LXC container
dockerclient = Dclient(base_url="tcp://{}:{}".format(host,port), version="auto")

print "Connected to Docker host on {}:{}".format(host,port)

######## Create an docker image ########

print "\nCreating image from Dockerfile\n"

#Create a docker container image from the Dockerfile in this directory
response = dockerclient.build(path=".", dockerfile="Dockerfile", tag="pyne/helloworld")

#Show the output from the build process
for line in response:
    print line

#Show the images now avalible on the docker host
print "Images on docker host:"
pprint(dockerclient.images())

print "\nCreating container from hello world image:\n"

#Create a config object containing the port mappings from the containers port to the host port
#The container port should match the one that is exposed in the Dockerfile
container_port = 5000
host_port = 4000
host_config=dockerclient.create_host_config(port_bindings={container_port : host_port})

#Create a container from the newly created image, expose the correct ports
#and add the config that maps these ports to the host
hw_container = dockerclient.create_container(name = "hello", image="pyne/helloworld:latest", ports = [container_port], host_config = host_config)

#Start the container
response = dockerclient.start(container=hw_container["Id"])

#Check that the container is serving correctlty
r = requests.get("http://{}:{}".format(host,host_port))
print "The container said: {}".format(r.text)
