from pylxd import Client as LXDclient
from docker import Client as Dclient

from pprint import pprint

#Get the LXD container running docker
lxd_client = LXDclient()
docker = lxd_client.containers.get("Docker1")

#Get the ip address for the LXD container running docker
#You could get this through a REST API call, but who has the time!
host = docker.execute(["ifconfig", "eth0"])[0].split("inet addr:")[1].split()[0]

print "Connected to LXD container {} at {}".format(docker.name, host)

#Connect to the remote docker host in the LXC container
dockerclient = Dclient(base_url="tcp://{}:2345".format(host), version="auto")

print "Connected to Docker host"

#Create a docker container image from the Dockerfile in this directory
response = dockerclient.build(path=".", dockerfile="Dockerfile", tag="pyne/helloworld")

for line in response:
    print line

pprint(dockerclient.images())
