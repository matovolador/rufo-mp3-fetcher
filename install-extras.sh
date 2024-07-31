#!/bin/bash
# you will have to execute this script as sudo
echo "installing ffmpeg"
apt install ffmpeg -y
echo "installing tkinter"
apt install python3-tk -y
echo "Installing python3-dev"
apt install python3-dev -y
echo "Installing virtualenv"
apt-get install virtualenv -y