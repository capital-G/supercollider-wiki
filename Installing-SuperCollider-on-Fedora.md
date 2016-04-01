# Installing SuperCollider on Fedora

There doesn't appear to be the equivalent of a PPA for Fedora. It seems installing from source is the way to go.

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

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

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

Resulting output:

```
-- SuperCollider Version: 3.7alpha1
-- Building from branch master, commit hash is 4b75ab6
-- Build type defaulting to "RelWithDebInfo"
-- Compiling with Qt GUI
-- building boost libraries manually
-- using bundled libyaml-cpp
CMake Warning (dev) at external_libraries/hidapi/CMakeLists.txt:3 (project):
  Policy CMP0048 is not set: project() command manages VERSION variables.
  Run "cmake --help-policy CMP0048" for policy details.  Use the cmake_policy
  command to set the policy and suppress this warning.

  The following variable(s) would be set to empty:

    PROJECT_VERSION
    PROJECT_VERSION_MAJOR
    PROJECT_VERSION_MINOR
    PROJECT_VERSION_PATCH
This warning is for project developers.  Use -Wno-dev to suppress it.

hidapi cmakelists
===linux hidraw cmakelists===
-- libudev stable: 1
-- Found UDev: /usr/lib64/libudev.so
--    include: /usr/include
===hidapi_parser cmakelists===
-- using fftw3f
-- Found jack: /usr/lib64/libjack.so
-- Audio API: jack
-- Found ALSA: /usr/lib64/libasound.so (found version "1.0.29") 
libsclang qt libs:Qt5::CoreQt5::GuiQt5::WidgetsQt5::NetworkQt5::WebKitQt5::WebKitWidgetsQt5::PrintSupportQt5::OpenGLQt5::SensorsQt5::QuickQt5::QmlQt5::SqlQt5::Positioning/usr/lib64/libm.so/usr/lib64/libX11.so
core: /usr/lib64/libQt5Core.so.5.4.2
-- Compiling with ALSA midi support
-- Building the Qt IDE
-- Building with Sced for gedit 3 (UNIX)
-- Configuring done
-- Generating done
-- Build files have been written to: /home/foo/bar/supercollider/build
```

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

So in my case, I would run:

    cmake -DSC_PATH=/home/badnumbers/supercollider -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release ..

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