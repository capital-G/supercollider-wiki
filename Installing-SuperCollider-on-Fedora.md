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

To install each package, just use (for example):

    sudo yum install gcc

You may already have one or more of these packages installed. Using `yum install` for a package you already have installed will do no harm.

## Obtaining the source code

Simply clone the git repository:

    git clone https://github.com/supercollider/supercollider.git

Although for installation purposes, it doesn't matter where in the file system you clone the repository, you will obviously need write access there. If you don't, when you attempt to clone you will see the error:

    fatal: could not create work tree dir 'sc3-plugins'.: Permission denied

Cloning the repository will create a folder called supercollider containing the source code.