# Installing SuperCollider on Fedora

There doesn't appear to be the equivalent of a PPA for Fedora. It seems installing from source is the way to go.

I'm following the instructions [here](https://github.com/supercollider/supercollider/blob/master/README_LINUX.md), but clarifying them for the benefit of noobs.

## Obtaining dependencies

I couldn't find out what 'libjack' is, so I'm assuming that it's obtained through the package `jack-audio-connection-kit`.

The following packages are required and are available through yum.

* gcc
* jack-audio-connection-kit-devel
* libsndfile-devel
* cmake
* fftw
* libXt-devel (note capital 'X')
* git
* gcc-c++
* libX11-devel (not actually sure devel is needed - check at some point)
* qtwebkit-devel

To install each package, just use (for example):

    sudo yum install gcc

You may already have one or more of these packages installed. Using `yum install` for a package you already have installed will do no harm.

## Obtaining the source code

Simply clone the git repository:

    git clone https://github.com/supercollider/supercollider.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

Cloning the repository will create a folder called supercollider containing the source code.

### Getting the submodules

From within the supercollider directory, run the following:

    git submodule init && git submodule update

## Running cmake

Create a directory inside supercollider called build. From within supercollider/build, run the following:

    cmake  ..

(Notice the space between `cmake` and the dots.)

Resulting output:

    -- SuperCollider Version: 3.7alpha0
    -- Build type defaulting to "RelWithDebInfo"
    -- Compiling with Qt GUI
    -- building boost libraries manually
    -- Could NOT find YAMLCPP (missing:  YAMLCPP_INCLUDE_DIR YAMLCPP_LIBRARY) 
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
    -- UDev not found.
    -- UDev: You can specify includes: -DUDEV_PATH_INCLUDES=/opt/udev/include
    --       currently found includes: UDEV_INCLUDE_DIR-NOTFOUND
    -- UDev: You can specify libs: -DUDEV_PATH_LIB=/opt/udev/lib
    --       currently found libs: UDEV_LIBRARIES-NOTFOUND
    CMake Warning (dev) at external_libraries/hidapi/CMakeLists.txt:58 (link_directories):
      This command specifies the relative path
    
        UDEV_LIBRARIES-NOTFOUND
    
      as a link directory.
    
      Policy CMP0015 is not set: link_directories() treats paths relative to the
      source dir.  Run "cmake --help-policy CMP0015" for policy details.  Use the
      cmake_policy command to set the policy and suppress this warning.
    This warning is for project developers.  Use -Wno-dev to suppress it.
    
    ===hidapi_parser cmakelists===
    -- using green fft
    -- Could NOT find Sndfile (missing:  SNDFILE_LIBRARY SNDFILE_INCLUDE_DIR) 
    CMake Error at server/plugins/CMakeLists.txt:126 (message):
      Cannot find libsndfile
    
    
    CMake Error at server/plugins/CMakeLists.txt:191 (message):
      Cannot find libsndfile
    
    
    CMake Error at /usr/share/cmake/Modules/FindX11.cmake:440 (message):
      Could not find X11
    Call Stack (most recent call first):
      server/plugins/CMakeLists.txt:231 (find_package)
    
    
    CMake Error: The following variables are used in this project, but they are set to NOTFOUND.
    Please set them or make sure they are set and tested correctly in the CMake files:
    UDEV_INCLUDE_DIR
       used as include directory in directory /home/david/supercollider/external_libraries/hidapi/linux
    UDEV_LIBRARIES
        linked by target "hidapi" in directory /home/david/supercollider/external_libraries/hidapi/linux
    
    -- Configuring incomplete, errors occurred!
    See also "/home/david/supercollider/build/CMakeFiles/CMakeOutput.log".
    See also "/home/david/supercollider/build/CMakeFiles/CMakeError.log".
    [david@localhost build]$ sudo yum install libsndfile
    [sudo] password for david: 
    Loaded plugins: langpacks
    Package libsndfile-1.0.25-14.fc21.x86_64 already installed and latest version
    Nothing to do