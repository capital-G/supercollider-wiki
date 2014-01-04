This page represents a somewhat ambitious attempt to describe how to install SuperCollider onto a computer running Ubuntu or a similar system (e.g. Mint). It covers installing SuperCollider from a package and installing the plugins from source. It does not cover installing SuperCollider from source.
## Adding the PPA
The PPA contains a more up-to-date version of SuperCollider than the default package source. Install the PPA by entering these lines into a terminal:

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FABAEF95
    sudo add-apt-repository ppa:supercollider/ppa

Further information about the PPA can be found [here](https://launchpad.net/~supercollider/+archive/ppa).

## Installing SuperCollider
Enter these lines into a terminal:

    sudo apt-get update
    sudo apt-get install supercollider

## Checking the installation worked
First, open the SuperCollider IDE by searching for and running 'SuperCollider IDE'. The IDE should open and give you three main panes: a large blank text window, a help window and a post window containing text about how the startup process went.
Secondly, boot the server using the command in the Language menu, or Ctrl+B.
Thirdly, enter the following into the blank text window:

    {SinOsc.ar}.play

Ensure the cursor is on this line and hit <kbd>Ctrl</kbd>+<kbd>Enter</kbd>. You should now hear a sine tone. Kill the sine tone by hitting <kbd>Ctrl</kbd>+<kbd>.</kbd>.