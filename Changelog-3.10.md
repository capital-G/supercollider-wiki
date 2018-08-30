How to maintain this changelog
==============================

This changelog documents the publicly visible changes since the most recent SuperCollider release. A change is worth putting here if it affects users, such as breaking changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

The website [Keep a CHANGELOG](http://keepachangelog.com/en/0.3.0/) is a major inspiration for the organization of the changelog. Changes to each component of SuperCollider are subdivided into Added, Changed, Deprecated, Removed, Fixed, and Security, in that order.

Please provide the link to the PR with every entry in the changelog for easy navigation.

Try to exercise common sense in keeping this log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. In case of doubt, prefer inclusion over exclusion.

Release to-do list
------------------

Write a blurb to overview the release. Use the `package/contributor-list-generator` node.js script to generate a list of contributors, and add it to the changelog.

Post the changelog to the following announcement channels:

- CHANGELOG.md: post full version with all pull request links
- GitHub release page: post an abbreviated version
- "News in 3.x" helpfile: post full version without pull request links
- GitHub website: post an abbreviated version
- sc-users mailing list: post an abbreviated version
- Facebook group: post an abbreviated version
- Reddit (/r/supercollider): post an abbreviated version

General: Added
-----

A `NO_X11` option has been added to the build system so that server plugins requiring an X server such as MouseX can be omitted ([#3738](https://github.com/supercollider/supercollider/pull/3738)).

General: Changed
-------

sclang and scide have long been stuck with Qt 5.5 due to Qt dropping QtWebKit for QtWebEngine. They have been upgraded for compatibility with Qt 5.7+. We recommend using the most recent version of Qt. The impacts of this change include:

- sclang and scide now build on Visual Studio 2015 and later. (Previously, Windows users had to obtain the now-ancient Visual Studio 2013.)
- UserView now supports Retina/HiDPI display.
- A somewhat different build process on Linux. See the README.

The minimum required version is now CMake 3.5 instead of CMake 2.8 ([#3656](https://github.com/supercollider/supercollider/pull/3656)).

scel (the emacs package) is now a submodule ([#3519](https://github.com/supercollider/supercollider/pull/3519)).

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

Many issues with Unicode paths on Windows were fixed in 3.9. A few remaining cases involving sound files remained, and are now fixed ([#3720](https://github.com/supercollider/supercollider/pull/3720)):

- supernova's sound file backend, buffer manager, and plugin loading
- NRT mode in scsynth
- `/b_read` family of commands in scsynth
- `SoundFileView` in the sclang GUI

Fixed a build failure with the CMake option `SYSTEM_YAMLCPP=on` ([#3558](https://github.com/supercollider/supercollider/pull/3558)).

Fixed a misleading deprecation warning when `CMAKE_INSTALL_PREFIX` is set to the home directory in Linux ([#3613](https://github.com/supercollider/supercollider/pull/3613)).

scsynth and supernova: Added
-----

supernova now has latency compensation ([#3790](https://github.com/supercollider/supercollider/pull/3790)).

scsynth and supernova: Changed
-------

scsynth and supernova: Deprecated
----------

scsynth and supernova: Removed
------

scsynth and supernova: Fixed
-----

scsynth's latency compensation had a math error that ended up doubling the latency. It is fixed now ([#3790](https://github.com/supercollider/supercollider/pull/3790)).

For consistency with scsynth, supernova no longer requires the final argument to `/b_allocReadChannel` ([#3826](https://github.com/supercollider/supercollider/pull/3826)).

Fixed a missing newline in some of supernova's error messages ([#3897](https://github.com/supercollider/supercollider/pull/3897)).

Fixed errors in supernova's `/s_getn` ([#3893](https://github.com/supercollider/supercollider/pull/3893)).

UGens: Added
-----

UGens: Changed
-------

UGens: Deprecated
----------

UGens: Removed
-------

UGens: Fixed
-----

Fixed clicks in Convolution2L ([#3687](https://github.com/supercollider/supercollider/pull/3687)).

sclang: Added
-----

Menus are now supported in the Qt GUI. See help files for `Menu`, `MenuAction`, `ToolBar`, and `MainMenu` ([#2504](https://github.com/supercollider/supercollider/pull/2504)).

Added wrappers for over 100 special mathematical functions (gamma function, Bessel functions, elliptic integrals, etc.) from the Boost library ([#3672](https://github.com/supercollider/supercollider/pull/3672)).

SerialPort now works on Windows ([#3809](https://github.com/supercollider/supercollider/pull/3809)).

`FileDialog` and `Dialog` now support a "path" argument that specifies a default directory when the dialog appears ([#3508](https://github.com/supercollider/supercollider/pull/3508)).

`QTreeView` has a new method: `setColumnWidth` ([#3560](https://github.com/supercollider/supercollider/pull/3560)).

sclang: Changed
-------

**Breaking change:** `Float:asString` now always produces a decimal point, so `3.0.asString` is now `"3.0"` instead of `"3"` ([#3585](https://github.com/supercollider/supercollider/pull/3585)).

**Breaking change:** The `server` argument has changed to `target` in `Function:asBuffer`, `Function:loadToFloatArray`, and `Function:plot`, and now allows spawning the plotting synth relative to a group or node rather than just a server ([#3088](https://github.com/supercollider/supercollider/pull/3088)).

**Breaking change:** `File:mkdir` now returns a Boolean indicating whether the operation was successful. Previously, it returned the File object ([#3635](https://github.com/supercollider/supercollider/issues/3635)).

Scrollbars now always appear for ScrollView on Linux an Windows, as a temporary workaround for a very odd dependency on the use of the scroll wheel ([#3686](https://github.com/supercollider/supercollider/pull/3686)).

sclang: Deprecated
----------

sclang: Removed
-------

Removed some unused Qt dependencies from the build system ([#3472](https://github.com/supercollider/supercollider/pull/3472)).

sclang: Fixed
-----

**Breaking change:** Fixed a long-standing math error in `SimpleNumber:expexp` ([#3786](https://github.com/supercollider/supercollider/pull/3786)).

Fixed extreme CPU usage of sclang when built without Qt ([#3772](https://github.com/supercollider/supercollider/pull/3772)).

On Windows, the directory where extensions were installed was accidentally changed in 3.9. It has been reverted ([#3751](https://github.com/supercollider/supercollider/pull/3751)).

Fixed a crash when calling `File.copy` when the destination exists ([#3633](https://github.com/supercollider/supercollider/pull/3633)).

Fixed two `Array:lace` issues: a crash when any element is an empty array, and an error when no length argument is provided and any element is not an array ([#3716](https://github.com/supercollider/supercollider/issues/3716)).

Fixed conditions where `Integer:forBy` can cause sclang to freeze when the step size is 0 or a floating point value with an absolute value less than 1 ([#3804](https://github.com/supercollider/supercollider/pull/3804)).

Fixed some incorrect output in `FunctionDef:dumpByteCodes` ([#3803](https://github.com/supercollider/supercollider/pull/3803)).

Fixed `Node:release` getting stuck on negative release times, which are now equivalent to 0 ([#3741](https://github.com/supercollider/supercollider/pull/3741)).

Fixed `==` on `Signal` objects randomly returning the wrong result ([#3970](https://github.com/supercollider/supercollider/pull/3970)).

Class library: Added
-----

`UnitTest.passVerbosity` allows changing the verbosity of test failure reports. See the `UnitTest` help file for more information ([#3615](https://github.com/supercollider/supercollider/pull/3615)).

Added new UGen methods `.snap` and `.softRound` ([#3429](https://github.com/supercollider/supercollider/pull/3429/files)).

`Node:query` has a new `action` argument, allowing specification of a callback function ([#3701](https://github.com/supercollider/supercollider/pull/3701)).

`.degrad` and `.raddeg` are now implemented for UGens ([#3821](https://github.com/supercollider/supercollider/pull/3821)).

Class library: Changed
-------

The default behavior of `SerialPort.devices` pattern matching has been improved to match a wider variety of devices on macOS and Linux ([#3809](https://github.com/supercollider/supercollider/pull/3809)).

Internal calls to `.interpret` have been removed from `Color.fromHexString` and `History.unformatTime`, improving both performance and security ([#3527](https://github.com/supercollider/supercollider/pull/3527)).

Class library: Deprecated
----------

`SerialPort.cleanupAll` is deprecated ([#3809](https://github.com/supercollider/supercollider/pull/3809)).

Providing an integer index for `SerialPort.new` is deprecated ([#3809](https://github.com/supercollider/supercollider/pull/3809)).

Class library: Removed
-------

Class library: Fixed
-----

`BufWr.ar` no longer allows its input signals to be control rate, which caused the server to read from garbage memory ([#3749](https://github.com/supercollider/supercollider/pull/3749)).

`Buffer:query` returned incorrect results if multiple query messages are sent at once. This has been fixed ([#3645](https://github.com/supercollider/supercollider/pull/3645)).

Fixed fragilities in path joining methods such as `+/+`, `withTrailingSlash`, and `withoutTrailingSlash` ([#3634](https://github.com/supercollider/supercollider/pull/3634)).

Fixed bugs when certain pattern classes are passed in 0 as the number of repeats ([#3603](https://github.com/supercollider/supercollider/pull/3603)).

Fixed `Event.addEventType` ignoring the `parentEvent` argument ([#3736](https://github.com/supercollider/supercollider/pull/3736)).

Fixed `Pkey` being skipped because the default number of repeats is `nil` instead of `inf` ([#3724](https://github.com/supercollider/supercollider/pull/3724)).

Fixed some harmless but annoying errors about extensions of nonexistent classes when sclang is built without Qt ([#3770](https://github.com/supercollider/supercollider/pull/3770)).

`ProxySpace:linkDoc` was broken — switching documents did not actually change ProxySpaces. This is fixed now ([#3764](https://github.com/supercollider/supercollider/pull/3764)).

`Recorder:prepareForRecord` produced an error if the recordings path does not exist. It now makes the directory if it doesn't exist ([#3788](https://github.com/supercollider/supercollider/pull/3788)).

Fixed bugs when providing multiple paths in `ServerOptions:ugensPluginPath` ([#3754](https://github.com/supercollider/supercollider/pull/3754)).

Fixed `HelpBrowser` (the class, not the IDE help browser) being unusable since it didn't trigger rendering of help files when links are clicked ([#3832](https://github.com/supercollider/supercollider/pull/3832)).

Fixed some bugs in `EnvGate`: throwing an error when `fadeTime` is a constant rather than a UGen input, and `i_level` not behaving as documented ([#3797](https://github.com/supercollider/supercollider/pull/3797)).

Fixed occasional hangs when rebooting supernova ([#3848](https://github.com/supercollider/supercollider/pull/3848)).

Fixed confusing user feedback with the "Check for updates" button in the quarks GUI ([#3986](https://github.com/supercollider/supercollider/pull/3986)).

`Buffer` methods ensure that the buffer number in outbound OSC messages is an integer ([#3907](https://github.com/supercollider/supercollider/pull/3907)). This fixes errors in supernova, which is stricter than scsynth about the buffer number type.

IDE & SCDoc: Added
-----

The IDE has a prettier default theme ([#4025](https://github.com/supercollider/supercollider/pull/4025)). The old theme still exists as "classic."

IDE & SCDoc: Changed
-------

The IDE now has a unified look across all platforms, and its color scheme adapts to match the editor theme ([#3950](https://github.com/supercollider/supercollider/pull/3950)).

The SCDoc TOC and menubar have been redesigned again ([#3831](https://github.com/supercollider/supercollider/pull/3831)).

Various tweaks to the appearance of the IDE: nicer tabs ([#3992](https://github.com/supercollider/supercollider/pull/3992)), better border colors ([#4022](https://github.com/supercollider/supercollider/pull/4022)).

IDE & SCDoc: Deprecated
----------

IDE & SCDoc: Removed
-------

IDE & SCDoc: Fixed
-----

When starting the IDE, detached docklet sometimes spawn as unresponsive. This has been fixed ([#3660](https://github.com/supercollider/supercollider/pull/3660)).

Syntax colors in the help browser now match the IDE ([#3883](https://github.com/supercollider/supercollider/pull/3883)).

Only one preference window can be open at a time now ([#3988](https://github.com/supercollider/supercollider/pull/3988)).

Fixed tabs reversing in order when restoring a session ([#3942](https://github.com/supercollider/supercollider/pull/3942)).
