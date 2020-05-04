This document describes how SuperCollider decides which platforms to support. For information on which versions of SuperCollider support which platforms, see the README.md or the website download page.

## Support guarantees

The development community for SuperCollider has agreed on some guarantees about support for various platforms and
toolchains. Anything that breaks these guarantees should be fixed as soon as possible.

These guarantees should not be taken as an indication that we do not intend to support older platforms. On the contrary,
care should be taken not to lose support for platforms with which SuperCollider is currently compatible, unless there
are good reasons for doing so, and patches to add or restore support for any platform are welcome.

Reasons to drop support include:
- newer versions of tools and libraries have dropped support
- security issues
- the OS vendor itself has dropped support (for example, in Windows or macOS SDKs)
- significant features require a feature not available on an older platform, and there is no practial way to make the
  feature configurable

These guarantees are given as both a number of years and number of releases. Whichever period is longer applies. For
instance, macOS is supported for 2 years and 2 major releases. That means that any new version of macOS released in
the last 2 years is supported, _and_ that the last two major releases of macOS are always supported. At
present (2020-04-02) that would be macOS Mojave 10.14 and Catalina 10.15.

These guarantees are for the official releases published on GitHub and the supercollider.github.io website
(pre-compiled binaries on macOS and Windows, and a built-from-source binary on Linuxes).

### Platforms

The following platforms are supported:
- macOS: 2 years, 2 major releases (i.e. Mojave 10.14, Catalina 10.15)
- Windows: 4 years, 4 major updates
- Ubuntu: 4 years, 2 LTS releases
- Debian: 4 years, 2 major releases
- Fedora: latest release
- Arch Linux: latest release
- Raspberry Pi (Raspbian): latest release
- BeagleBone Black (Debian): latest release

"Compatibility" on Linuxes means there exists some toolchain easily obtainable -- preferably through the standard
package manager of that plaform, or the one used for cross-compiling -- that can build SuperCollider.

### Toolchains

SuperCollider also makes some guarantees about the toolchains (libraries, compilers, and other third-party software)
that can be used to compile it.

The official minor release of SuperCollider is guaranteed to be compatible with:
- Xcode: 2 years, 2 major releases
- gcc: 4 years, 4 major releases
- clang: 4 years, 4 major releases
- MSVC: 4 years, 2 major releases
- Qt: 2 years, 1 LTS release

As much as possible, SuperCollider should support building with the latest release of Boost, and the version packaged
in the source tree should be updated reasonably soon after a release.

Other libraries and tools which SuperCollider uses:
- CMake
- libsndfile
- libjack
- fftw
- git
- ALSA
- libudev
- libreadline
- Asio SDK
- NSIS
- libyaml-cpp

These are not given guarantees either because:
- a compatible version is included in the SuperCollider repository itself, or
- the library is relatively stable and so no additional compatibility requirements are necessary, or
- there have been few compatibility issues with the library.

Support guarantees can be added if needed.

### Patch releases

To the extent that it is possible and practical, the supported platforms and toolchains for a minor SuperCollider
release should also be supported by patch releases within that same minor release. For example, if SuperCollider
3.11.0 supports Debian Buster, so should 3.11.1, 3.11.2, and so on.