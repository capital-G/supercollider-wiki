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

Fixed a build issue on OpenBSD ([#4203](https://github.com/supercollider/supercollider/pull/4203)).

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

Fixed `/b_fill`, which was broken in supernova ([#4188](https://github.com/supercollider/supercollider/pull/4188)).

Fixed incorrect latency compensation in PortAudio driver ([#4210](https://github.com/supercollider/supercollider/pull/4210)).

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

`CheckBadValues` incorrectly recognized zero as a bad value on Windows. This has been fixed ([#4240](https://github.com/supercollider/supercollider/pull/4240)).

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

Fixed `crtscts` flag in `SerialPort.new`, which broke in 3.10 ([#4191](https://github.com/supercollider/supercollider/issues/4191)).

Fixed lack of `backgroundImage` support for `Slider2D` ([#3952](https://github.com/supercollider/supercollider/pull/3952)).

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

Fixed incorrect behavior of `String:asSecs` ([#3819](https://github.com/supercollider/supercollider/pull/3819)).

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

`0X0` is an illegal hexadecimal literal in sclang, but SCIDE and SCDoc highlighted such strings as if they were correct. They have been updated ([#4170](https://github.com/supercollider/supercollider/pull/4170)).

Fixed weird colors when changing from other themes to the "classic" theme ([#4161](https://github.com/supercollider/supercollider/pull/4161)).