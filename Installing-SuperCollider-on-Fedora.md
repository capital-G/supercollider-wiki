# Installing SuperCollider on Fedora

There doesn't appear to be the equivalent of a PPA for Fedora. It seems installing from source is the way to go.

I'm following the instructions [here](https://github.com/supercollider/supercollider/blob/master/README_LINUX.md), but clarifying them for the benefit of noobs.

## Obtaining dependencies

I couldn't find out what 'libjack' is, so I'm assuming that it's obtained through the package `jack-audio-connection-kit`.

The following packages are required and are available through yum.

* gcc
* jack-audio-connection-kit
* libsndfile
* cmake
* fftw
* libXt (note capital 'X')
* git
* gcc-c++

To install each package, just use (for example):

    sudo yum install gcc

You may already have one or more of these packages installed. Using `yum install` for a package you already have installed will do no harm.

## Obtaining the source code

Simply clone the git repository:

    git clone https://github.com/supercollider/supercollider.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

Cloning the repository will create a folder called supercollider containing the source code.

## Running cmake

Create a directory inside supercollider called build. From within supercollider/build, run the following:

    cmake  ..

(Notice the space between `cmake` and the dots.)

Resulting output:

    -- The C compiler identification is GNU 4.9.2
    -- The CXX compiler identification is unknown
    -- Check for working C compiler: /usr/bin/cc
    -- Check for working C compiler: /usr/bin/cc -- works
    -- Detecting C compiler ABI info
    -- Detecting C compiler ABI info - done
    CMake Error at CMakeLists.txt:1 (project):
      No CMAKE_CXX_COMPILER could be found.
    
      Tell CMake where to find the compiler by setting either the environment
      variable "CXX" or the CMake cache entry CMAKE_CXX_COMPILER to the full path
      to the compiler, or to the compiler name if it is in the PATH.
    
    
    -- Configuring incomplete, errors occurred!
    See also "/home/david/supercollider/build/CMakeFiles/CMakeOutput.log".
    See also "/home/david/supercollider/build/CMakeFiles/CMakeError.log".




