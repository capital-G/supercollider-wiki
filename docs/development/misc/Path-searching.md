# Path searching

Work in progress document. Please add or correct info as you see fit.

The following are parts of SuperCollider where path configuration coems into play:

- scide finds the sclang executable.
- scide finds its own configuration file.
- scide finds sclang's configuration file.
- sclang finds the scsynth/supernova executable.
- sclang finds its own class library and startup file.
- SCDoc (part of sclang) finds all help files and a location to render help files.
- scsynth/supernova finds its own plugins.

## Important directories

- `${CMAKE_INSTALL_PREFIX}`, set while configuring CMake.
  - Linux: defaults to `/usr/local/`.
  - Windows: `C:\Program Files\SuperCollider\`.
- `SC_DATA_DIR`, a compile-time definition set to `${CMAKE_INSTALL_PREFIX}/share/SuperCollider` only on Linux.
- System App Support Directory
  - On Linux this contains the SC class library, examples, sounds, HID_support, help source, Extensions and translations. On Mac the directory needs to be created and is a search path for systemwide Extensions.
  - Linux: `${CMAKE_INSTALL_PREFIX}/share/SuperCollider`.
  - macOS: `/Library/Application Support/SuperCollider/`.
  - Windows: `%PROGRAMDATA%/SuperCollider/`
- System Extension Directory: `<System App Support Directory>/Extensions/`
  - This is the location of quarks and plugins that are installed "system wide" for this SuperCollider install.
- User App Support Directory
  - Contains: recordings, SynthDef files, downloaded Quarks.
  - Linux: `$XDG_DATA_HOME/SuperCollider`, defaulting to `~/.local/share/SuperCollider`. Compliant with the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/basedir-spec-latest.html).
  - macOS: `$XDG_DATA_HOME/SuperCollider`, or if not present, `~/Library/Application Support/SuperCollider`.
- User Extension Directory: `<User App Support Directory>/Extensions/`.
  - A search location for server plugins.
- User Config Directory
  - Default location for scide and sclang configuration files.
  - Linux: `$XDG_CONFIG_HOME/SuperCollider`, defaulting to `~/.config/SuperCollider`, compliant with the XDG Base Directory Specification.
  - macOS: `$XDG_CONFIG_HOME/SuperCollider`, or if not present, this is the same as the User App Support Directory.
- Resource Directory
  - On Linux and Windows this is a search location for server plugins. On Mac this is the location of the scsynth executable, SC class library, plugins and assets.
  - Linux: `SC_DATA_DIR`, or if not available, `${CMAKE_INSTALL_PREFIX}/lib${LIB_SUFFIX}/SuperCollider/`.
  - Mac: `SuperCollider.app/Contents/Resources`

## sclang finds scsynth/supernova

The shell command to run the server is configurable in sclang, and stored as `Server.program`. The rules are:

- **macOS:** `"exec %/scsynth".format((Platform.resourceDir +/+ "../Resources").shellQuote)`
- **Linux:** `"exec scsynth"`
- **Windows:** `"scsynth.exe"`

Linux and Windows will only be able to find scsynth if it is in the system PATH.

## sclang finds class library

When sclang starts up, it searches for files ending in the `.sc` extension. The logic that sclang uses to determine search paths is as follows:

- If the `-a` command line option is NOT provided:
  - The Resource Directory, the System Extension Directory, and the User Extension Directory are included.
- If the `-l` command line argument is passed, it is read as a YAML configuration file. This file can contain lists of paths to be included and excluded, in addition to (and potentially overriding) the default paths. Note that all relative paths are relative to the current working directory, not to the location of the YAML file.
- If the `-l` command line argument is not passed, sclang looks for `<User Config Directory>/sc_lang_conf.yaml`. If that exists, then it contain additional paths to include and exclude.

## scsynth finds plugins

`initialize_library` in `SC_Lib_Cintf` determines the following rules:

- If the `-U` command-line parameter is specified, it is searched.
- Otherwise:
  - If the compile-time definition `SC_PLUGIN_DIR` is set, it is searched (can be set through CMake using `cmake -DSC_PLUGIN_DIR=<path> ..`).
    - By default, this is not set except on Linux, where its default value is `${CMAKE_INSTALL_PREFIX}/lib${LIB_SUFFIX}/SuperCollider/plugins`.
  - The directory `<Resource>/plugins/` is searched.
  - The System Extension Directory is searched.
  - The User Extension Directory is searched.
  - If the environment variable `SC_PLUGIN_PATH` is set, it is searched.

The "search" operation looks for all files ending in `.scx` (on Windows or macOS) or `.so` (on Linux).

## scide finds sclang

- macOS uses `<Resource Directory>/../MacOS/sclang`.
- Linux and Windows simply run `sclang`.

In all cases, the working directory is configured as the "Runtime Directory" in the IDE settings.

## scide finds its own configuration file

Hardcoded as `<User Config Directory>/sc_ide_conf.yaml`.

## Design goals for improving SuperCollider's search paths

- **Easier standalone packaging.** It should be possible to distribute the entire SuperCollider bundle in a self-contained tarball.
- **AppImage distribution for Linux.** A corollary of standalone packaging that will solve some packaging issues for Linux.
- **Allow concurrently installed major versions of SC.** SC 3.x versions all conflict with each other.
