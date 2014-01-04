This page represents a somewhat ambitious attempt to describe how to install SuperCollider onto a computer running Ubuntu or a similar system (e.g. Mint). It covers installing SuperCollider from a package and installing the plugins from source. It does not cover installing SuperCollider from source.
## Adding the PPA
The PPA contains a more up-to-date version of SuperCollider than the default package source. Install the PPA by opening a terminal and entering these lines:
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FABAEF95
    sudo add-apt-repository ppa:supercollider/ppa
    sudo apt-get update
    sudo apt-get install supercollider supercollider-gedit supercollider-plugins