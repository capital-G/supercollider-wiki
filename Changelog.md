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

Introduced Guard integration that allows sclang UnitTests to be automatically rerun whenever a file changes ([#3369](https://github.com/supercollider/supercollider/pull/3369)).

Bleeding-edge builds are now uploaded for Windows. See the Windows README for details ([#3441](https://github.com/supercollider/supercollider/pull/3441)).

General: Changed
-------

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

Debugging information is improved when building a Windows installer package ([#3464](https://github.com/supercollider/supercollider/pull/3464)).

scsynth and supernova: Added
-----

scsynth and supernova: Changed
-------

scsynth and supernova: Deprecated
----------

scsynth and supernova: Removed
------

scsynth and supernova: Fixed
-----

supernova only looked for plugins in a `plugins/` subfolder of the provided extensions directory. This has been fixed to be consistent with scsynth. ([#3433](https://github.com/supercollider/supercollider/pull/3433)).

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

Fixed `Index`, `IndexL`, `FoldIndex`, `WrapIndex`, `IndexInBetween`, and `DetectIndex` incorrectly handling audio-rate index arguments ([#3436](https://github.com/supercollider/supercollider/pull/3436)).

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

The GUI class library folders were installed even when building sclang without Qt, resulting in unbound primitives. This has been fixed ([#3456](https://github.com/supercollider/supercollider/pull/3456)).

Some default class library directories had to be manually created. sclang will now create them for you if they don't exist ([#3469](https://github.com/supercollider/supercollider/pull/3469)).

Class library: Added
-----

Class library: Changed
-------

Class library: Deprecated
----------

Class library: Removed
-------

Class library: Fixed
-----

Fixed a Routine not being properly terminated when running `CmdPeriod.run` (or hitting an equivalent shortcut) when a `Server:plotTree` window is open ([#3423](https://github.com/supercollider/supercollider/pull/3423)).

Fixed `LevelIndicator:style_` doing nothing and printing the warning `Qt: WARNING: Do not know how to use an instance of class 'Meta_QLevelIndicatorStyle'` ([#3398](https://github.com/supercollider/supercollider/pull/3398)).

Fixed `Git.checkForGit` returning `nil` ([#3445](https://github.com/supercollider/supercollider/issues/3445)).

The SynthDef compiler optimizes `a + b.neg` to `a - b`, but other UGens that depend on `b.neg` would also be incorrectly removed in some cases. This has been fixed ([#3437](https://github.com/supercollider/supercollider/pull/3437)).

In 3.9.0, the `group` key broke in the "grain" event type. This has been fixed ([#3483](https://github.com/supercollider/supercollider/pull/3483)).

IDE & SCDoc: Added
-----

New IDE themes have been introduced for the editor and post window: Solarized, Solarized Dark, and Dracula ([#3412](https://github.com/supercollider/supercollider/pull/3412), [#3410](https://github.com/supercollider/supercollider/pull/3410)).

IDE & SCDoc: Changed
-------

Set the default font in the IDE for macOS to Monaco, instead of the rather silly non-monospace font that has been the SC default for over a decade ([#3404](https://github.com/supercollider/supercollider/pull/3404)).

IDE & SCDoc: Deprecated
----------

IDE & SCDoc: Removed
-------

IDE & SCDoc: Fixed
-----

Fixed duplicate SCIDE icons in GNOME, and fixed the SCIDE icon looking wrong ([#3380](https://github.com/supercollider/supercollider/pull/3380)).

Fixed SCDoc breaking with page titles containing a single quote character ([#3301](https://github.com/supercollider/supercollider/pull/3301)).

Fixed an error due to lack of input sanitization when trying to open help (Cmd+D/Ctrl+D) or references (Cmd+U/Ctrl+U) on text containing a double quote character ([#3277](https://github.com/supercollider/supercollider/pull/3277)).