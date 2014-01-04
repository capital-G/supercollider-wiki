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

When you are presented with a screen asking you if you would like to enable realtime access priority, choose 'Yes'.

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
Start the SuperCollider IDE, and look at the post window. The following is part of the post window output on my machine: 

    NumPrimitives = 679
    compiling dir: '/usr/share/SuperCollider/SCClassLibrary'
    compiling dir: '/usr/share/SuperCollider/Extensions'
    pass 1 done

Look for the two lines starting 'compiling dir:'. The second quotes the location we want. Remove the trailing '/share/SuperCollider/Extensions' bit and make a note of it. So in my case, the location is '/usr'.

This location will be referred to as **PluginLocation** for the remainder of this article.
#### Where the header include files are
The header include files are added when you install the supercollider-dev package. You need to know where these files are when you install the plugins.
To locate the directory containing the header include files, search your file system (not just your home folder) for a file called 'SCVersion.txt'. The directory containing this file, usually '/usr/include/SuperCollider', is the one you want.

This location will be referred to as **HeaderIncludeFileLocation** for the remainder of this article.
### Getting the source code for the plugins
Simply clone the git repository:

    git clone https://github.com/supercollider/sc3-plugins.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

This will create a folder called **sc3-plugins**.
### Getting the submodules
From within **sc3-plugins**, run the following:

    git submodule init && git submodule update

### Running cmake
Create a directory inside **sc3-plugins** called **build** and move to it in the terminal. Run the following:

    cmake -DSC_PATH=**HeaderIncludeFileLocation** -DCMAKE_INSTALL_PREFIX=**PluginLocation** ..

So in my case, I would run:

    cmake -DSC_PATH=/usr/include/SuperCollider -DCMAKE_INSTALL_PREFIX=/usr ..

Don't miss out those two dots on the end!
### Finally, building the plugins
From within **sc3-plugins/build**, run the following:

    make
    sudo make install

### Checking the installation worked
If you have the IDE open, close it. Now open it again and boot the server.

Enter the following into the blank text window and run it:

    {VOSIM.ar(Impulse.ar(100), 500, 3, 0.99)}.play

You should hear a buzzing sound. If you don't, double check and attempt the instructions again. To undo the build you just did, from within **sc3-plugins**, run the following:

    make uninstall
    rm -r *

If you still don't have any luck, ask a question [here](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/SuperCollider-Users-New-Use-this-f2676391.html), providing as much information as you can.