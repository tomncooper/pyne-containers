# Python North East

<img src="http://pythonnortheast.co.uk/color_logo_cmp.png" width="200">

## 14th September 2016

<img src="https://linuxcontainers.org/static/img/containers.png" width="100"> + <img src="https://d3nmt5vlzunoa1.cloudfront.net/phpstorm/files/2015/10/large_v-trans.png" width="150"> +  <img src="https://www.python.org/static/opengraph-icon-200x200.png" width="100"> =  <img src="http://i2.kym-cdn.com/photos/images/original/000/869/487/ccf.png" width="75">

## Containers + Python = Awesome

This repository contains code and instructions for the [Python North East](http://pythonnortheast.co.uk/) talk on container scripting using python.

### Container engines

If you would like to follow along with the talk and try messing with containers, you can install the container engines yourself.

[Docker](https://www.docker.com/products/docker) has a platform installer for Linux, Mac and Windows.

However, [LXD](https://linuxcontainers.org/lxd/) is a Linux only system (provided your distro has the correct kernel modules). To use it you either need to run Ubuntu (natively or via a VM) or use a server in the cloud.

Alternatively, you can have a mess around in a sandbox container at the LXD [try it page](https://linuxcontainers.org/lxd/try-it). This provides a LXD container instance, running Ubuntu 16.04, that you can ssh into or access via the console on the website. You get it for 30 mins and can install any packages in the Ubuntu repositories.

Unfortunatly, the try-it containers cannot access any external sites so you cannot clone this repo onto the container. However, you can install python and the libraries listed below. You can then copy and paste commands from this repo into the python REPL.

### Required libraries

This talk uses the Python libraires for both [LXD](https://github.com/lxc/pylxd) and [Docker](https://github.com/docker/docker-py). On Ubuntu these can be installed via:

    sudo apt-get install python-docker python-pylxd

Packages are also available in the [AUR](https://www.archlinux.org/packages/community/any/python-docker-py/) and for [RPM](https://www.rpmfind.net/linux/rpm2html/search.php?query=python-docker-py) based distros.

If you are using one of the other, lesser, operating systems then the libraries can also be installed using pip:

    pip install docker-py pylxd

The pylxd library can be a bit funny about finding images sometimes. If you want to speed things up you can run the command below on your LXD box to copy the latest ubuntu image over to you local machine:

    lxc image copy ubuntu:16.04 local:

### Resources

LXD:

- [Linux Containers](https://linuxcontainers.org/) - Home page of LXC and LXD. Contains getting started guides and links to other resources.
- [LXD 2.0 Blog series](https://www.stgraber.org/2016/03/11/lxd-2-0-blog-post-series-012/) - A great series of blog posts about what LXD 2.0 can do and how to do it.
- [pyLXD Documentation](https://pylxd.readthedocs.io/en/latest/) - Read the docs site for pyLXD.

Docker:

- [docker-py Documentation](https://docker-py.readthedocs.io/en/latest/) - Read the docs site for docker-py.
