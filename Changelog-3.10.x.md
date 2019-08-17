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

General: Changed
-------

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

For people compiling with musl libc, some build errors have been fix ([#4535](https://github.com/supercollider/supercollider/pull/4535)).

scsynth and supernova: Added
-----

scsynth and supernova: Changed
-------

**Breaking change:** scsynth had a security issue where it listens to 0.0.0.0 by default. For most users, this is undesirable behavior since it allows anyone on your local network to send messages to scsynth! This default has been changed to 127.0.0.1 ([#4516](https://github.com/supercollider/supercollider/pull/4516)). To change it back (e.g. for networked server/client setups), use `-B 0.0.0.0` at the command line or `server.options.bindAddress = "0.0.0.0"`.

scsynth and supernova: Deprecated
----------

scsynth and supernova: Removed
------

scsynth and supernova: Fixed
-----

On Windows, scsynth was not able to select separate input and output devices. Since many audio drivers present inputs and outputs as separate devices, this caused major blocking issues for anyone using Windows with an external sound card. This has been fixed ([#4475](https://github.com/supercollider/supercollider/pull/4475)).

Fixed cases involving `ASyncPlugInCmd` where memory can be freed twice, causing scsynth to freeze ([#4456](https://github.com/supercollider/supercollider/pull/4456)).

Fixed a supernova compilation issue on Boost 1.67 ([#4447](https://github.com/supercollider/supercollider/pull/4447)).

Fixed server hangs happening in plugins employing SequencedCmd ([#4456](https://github.com/supercollider/supercollider/pull/4456)).

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

Fixed an initialization issue for the `trig` input to `Convolution2` ([#4341](https://github.com/supercollider/supercollider/pull/4341)).

sclang: Added
-----

sclang: Changed
-------

sclang: Deprecated
----------

sclang: Removed
-------

sclang: Fixed
-----

The `mouseWheelAction` of `View` erroneously reported `xDelta` and `yDelta` to be 0 in some cases. This is fixed ([#4423](https://github.com/supercollider/supercollider/pull/4423)).

Fixed incorrect mathematics in `SimpleNumber:series` ([#4454](https://github.com/supercollider/supercollider/pull/4454)).

Fixed a harmless but annoying warning in when running `HelpBrowser.instance` in sclang without the IDE ([#4488](https://github.com/supercollider/supercollider/pull/4488)).

Class library: Added
-----

The `-B` command-line flag to scsynth was missing a frontend in `ServerOptions`. This has been fixed by introducing `ServerOptions:bindAddress` ([#4516](https://github.com/supercollider/supercollider/pull/4516)).

Add `Platform.hasQtWebEngine` to query whether sclang was compiled with QtWebEngine support ([#4523](https://github.com/supercollider/supercollider/pull/4523)).

Class library: Changed
-------

Class library: Deprecated
----------

Class library: Removed
-------

Class library: Fixed
-----

Fix issues when using a regular `Buffer` (that is, not a `LocalBuf`) for FFT ([#4050](https://github.com/supercollider/supercollider/pull/4050)).

Lots of small issues in `Plotter` were fixed, especially related to the `domain` and `domainSpec` arguments ([4082](https://github.com/supercollider/supercollider/pull/4082)).

When changing the source of an input to a `NodeProxy`, discontinuities can happen even when smooth crossfading is requested. This has been fixed ([#4296](https://github.com/supercollider/supercollider/pull/4296)).

`ProxyMixer` no longer assumes the `ProxySpace` it is using to be the current environment ([#4339](https://github.com/supercollider/supercollider/pull/4339)).

The default recordings directory on Windows was the somewhat redundant `My Documents\SuperCollider\SuperCollider\Recordings`. The additional `SuperCollider` subdirectory has been removed ([#4420](https://github.com/supercollider/supercollider/pull/4420)).

In Events where `strum` is set, the releases of notes was erroneously done in reverse order. This is fixed ([#4406](https://github.com/supercollider/supercollider/pull/4406)).

Fix `EnvirGui` always creating a `SkipJack` due to incorrect logic concerning the `makeSkip` flag ([#4376](https://github.com/supercollider/supercollider/pull/4376)).

`SkipJack` would not remove itself properly when stopped by its stopTest. This is fixed ([#4376](https://github.com/supercollider/supercollider/pull/4376)).

Fixed class library compilation issues on Qt-less sclang installations ([#4219](https://github.com/supercollider/supercollider/pull/4219)).

IDE & SCDoc: Added
-----

IDE & SCDoc: Changed
-------

IDE & SCDoc: Deprecated
----------

IDE & SCDoc: Removed
-------

IDE & SCDoc: Fixed
-----

On macOS, Cmd+Q in the IDE would quit the interpeter but not the IDE. This is a regression from old behavior where the IDE was quit entirely. This has been fixed ([#4300](https://github.com/supercollider/supercollider/issues/4300)).

Since 3.10, the help browser would execute code twice when selected. This has been fixed ([#4390](https://github.com/supercollider/supercollider/pull/4390)).

Fix footnotes adding unwanted line breaks in SCDoc ([#4365](https://github.com/supercollider/supercollider/pull/4365)).
