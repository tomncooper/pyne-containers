#!/bin/bash

sudo apt-get install -y python-pylxd python-docker

lxc image copy ubuntu:16.04 local:

lxc launch local:16.04 Docker1 -p default -p docker
