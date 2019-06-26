# RUFO MP3 FETCHER

## Requirements

[Git](https://git-scm.com/downloads)

For DEB people:
***sudo apt install git -y***

## Installation

The installation starts by fetching the repo with git.

So the command would be:

```bash
git clone https://github.com/bossnode/rufo-mp3-fetcher.git && cd rufo-mp3-fetcher && git fetch && git checkout dev && chmod +x ./install.sh && chmod +x ./run.sh && chmod +x ./install-extras.sh && chmod +x ./update.sh
```

### What it does

The install script is `install.sh`.

The script does an insane amount of stuff. Currently under testing. Will try to nuke down the overload, and then add a proper description of what it does here. Mainly, it gets the required python if you do not have it, and installs/creates the virtual environment + installs python dependencies there.

You will probably need to install extra stuff that requires sudo priviledges. I stored those commands on a separate file so you dont need to worry about reading that much. The file is `install-extras.sh`.

So in the scenario where you would need to install all of the dependencies, or are unsure what you need, and you trust a random guy on the internet enough to run .sh scripts as sudo, you would do:

```bash
sudo ./install-extras.sh
./install.sh
```

### Updating

If you wish you update, you can run the `update.sh` script.

You might need to update more dependencies, in which case you might need to run the `install-extras.sh` script (as sudo, read the contents first).

After updating, your .sh scripts might need to have their "execution" permission updated again. So you can run

```bash
chmod +x ./install.sh && chmod +x ./run.sh && chmod +x ./install-extras.sh && chmod +x ./update.sh
```

## EXCECUTION

The run entry is `run.sh` . The command from the "Get the files" will activate "execute" mode on it. so just navigate to the folder and double click it.

ENJOY!

## LICENCE

MIT

## If you want to donate

4ArHfJ6tMwf7fGupuYsZZ9XFwgVAQPCdsXqtq9Kc1gwCSQfwLBwFCFwL5aav9KqCz6RMH4rYtaETaQuP81YcwYdUGrJCrPm

