This page represents a somewhat ambitious attempt to describe how to install SuperCollider onto a computer running Ubuntu or a similar system (e.g. Mint). It covers installing SuperCollider from a package and installing the plugins from source. It does not cover installing SuperCollider from source.
### Adding the PPA
The PPA contains a more up-to-date version of SuperCollider than the default package source. Add the PPA by entering these lines into a terminal:

    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys FABAEF95
    sudo add-apt-repository ppa:supercollider/ppa

Further information about the PPA can be found [here](https://launchpad.net/~supercollider/+archive/ppa).

### Installing SuperCollider
Enter these lines into a terminal:

    sudo apt-get update
    sudo apt-get install supercollider

### Checking the installation worked
First, open the SuperCollider IDE by searching for and running 'SuperCollider IDE'. The IDE should open and give you three main panes:
* a large blank text window
* a help window
* a post window containing text about how the startup process went.

Secondly, boot the server using the command in the Language menu, or <kbd>Ctrl</kbd>+<kbd>B</kbd>.

Thirdly, enter the following into the blank text window:

    {SinOsc.ar}.play

Ensure the cursor is on this line and hit <kbd>Ctrl</kbd>+<kbd>Enter</kbd>. You should now hear a sine tone. Kill the sine tone by hitting <kbd>Ctrl</kbd>+<kbd>.</kbd>.
If you don't hear the tone, remember to check your speakers, volume control etc!

## Installing the plugins
The plugins are not required, but they're a whole bunch of free stuff, so why wouldn't you get them? Unfortunately they're not available as a package so you need to build and install them for yourself. I have attempted to provide instructions for this which assume as little knowledge of Linux and building C++ code as possible.
### Packages you need
You will need to install quite a bit of software to get the plugins. Below is a list of this software, along with the terminal commands to get it.
#### C++ compiler

    sudo apt-get install build-essential

#### cmake

    sudo apt-get install cmake

#### FFTW

    sudo apt-get install libfftw3-dev

#### git

    sudo apt-get install git

#### supercollider-dev

    sudo apt-get install supercollider-dev
### Information you need
#### Where to install the plugins
When SuperCollider starts up, it looks for the plugins in a particular location. You need to know this location in order to control where the plugins get installed.
Start SuperCollider, and look at the post window. The following is part of the post window output on my machine: 

    NumPrimitives = 679
    compiling dir: '/usr/share/SuperCollider/SCClassLibrary'
    compiling dir: '/usr/share/SuperCollider/Extensions'
    pass 1 done

Look for the two lines starting 'compiling dir:'. The second quotes the location we want. Remove the trailing '/share/SuperCollider/Extensions' bit and make a note of it. So in my case, the location is '/usr'.

This location will be referred to as **PluginLocation** for the remainder of this article.
#### Where the header include files are
The header include files are added when you install the supercollider-dev package. You need to know where these files are when you install the plugins.
To locate the directory containing the header include files, search your file system for a file called 'SCVersion.txt'. The directory containing this file, usually '/usr/include/SuperCollider' is the one you want.

This location will be referred to as **HeaderIncludeFileLocation** for the remainder of this article.
### Getting the source code for the plugins
Simply clone the git repository. It doesn't matter in the file system you do this:

    git clone https://github.com/supercollider/sc3-plugins.git

This will create a folder called **sc3-plugins**.
### Getting the submodules