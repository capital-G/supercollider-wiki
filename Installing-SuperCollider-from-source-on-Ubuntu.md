This page gives instructions for installing SuperCollider on Ubuntu and its derived OSes (e.g. Mint / Elementary OS). It covers installing SuperCollider and the plugins from source.

## Installing SuperCollider
### Packages you need
You will need to install quite a few packages to build the SuperCollider and its plugins. Below is a list of this software, along with the terminal commands to get it.

    sudo apt-get install build-essential libjack-dev or libjack-jackd2-dev libsndfile1-dev libasound2-dev libavahi-client-dev libicu-dev libreadline6-dev libfftw3-dev libxt-dev libudev-dev pkg-config git cmake qt5-default qt5-qmake qttools5-dev qttools5-dev-tools qtdeclarative5-dev libqt5webkit5-dev qtpositioning5-dev libqt5sensors5-dev libqt5opengl5-dev

*Note*: You need at least gcc version 4.7. The sc3-plugins contains c++11 code that does not build with v4.6. Check with `gcc -v` if you run into c++11 related errors.

### Getting the source code for SuperCollider
Clone the git repository:

    git clone https://github.com/supercollider/supercollider.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'supercollider'.: Permission denied

Cloning the repository will create a folder called **supercollider** containing the source code.
### Getting the submodules
From within **sc3-plugins**, run the following:

    git submodule init && git submodule update

### Checking the installation worked
First, open the SuperCollider IDE by searching for and running 'SuperCollider IDE'. The IDE should open and give you three main panes:
* a large blank text window
* a help window
* a post window containing text about how the startup process went.

Secondly, boot the server using the command in the Language menu, or <kbd>Ctrl</kbd>+<kbd>B</kbd>.

Thirdly, enter the following into the blank text window:

    {SinOsc.ar}.play

Ensure the cursor is on this line and hit <kbd>Ctrl</kbd>+<kbd>Enter</kbd>. You should now hear a sine tone. Kill the sine tone by hitting <kbd>Ctrl</kbd>+<kbd>.</kbd>.
If you don't hear the tone, remember to check your speakers, volume control – all the regular suspects!

## Installing the plugins
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

#### If SCVersion.txt is not present
If you find that SCVersion.txt is not on your file system, you will need to create it. Create a file of that name in '/usr/include/SuperCollider'.

Now fire up the IDE and read the introductory text that appears in the post window. You will see a line like this:

    Welcome to SuperCollider 3.6.6. For help press Ctrl-D.

Make a note of the three numbers in the SuperCollider version. Now give SCVersion.txt the following contents:

    set(PROJECT_VERSION_MAJOR {major version})
    set(PROJECT_VERSION_MINOR {minor version})
    set(PROJECT_VERSION_PATCH {build number})

So in my case, I would give SCVersion.txt the contents:

    set(PROJECT_VERSION_MAJOR 3)
    set(PROJECT_VERSION_MINOR 6)
    set(PROJECT_VERSION_PATCH 6)

### Getting the source code for the plugins
Simply clone the git repository:

    git clone https://github.com/supercollider/sc3-plugins.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

Cloning the repository will create a folder called **sc3-plugins** containing the source code.
### Getting the submodules
From within **sc3-plugins**, run the following:

    git submodule init && git submodule update

### Running cmake
Create a directory inside **sc3-plugins** called **build**. From within **sc3-plugins/build**, run the following:

    cmake -DSC_PATH=**HeaderIncludeFileLocation** -DCMAKE_INSTALL_PREFIX=**PluginLocation** -DCMAKE_BUILD_TYPE=Release ..

So in my case, I would run:

    cmake -DSC_PATH=/usr/include/SuperCollider -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..

Don't miss out those two dots on the end!
### Finally, building the plugins
From within **sc3-plugins/build**, run the following:

    make
    sudo make install
    sudo ldconfig

### Checking the installation worked
If you have the IDE open, close it. Now open it again and boot the server.

Enter the following into the blank text window and run it:

    {VOSIM.ar(Impulse.ar(100), 500, 3, 0.99)}.play

You should hear a buzzing sound. If you don't, double check and attempt the instructions again. To undo the build you just did, from within **sc3-plugins**, run the following:

    make uninstall
    rm -r *

If you still don't have any luck, ask a question [here](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/SuperCollider-Users-New-Use-this-f2676391.html), providing as much information as you can.