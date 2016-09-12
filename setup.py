from pylxd import Client

#Create a connection to the local LXD deamon
c = Client()

#Get the container instance for the newly created container
container = c.containers.get("Docker1")

#The status command lets you know the current state of the container on the server
if container.status != "Running":
    container.start()

#Install Docker in the new container

#First update the repository database inside the container
#This command will block until the supplied command returns
#This is like a remote call to subprocess.Popen, the output is a tuple containing (stdout, stderr)
output = container.execute(["apt-get", "update"])
#You can parse the error messages and stdout for more complex automation
if output[1]:
    print "Errors returned:"
    print output[1]

#Upgrade any packages
output = container.execute(["apt-get", "dist-upgrade", "-y"])

#Install Docker
output = container.execute(["apt-get", "install", "docker.io", "-y"])
