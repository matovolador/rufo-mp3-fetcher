#!/bin/bash
# Pull the repo and hard merge
git fetch --all
git reset --hard origin/master

# Update python dependencies
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
# Intentionally upgrade youtube-dl module as its the 'hottest one in town'
pip install -U youtube-dl
# If you get newer version...
pip freeze > requirements.txt
deactivate
# reset the damn flags back to +x on these (retrieving the repo seems to clean them out)
chmod +x ./update.sh && chmod +x ./run.sh && chmod +x ./install.sh && chmod +x ./install-extrash.sh