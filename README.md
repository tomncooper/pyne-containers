# Python North East

<img src="http://pythonnortheast.co.uk/color_logo_cmp.png" width="200">

## 14th September 2016

<img src="https://linuxcontainers.org/static/img/containers.png" width="100"> + <img src="https://d3nmt5vlzunoa1.cloudfront.net/phpstorm/files/2015/10/large_v-trans.png" width="150"> +  <img src="https://www.python.org/static/opengraph-icon-200x200.png" width="100"> =  <img src="http://i2.kym-cdn.com/photos/images/original/000/869/487/ccf.png" width="75">

## Containers + Pyton = Awesome

This repository contains code and instructions for the [Python North East](http://pythonnortheast.co.uk/) talk on container scripting using python.

### Container engines

If you would like to follow along with the talk and try messing with containers you can install the container engines yourself.

[Docker](https://www.docker.com/products/docker) has a platform installer for Linux, Mac and Windows.

However, [LXD](https://linuxcontainers.org/lxd/) is a Linux only system. To use it you either need to run Ubuntu (natively or via a VM) or use a server in the cloud.

Alternatively, you can have a mess around in a sandbox container at the LXD [try it page](https://linuxcontainers.org/lxd/try-it).

### Required libraires

This talk uses the Python libraires for both [LXD](https://linuxcontainers.org/lxd/) and [Docker](https://www.docker.com/). On Ubuntu these can be installed via:

    sudo apt-get install python-docker python-pylxd

Packages are also available in the [AUR](https://www.archlinux.org/packages/community/any/python-docker-py/) and for [RPM](https://www.rpmfind.net/linux/rpm2html/search.php?query=python-docker-py) based distros.

If you are using one of the other, lesser, operating systems then the libraries can also be installed using pip:

    pip install docker-py pylxd
