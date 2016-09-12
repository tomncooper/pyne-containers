from pylxd import Client
c = Client()

#Create config values
source = {'type': 'image', "alias" : "xenial"}
profiles = ["default"]

###### Create zookeeper machine #####
zk = c.containers.create({'name': 'Zookeeper', 'source': source, "profiles": profiles})

#Install Java and supervisor
output = zk.execute(["apt-get", "update", "-y"])
output = zk.execute(["apt-get", "dist-upgrade", "-y"])
output = zk.execute(["apt-get", "install", "openjdk-8-jdk-headless", "supervisor", "-y"])

#Get the zookeeper binary
urllib.urlretrieve('http://mirrors.ukfast.co.uk/sites/ftp.apache.org/zookeeper/stable/zookeeper-3.4.9.tar.gz', 'zookeeper.tar.gz')

#Upload zookeeper binary
zk.files.put("/root/zookeeper.tar.gz", open("zookeeper.tar.gz","rb"))

#Unpack the tar and upload zookeeper config
output = zk.execute(["tar", "-xf", "zookeeper.tar.gz"])
zk.files.put("/root/zookeeper/conf/zoo.cfg", open("config/zk/zoo.cfg","r"))

#Setup supervisor to start zk automatically
zk.files.put("/etc/supervisor/conf.d/zk.conf", open("config/zk/zk.conf","r"))
#Update supervisor config
output = zk.execute(["supervisorctl", "reread"])
output = zk.execute(["supervisorctl", "update"])

###### Create Nimbus Server ######

#...

###### Create Storm Workers ######

###### Create Worker machine #####
worker = c.containers.create({'name': 'Worker1', 'source': source, "profiles": profiles})

#Install Java and supervisor
output = worker.execute(["apt-get", "update", "-y"])
output = worker.execute(["apt-get", "dist-upgrade", "-y"])
output = worker.execute(["apt-get", "install", "openjdk-8-jdk-headless", "supervisor", "-y"])

#Get and upload the storm binary and config
urllib.urlretrieve('http://mirrors.ukfast.co.uk/sites/ftp.apache.org/storm/apache-storm-1.0.2/apache-storm-1.0.2.tar.gz', 'storm.tar.gz')
worker.files.put("/root/storm.tar.gz", open("storm.tar.gz","rb"))
output = worker.execute(["tar", "-xf", "storm.tar.gz"])
worker.files.put("/root/storm/conf/storm.yaml", open("config/storm/storm.yaml","r"))

#Setup supervisor to start storm worker program automatically
worker.files.put("/etc/supervisor/conf.d/storm_supervisor.conf", open("config/storm/storm_supervisor.conf","r"))
#Update supervisor config
output = worker.execute(["supervisorctl", "reread"])
output = worker.execute(["supervisorctl", "update"])

#All workers will be the same base software so to save time adding more we can create an image of this worker.
#To create an image from a container it must be stopped
worker.stop()
wrk_image = worker.publish(wait=True)
wrk_image.add_alias(name="StormWorker", description="Pre-installed storm worker image")
worker.start()

#New workers can now be created from that image
workers = list()
workers.append(worker)
for i in range(2,10):
    w = c.containers.create({'name': 'Worker{}'.format(i), 'source': {'type': 'image', "alias" : "StormWorker"}, "profiles": profiles}, wait=True)
    w.start()
    workers.append(w)

#Could also snapshot servers at different stages and create images from those snapshots.
#pylxd also allows you to migrate workers between lxd servers
