# Installing SuperCollider on Fedora

There doesn't appear to be the equivalent of a PPA for Fedora. It seems installing from source is the way to go.

## Obtaining gcc

### Determine if gcc is installed

    gcc --version

The command will not be recognised if gcc is not installed. If it's not:

    sudo yum install gcc

After installation, try:

    gcc --version

... to ensure that the version is equal or greater than 4.6.


## Obtaining jack and libjack

I couldn't find much information about what libjack is.

    sudo yum install jack-audio-connection-kit

