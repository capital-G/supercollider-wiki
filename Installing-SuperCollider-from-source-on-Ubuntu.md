This page gives instructions for installing SuperCollider on Ubuntu and its derived distributions (e.g. Linux Mint, Elementary OS). It covers building and installing SuperCollider and the sc3-plugins from source.

## Building SuperCollider
### Packages you need
You will need to install quite a few packages to build SuperCollider and the sc3-plugins. Below is a list of this software, along with the terminal commands to get it.
```
sudo apt-get install build-essential libsndfile1-dev libasound2-dev libavahi-client-dev libicu-dev libreadline6-dev libfftw3-dev libxt-dev libudev-dev pkg-config git cmake qt5-default qt5-qmake qttools5-dev qttools5-dev-tools qtdeclarative5-dev libqt5webkit5-dev qtpositioning5-dev libqt5sensors5-dev libqt5opengl5-dev
```

**Note**: The minimum required version of gcc is `4.8`. Most Linux systems meet this requirement. You can check your gcc version in a terminal with the command `gcc --version`.

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

Simply clone the SuperCollider git repository to a sensible location on your system:
```
git clone --recursive https://github.com/supercollider/supercollider.git
```

With the `--recursive` flag, the repository's submodules are also cloned.

Cloning the repository will create a folder called **supercollider** containing the source code.

### Getting the submodules

If you cloned the SuperCollider repository without the `--recursive` flag, you will need to manually initialise and update the submodules. From within the **supercollider** directory, run the following:
```
git submodule update --init
```

## Running cmake

Create a directory inside the **supercollider** folder called **build** and move to it:
```
mkdir build && cd build
```

From within **supercollider/build**, run the following:
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

Use the following commands to build and install SuperCollider:
```
make
sudo make install
```

If your CPU has multiple cores, you can take advantage of make's `-j` option. For example, a CPU containing 4 cores can run:
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

**Note:** Extensions for the SuperCollider programming language are different. They are collected within the **Quarks** packaging system included in SuperCollider.
 

### Getting the source code for the sc3-plugins
Simply clone the sc3-plugins git repository to a sensible location on your system:
```
git clone --recursive https://github.com/supercollider/sc3-plugins.git
```

With the `--recursive` flag, the repository's submodules are also cloned.

Cloning the repository will create a folder called **sc3-plugins** containing the source code.

### Getting the submodules
If you cloned the sc3-plugins repository without the `--recursive` flag, you will need to manually initialise and update the submodules. From within **sc3-plugins**, run the following:
```
git submodule update --init
```

### Running cmake
Create a directory inside the **sc3-plugins** folder called **build** and move to it:
```
mkdir build && cd build
```

From within **sc3-plugins/build**, run the following command, replacing `/path/to/your/supercollider/source` with the path to the SuperCollider source code on your system:
```
cmake -DSC_PATH=/path/to/your/supercollider/source ..
```

Running the following will post a list of all available flags that can be set in order to configure your build.
```
cmake -L ..
```

It's a good idea to set the cmake flags `CMAKE_BUILD_TYPE` and `NATIVE` to the same values that where used when building SuperCollider. In the end, your cmake configuration command might look something like this:
```
cmake -DSC_PATH=/path/to/your/supercollider/source -DCMAKE_BUILD_TYPE=Release -DNATIVE=ON ..
```

### Finally, building the plugins
From within **sc3-plugins/build**, run the following:
```
make
sudo make install
```

If your CPU has multiple cores, you can take advantage of make's `-j` option. For example, a CPU containing 4 cores can run:
```
make -j4
sudo make install
```

If building the sc3-plugins for the first time, run:
```
sudo ldconfig
```

### Checking the installation worked
If you have the IDE open, close it. Now open it again and boot the server.

Enter the following into the blank text window and run it:
```
{VOSIM.ar(Impulse.ar(100), 500, 3, 0.99)}.play
```

You should hear a buzzing sound. If you don't, double check and attempt the instructions again. 

## Uninstalling the sc3-plugins
To uninstall the sc3-plugins, from the **sc3-plugins/build** directory, run the following:
```
sudo make uninstall
```

# Getting help
If you still don't have any luck with the above, ask a question [here](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/SuperCollider-Users-New-Use-this-f2676391.html), providing as much information as you can.