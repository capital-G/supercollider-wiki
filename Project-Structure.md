
- **`.github`**: PR and issue template for GitHub
- **`.travis`**: scripts for Travis CI
- **`cmake_modules`**: Find and Config modules for CMake
- **`common`**: C++ files needed by multiple components of the project
- **`editors`**: Files for `scide` and editor extensions
  - **`sc-el`**: the SuperCollider Emacs package, `scel`
  - **`sc-ide`**: source for `scide`
  - **`sced`**: source for the SuperCollider `gedit` plugin, `sced`
  - **`scvim`**: the SuperCollider Vim package, `scvim`
- **`examples`**: SuperCollider code examples, packaged into release assets
- **`external_libraries`**: C and C++ third-party libraries
  - **`boost`**: root of Boost C++ sources
  - **`boost_sync`**: contains [Boost::sync](https://github.com/boostorg/sync), a synchronization lib which was never
    integrated into Boost proper.
  - **`hidapi`**: [HID API](http://www.signal11.us/oss/hidapi/) project, which `sclang` uses for HID capability. Our
    fork is significantly patched for cross-platform compatibility.
  - **`icu`**: IBM's [ICU](http://site.icu-project.org/) library
  - **`jackey`**: a simple header for Jack that makes working with Jack Metadata easier. Used by `scsynth` and
    `supernova`, but not in current builds (only when `SC_JACK_USE_METADATA_API` is defined, may be old work that was
    never completed)
  - **`libsndfile`**: header for [`libsndfile`](http://www.mega-nerd.com/libsndfile/), for working with audio file
    formats. Used by `sclang` and the servers
  - **`nova-simd`**: `nova-simd`, a framework for SIMD vector functions
  - **`nova-tt`**: `nova-tt`, a library for cross-platform thread synchronization
  - **`oscpack_1_1_0`**: [Oscpack](http://www.rossbencina.com/code/oscpack), a library for working with OSC packets.
  - **`portaudio_sc_org`**: SC's fork of [PortAudio](http://www.portaudio.com/), which has been modded for
    cross-platform work
  - **`portmidi`**: [PortMIDI](http://portmedia.sourceforge.net/portmidi/), a cross-platform library for MIDI I/O
  - **`simplejson-2.3.2`**: [simplejson](https://pypi.python.org/pypi/simplejson/), a Python package used by `sced`
  - **`yaml-cpp`**: [yaml-cpp](https://github.com/jbeder/yaml-cpp), a C++ library for YAML
- **`HelpSource`**: schelp source for SCDoc
- **`icons`**: contains icon files for the project
- **`include`**: C++ headers for client code, including server plugins
- **`lang`**: C++ source for `sclang`
  - **`LangSource`**: sources for the core of the language, including the interpreter
  - **`LangPrimSource`**: sources for SuperCollider primitive functions. Loosely organized by functionality.
- **`package`**: tools for preparing and packaging release assets, including changelog-related scripts
- **`platform`**: various platform-specific bits
- **`QtCollider`**: sources for the Qt GUI extensions to `sclang`
- **`SCClassLibrary`**: SuperCollider sources for the core class library
- **`SCDoc`**: C++ sources for SCDoc, the .schelp parser
- **`server`**: C++ sources for `scsynth`, `supernova`, and server plugins
  - **`plugins`**: sources for server plugins (UGens)
  - **`scsynth`**: sources for scsynth
  - **`supernova`**: sources for supernova
- **`sounds`**: sound files, packaged into release assets
- **`testsuite`**: test files
  - **`classlibrary`**: SuperCollider-language tests for the core class library
  - **`sclang`**: tests for `sclang`
  - **`server`**: C++ tests for `scsynth` and `supernova`
- **`tools`**: various tools useful for maintainers

Important files in the root directory are:

- **`.appveyor.yml`**: config file for AppVeyor CI
- **`.travis.yml`**: config file for Travis CI
- **`build_sclang_cfg.in`**: config file used for the special `SC_DOC_RENDER` build target
- **`CMakeLists.txt`**: main CMake file
- **`README_*`**: readmes for various platforms
- **`SCVersion.txt`**: the primary versioning document. The version number is stored here and nowhere else.
- **`travis_test_run_proto.json`**: config file used by qpm to run tests in CI
