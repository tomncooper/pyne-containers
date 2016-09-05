from pylxd.client import Client

#Create a connection to the local LXD deamon
c = Client()

#Create the config for an Ubuntu container
#Set the source for the container - this allows you to specify the base operating system image
source = {'type': 'image', "alias" : "xenial"}
#Specify the profiles to be applied to the base image. The default profile contains the basic network configuration while the docker profile tells LXD to load a few required kernel modules and set up some mounts for the container. The docker profile also enables container nesting.
profiles = ["default", "docker"]
#Create the container dict and give the container a name
config = {'name': 'Docker1', 'source': source, "profiles": profiles}

#Issue the create command, this can bd done asynchronsly if wait is set to False
c.containers.create(config, wait=True)

#Get the instance for the new container
docker = c.containers.get("Docker1")

print "Container {} is currently {}".format(docker.name, docker.status)

#Start the container
docker.start(wait=True)
#Update the container instance
docker.update()

print "Container {} is currently {}".format(docker.name, docker.status)