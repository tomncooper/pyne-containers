#!/bin/bash

sudo apt-get install -y python-pylxd python-docker

lxc launch ubuntu:16.04 Docker1 -p default -p docker
