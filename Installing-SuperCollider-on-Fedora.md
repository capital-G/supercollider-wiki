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

To install each package, just use (for example):

    sudo yum install gcc