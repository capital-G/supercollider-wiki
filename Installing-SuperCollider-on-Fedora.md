SuperCollider is not available within the official Fedora repositories. There are two ways to install SuperCollider: using the Stanford [Planet CCRMA repo](http://ccrma.stanford.edu/planetccrma/software/planetccrma.html) or building it from source.

### Install via Planet CCRMA

Please see the [Planet CCRMA](http://ccrma.stanford.edu/planetccrma/software/planetccrma.html) website for instructions on how to add this repository to your system. The SuperCollider packages available in this repository can be installed using `dnf install`.

### Building from source

SuperCollider's [Linux Readme](https://github.com/supercollider/supercollider/blob/master/README_LINUX.md) has all the information you need to build SuperCollider from source. The following should help you install the required dependencies and build SuperCollider on a recent Fedora system.

#### Installing dependencies

The following packages are required and are available in the Fedora repositories.

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
* boost-devel
* systemd-devel (provides libudev.h)
* libatomic
* avahi-devel 
* readline-devel
* qt5-qtlocation-devel
* qt5-qtsensors-devel
* qt5-qttools-devel 
* qt5-qtwebengine-devel
* qt5-qtwebsockets-devel
* qt5-qtsvg-devel 

The following packages are optional:
* emacs
* qjackctl
* ccache

The required and optional packages listed above may be installed with the following command;
```
  $ sudo dnf install gcc gcc-c++ cmake git jack-audio-connection-kit-devel          \
    libsndfile-devel fftw-devel libXt-devel libX11-devel boost-devel alsa-lib-devel \
    systemd-devel libatomic avahi-devel qt5-qtlocation-devel qt5-qtsensors-devel    \
    readline-devel qt5-qtwebengine-devel qt5-qttools-devel                          \
    qt5-qtwebsockets-devel qt5-qtsvg-devel emacs qjackctl ccache
```

#### A note about JACK 

You may have issues running JACK with real time scheduling privileges on Fedora. The following should allow you to run JACK in Realtime mode.

First, be sure to add your user to the **jackuser** group:

```
$ sudo usermod -a -G jackuser YOUR_USERNAME
```

Second, comment out the section that relates to the **pulse-rt** group in `/etc/security/limits.d/95-jack.conf`. The config file should like something like this:

```
$ cat /etc/security/limits.d/95-jack.conf
# Default limits for users of jack-audio-connection-kit

@jackuser - rtprio 80
@jackuser - memlock unlimited 

# @pulse-rt - rtprio 20
# @pulse-rt - nice -20
```

Restart your computer after completing the above.

## Getting the SuperCollider source code

Simply clone the SuperCollider git repository to a sensible location on your system:
```
git clone --recursive https://github.com/supercollider/supercollider.git
```

With the `--recursive` flag, the repository's submodules are also cloned.

Cloning the repository will create a folder called **supercollider** containing the source code.

#### Getting the submodules

If you cloned the SuperCollider repository without the `--recursive` flag, you will need to manually initialise and update the submodules. From within the **supercollider** directory, run the following:
```
git submodule update --init
```

#### Running cmake

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

#### Building and Installing

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


#### Installing the sc3-plugins
The sc3-plugins are an optional set of extension plugins for the SuperCollider3 audio synthesis server. These third-party plugins provide additional synthesis, analysis, and other capabilities for the sound server. 

Please note that these UGens are, on average, less stable and well-maintained than the core collection included with SuperCollider. Use at your own risk!

**Note:** Extensions for the SuperCollider programming language are different. They are collected within the **Quarks** packaging system included in SuperCollider.
 

#### Getting the source code for the sc3-plugins
Simply clone the sc3-plugins git repository to a sensible location on your system:
```
git clone --recursive https://github.com/supercollider/sc3-plugins.git
```

With the `--recursive` flag, the repository's submodules are also cloned.

Cloning the repository will create a folder called **sc3-plugins** containing the source code.

#### Getting the submodules
If you cloned the sc3-plugins repository without the `--recursive` flag, you will need to manually initialise and update the submodules. From within **sc3-plugins**, run the following:
```
git submodule update --init
```

#### Running cmake
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

#### Finally, building the plugins
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

#### Checking the installation worked
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

## Getting help
If you still don't have any luck with the above, ask a question [here](http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/SuperCollider-Users-New-Use-this-f2676391.html), providing as much information as you can.