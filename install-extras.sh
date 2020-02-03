#!/bin/bash
# you will have to execute this script as sudo
echo "installing ffmpeg"
apt install ffmpeg
echo "Installing python3-dev"
apt install python3-dev -y
echo "Installing virtualenv"
apt-get install virtualenv