#!/bin/bash
echo "This project requires python3.5.+ or python3.6.+. The script will find your python3 versions now..."
find / -type f -executable -iname 'python3*' -exec file -i '{}' \; | awk -F: '/x-executable; charset=binary/ {print $1}' | xargs readlink -f | sort -u | xargs -I % sh -c 'echo -n "%: "; % -V'
read -p "Do you wish to install python3.6.8? Enter y|Y if so, or n|N if you already have it instaled:" install_python
if [[ $install_python = "y" ||  $install_python = "Y" ]]
then
    #install python
    wget https://www.python.org/ftp/python/3.6.8/Python-3.6.8.tgz && gunzip < Python-3.6.8.tgz | tar xvf - && rm -r Python-3.6.8.tgz
    cd Python-3.6.8
    ./configure && make && make altinstall && echo "Looking for python3 locations again..." && find / -type f -executable -iname 'python3*' -exec file -i '{}' \; | awk -F: '/x-executable; charset=binary/ {print $1}' | xargs readlink -f | sort -u | xargs -I % sh -c 'echo -n "%: "; % -V'
else
    echo "Skipping python installation."
fi


python_path_default="/usr/bin/python3.6"
read -p "Enter python3.6.*path (defaults to $python_path_default ) Leave blank to use default:" python_path
if [[ $python_path = "" ]]
then
    $python_path="$python_path_default"
else
    $python_path="/usr/bin/python3.6"
fi
echo "Using path: $python_path"
echo "Setting up the virtual environment..."
virtualenv venv --python=$python_path
source venv/bin/activate
pip install -r requirements.txt
deactivate
echo "End of script."
exit $?