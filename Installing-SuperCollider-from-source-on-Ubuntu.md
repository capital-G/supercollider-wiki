This page gives instructions for installing SuperCollider on Ubuntu and its derived distributions (e.g. Linux Mint, Elementary OS). It covers building and installing SuperCollider and the sc3-plugins from the source code.

## Building SuperCollider
### Packages you need
You will need to install quite a few packages to build SuperCollider and the sc3-plugins. Below is a list of this software, along with the terminal commands to get it.
```
sudo apt-get install build-essential libsndfile1-dev libasound2-dev libavahi-client-dev libicu-dev libreadline6-dev libfftw3-dev libxt-dev libudev-dev pkg-config git cmake qt5-default qt5-qmake qttools5-dev qttools5-dev-tools qtdeclarative5-dev libqt5webkit5-dev qtpositioning5-dev libqt5sensors5-dev libqt5opengl5-dev
```

**Note**: The recommended version of gcc is `4.8`. Most Linux systems meet this requirement. You can check your gcc version in a terminal with the command `gcc --version`.

#### JACK dependency
You will also need JACK installed on your system. There are two version of JACK available: JACK1 and JACK2. If you are unsure of which version of JACK to install, we recommend choosing JACK2. It can be installed using the following command: 
```
sudo apt-get install libjack-jackd2-dev
```

SuperCollider requires JACK for sound on Linux. The package `qjackctl` provides a convenient graphical user interface for JACK, which facilitates JACK configuration, as well as making inter-application audio and MIDI connections.

You can run the following terminal command to find out which JACK version you have installed. The command simulates an actual installation:
```
apt-get -s install jackd1 jackd2
```

### Getting the SuperCollider source code
Clone the git repository:
```
git clone --recursive https://github.com/supercollider/supercollider.git
```

With the `--recursive` flag, the repository's submodules are also cloned. 

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:
```
fatal: could not create work tree dir 'supercollider'.: Permission denied
```

Cloning the repository will create a folder called **supercollider** containing the source code. 

### Getting the submodules
If you cloned the SuperCollider repository without the `--recursive` flag, you will need to manually initialise and update the submodules. From within the **supercollider** directory, run the following:
```
git submodule update --init
```

### Running cmake
Create a directory inside **supercollider** called **build**. 
```
mkdir build && cd build
```

From within **supercollider/build**, run the following:

    cmake ..

(Notice the space before the two dots)

Running the following will post a list of all available flags that can be set in order to configure your build.
```
cmake -L ..
```

For example, if you wish to build SuperCollider without emacs support, run:
```
cmake -DSC_EL=OFF ..
```

For a release type build, run:
```
cmake -DCMAKE_BUILD_TYPE=Release ..
```

For a native build, run:
```
cmake -DNATIVE=ON ..
```

It's possible to set multiple flags at once like so:
```
cmake -DCMAKE_BUILD_TYPE=Release -DNATIVE=ON -DSC_EL=OFF ..
```

## Building and installing
Use the following commands to build and install Supercollider;

    make
    sudo make install

If your system has multiple cores, you can take advantage of make's `-j` option. For example, a system containing 4 cores can run:
```
make -j4
sudo make install
```

### Checking the installation worked
First, fire up JACK, using qjackctl or your choice of tool.

Secondly, open the SuperCollider IDE by searching for and running 'SuperCollider IDE'. Occasionally I find that, immediately after installation, SuperCollider does not show up in the menu. This can be fixed by a restart. If you don't want to restart now, you can run SuperCollider by opening a terminal and entering 'scide'.

When the IDE opens, it should give you three main panes:
* a large blank text window
* a help window
* a post window containing text about how the startup process went.

Thirdly, boot the server using the command in the Language menu, or <kbd>Ctrl</kbd>+<kbd>B</kbd>.

And finally, enter the following into the blank text window:

    {SinOsc.ar}.play

Ensure the cursor is on this line and hit <kbd>Ctrl</kbd>+<kbd>Enter</kbd>. You should now hear a sine tone. Kill the sine tone by hitting <kbd>Ctrl</kbd>+<kbd>.</kbd>.
If you don't hear the tone, remember to check your speakers, volume control – all the regular suspects!

## Installing the plugins
### Information you need
#### Where to install the plugins
When SuperCollider starts up, it looks for the plugins in a particular location. You need to know this location in order to control where the plugins get installed.
Start the SuperCollider IDE, and look at the post window. The following is part of the post window output on my machine: 

    NumPrimitives = 679
    compiling dir: '/usr/local/share/SuperCollider/SCClassLibrary'
    compiling dir: '/usr/local/share/SuperCollider/Extensions'
    pass 1 done

Look for the two lines starting 'compiling dir:'. The second quotes the location we want. Remove the trailing '/share/SuperCollider/Extensions' bit and make a note of it. So in my case, the location is '/usr/local'.

This location will be referred to as **PluginLocation** for the remainder of this article.
#### Where the header include files are
You need to know where header include files are when you install the plugins.
To locate the directory containing the header include files, search your file system (not just your home folder) for a file called 'SC_BoundsMacros.h'. The directory containing this file, usually '/usr/local/include/SuperCollider/common', is a child of the headers directory. So if you find 'SC_BoundsMacros.h' in '/usr/local/include/SuperCollider/common', then the headers directory is '/usr/local/include/SuperCollider'.

This location will be referred to as **HeaderIncludeFileLocation** for the remainder of this article.

#### If SCVersion.txt is not present
You will also need a file called SCVersion.txt to be in the header directory. This is usually placed there during the installation of SuperCollider, but if you find it's not there, you will need to create it. Create a file of that name in **HeaderIncludeFileLocation**.

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

If the version you see in the welcome message is something like '3.6dev', then create a file like this:

    set(PROJECT_VERSION_MAJOR 3)
    set(PROJECT_VERSION_MINOR 6)
    set(PROJECT_VERSION_PATCH dev)

### Getting the source code for the plugins
Simply clone the git repository:

    git clone --recursive https://github.com/supercollider/sc3-plugins.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

Cloning the repository will create a folder called **sc3-plugins** containing the source code.

### Running cmake
Create a directory inside **sc3-plugins** called **build**. From within **sc3-plugins/build**, run the following:

    cmake -DSC_PATH=**HeaderIncludeFileLocation** -DCMAKE_INSTALL_PREFIX=**PluginLocation** -DCMAKE_BUILD_TYPE=Release ..

So in my case, I would run:

    cmake -DSC_PATH=/usr/local/include/SuperCollider -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release ..

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