#!/bin/bash
# you will have to execute this script as sudo
echo "installing ffmpeg"
apt install ffmpeg
echo "Installing python3-dev"
apt install python3-dev -y
echo "Installing libgirepository1.0-dev"
apt install libgirepository1.0-dev -y
echo "Installing libcairo2-dev libjpeg-dev libgif-dev"
apt-get install libcairo2-dev libjpeg-dev libgif-dev -y
echo "Installing virtualenv"
apt-get install virtualenv