# Installing SuperCollider on Fedora

SuperCollider is not available within the standard Fedora repos nor in a published Copr. There are two standard ways to install it: either using the Stanford [Planet CCRMA repo](http://ccrma.stanford.edu/planetccrma/software/) or installing from source.

## Planet CCRMA

Planet CCRMA documentation is not always up to date, here is an example installing SuperCollider on Fedora 25.

Install the repository package:

    # rpm -Uvh http://ccrma.stanford.edu/planetccrma/mirror/fedora/linux/planetccrma/24/i386/planetccrma-repo-1.1-3.fc24.ccrma.noarch.rpm

Install supercollider:

    # dnf search supercollider

    # dnf install -y supercollider supercollider-emacs supercollider-vim supercollider-sc3-plugins

## Install from source

I'm following the instructions [here](https://github.com/supercollider/supercollider/blob/master/README_LINUX.md), but clarifying them for the benefit of noobs.

Also, if you have difficulties, [this link](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/Installing-SuperCollider-on-Fedora-21-No-CMAKE-CXX-COMPILER-could-be-found-td7615864.html) might help.

The following [Sourceforge question](http://stackoverflow.com/questions/31381892/fedora-22-compile-atomic-is-lock-free) describes how to link to libatomic.

## Obtaining dependencies

The following packages are required and are available through yum / dnf.

* gcc
* jack-audio-connection-kit-devel
* libsndfile-devel
* cmake
* fftw-devel
* libXt-devel (note capital 'X')
* git
* gcc-c++
* libX11-devel
* qtwebkit-devel 
* qt5-qtlocation-devel
* qt5-qtsensors-devel
* systemd-devel (provides libudev.h)
* libatomic
* avahi-devel 
* qt5-qttools-devel 
* emacs 
* alsa-lib-devel 


The required packages may be installed with the following command;

    sudo dnf install gcc jack-audio-connection-kit-devel libsndfile-devel cmake \
    fftw-devel libXt-devel git gcc-c++ libX11-devel qt5-qtwebkit-devel \
    qt5-qtlocation-devel qt5-qtsensors-devel systemd-devel libatomic avahi-devel \
    qt5-qttools-devel emacs alsa-lib-devel 

## Obtaining the source code

Simply clone the git repository:

    git clone https://github.com/supercollider/supercollider.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'supercollider'.: Permission denied

Cloning the repository will create a folder called supercollider containing the source code.

### Getting the submodules

From within the supercollider directory, run the following:

    git submodule init && git submodule update

### Linking to libatomic
As indicated in [this Sourceforge question](http://stackoverflow.com/questions/31381892/fedora-22-compile-atomic-is-lock-free), CMakeLists.txt needs to be modified to include the directive `set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")`.  This can be inserted near the top of the file, modifying the original to read as follows;

```
project (SuperCollider)
set(CMAKE_CXX_LINK_FLAGS "${CMAKE_CXX_LINK_FLAGS} -latomic")
if (CMAKE_SYSTEM_NAME MATCHES "Linux")
    set(LINUX 1)
endif()
...
...
```
## Running cmake

Create a directory inside supercollider called build. From within supercollider/build, run the following:

    cmake  ..

(Notice the space between `cmake` and the dots.)

## Building and Installing

Use the following commands to build and install Supercollider;

```
make
sudo make install
```
## Installing the plugins
### Information you need
#### Where to install the plugins
When SuperCollider starts up, it looks for the plugins in a particular location. You need to know this location in order to control where the plugins get installed.
Start the SuperCollider IDE, and look at the post window. The following is part of the post window output on my machine: 

    NumPrimitives = 711
    compiling dir: '/usr/local/share/SuperCollider/SCClassLibrary'
    compiling dir: '/usr/local/share/SuperCollider/Extensions'
    pass 1 done

Look for the two lines starting 'compiling dir:'. The second quotes the location we want. Remove the trailing '/share/SuperCollider/Extensions' bit and make a note of it. So in my case, the location is '/usr/local'.

This location will be referred to as **PluginLocation** for the remainder of this article.
#### Where the header include files are
You need to know where these files are when you install the plugins.
To locate the directory containing the header include files, search your file system (not just your home folder) for a file called 'SCVersion.txt'. The directory containing this file, in my case '/home/badnumbers/supercollider', is the one you want.

This location will be referred to as **HeaderIncludeFileLocation** for the remainder of this article.

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

If the previous instructions have been followed, the installation would be under '/usr/local'.  In this
case the following command is used to build the plugins:

    cmake -DSC_PATH=/usr/local/include/SuperCollider/ -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release ..

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