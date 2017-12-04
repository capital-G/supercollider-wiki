# Installing SuperCollider on Fedora

SuperCollider is not available within the official Fedora repositories. There are two ways to install SuperCollider: using the Stanford [Planet CCRMA repo](http://ccrma.stanford.edu/planetccrma/software/) or building it from source.

## Planet CCRMA

Planet CCRMA documentation is not always up to date, here is an example installing SuperCollider on Fedora 25.

Install the repository package:

    # rpm -Uvh http://ccrma.stanford.edu/planetccrma/mirror/fedora/linux/planetccrma/25/i386/planetccrma-repo-1.1-3.fc25.ccrma.noarch.rpm

Install supercollider:

    # dnf search supercollider

    # dnf install -y supercollider supercollider-emacs supercollider-vim supercollider-sc3-plugins

## Install from source

SuperCollider's [Linux Readme](https://github.com/supercollider/supercollider/blob/master/README_LINUX.md) has all the information you need to build SuperCollider from source. The following should help you install the required dependencies and build SuperCollider on a recent Fedora system.

## Installing dependencies

The following packages are required and are available through `dnf` (or `yum`).

* gcc
* gcc-c++
* cmake
* git
* alsa-lib-devel 
* jack-audio-connection-kit-devel
* libsndfile-devel
* fftw-devel
* libXt-devel (note capital 'X')
* libX11-devel
* systemd-devel (provides libudev.h)
* libatomic
* avahi-devel 
* qt5-qtlocation-devel
* qt5-qtsensors-devel
* qt5-qttools-devel 
* qt5-qtwebengine-devel
* qt5-qtwebkit-devel 
* emacs  (optional)

The required packages may be installed with the following command;
```
    sudo dnf install gcc gcc-c++ cmake git jack-audio-connection-kit-devel \
    libsndfile-devel fftw-devel libXt-devel libX11-devel alsa-lib-devel \
    systemd-devel libatomic avahi-devel qt5-qtlocation-devel qt5-qtsensors-devel \
    qt5-qtwebengine-devel qt5-qttools-devel qt5-qtwebkit-devel emacs
```

## A note about JACK 

You may have issues running JACK with real time scheduling privileges on Fedora. Be sure to add your user to the **jackuser** and **pulse-rt** groups. You will need to reboot your system after running the following command:

```
sudo usermod -a -G jackuser,pulse-rt YOUR_USERNAME
```

## Obtaining the source code

Simply clone the git repository:
```
git clone https://github.com/supercollider/supercollider.git
```

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:
```
fatal: could not create work tree dir 'supercollider'.: Permission denied
```

Cloning the repository will create a folder called supercollider containing the source code.

### Getting the submodules

From within the supercollider directory, run the following:
```
git submodule init && git submodule update
```

## Running cmake

Create a directory inside the **supercollider** folder called **build** and move to it:
```
mkdir build && cd build
```

From within supercollider/build, run the following:
```
cmake  ..
```
(Notice the space between `cmake` and the dots.)

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

## Building and Installing

Use the following commands to build and install SuperCollider;

```
make
sudo make install
```
If your system has multiple cores, you can take advantage of make's `-j` option. For example, a system containing 4 cores can run:
```
make -j4
sudo make install
```
If building SuperCollider for the first time, run:
```
sudo ldconfig
```

## Uninstalling SuperCollider
From within you **supercollider/build** folder, run the following:
```
sudo make uninstall
```


## Installing the sc3-plugins
The sc3-plugins are an optional set of extension plugins for the SuperCollider3 audio synthesis server. These third-party plugins provide additional synthesis, analysis, and other capabilities for the sound server. 

Please note that these UGens are, on average, less stable and well-maintained than the core collection included with SuperCollider. Use at your own risk!

Note: Extensions for the SuperCollider programming language are different. They are collected within the Quarks packaging system.
 
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
Create a directory inside the **sc3-plugins** folder called **build** and move to it:
```
mkdir build && cd build
```

From within **sc3-plugins/build**, run the following:

    cmake -DSC_PATH=**HeaderIncludeFileLocation** -DCMAKE_INSTALL_PREFIX=**PluginLocation** -DCMAKE_BUILD_TYPE=Release ..

If the previous instructions have been followed, the installation would be under '/usr/local'. In this
case the following command is used to build the plugins:

    cmake -DSC_PATH=/usr/local/include/SuperCollider/ -DCMAKE_INSTALL_PREFIX=/usr/local -DCMAKE_BUILD_TYPE=Release ..

Don't miss out those two dots on the end!

### Finally, building the plugins
From within **sc3-plugins/build**, run the following:

    make
    sudo make install
    
If building for the first time, run:
```
sudo ldconfig
```

### Checking the installation worked
If you have the IDE open, close it. Now open it again and boot the server.

Enter the following into the blank text window and run it:

    {VOSIM.ar(Impulse.ar(100), 500, 3, 0.99)}.play

You should hear a buzzing sound. If you don't, double check and attempt the instructions again. 

## Uninstalling the sc3-plugins
To uninstall the sc3-plugins, from the **sc3-plugins/build** directory, run the following:

    sudo make uninstall

# Getting help
If you still don't have any luck with the above, ask a question [here](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/SuperCollider-Users-New-Use-this-f2676391.html), providing as much information as you can.