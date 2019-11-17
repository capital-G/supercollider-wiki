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

Xcode 11 is now supported ([#4611](https://github.com/supercollider/supercollider/pull/4611)).

Minimum supported Boost version is now 1.66.0 ([#4611](https://github.com/supercollider/supercollider/pull/4611)).

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

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

supernova would sometimes return malformed `/done` OSC messages over TCP due to a concurrency issue. This has been fixed ([#4435](https://github.com/supercollider/supercollider/pull/4435)).

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

On macOS, Cmd+Q crashed the interpreter while in focus. This has been fixed ([#4533](https://github.com/supercollider/supercollider/pull/4533)).

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

Fixed a mistake where `Recorder` would get its default file extension from `server.recHeaderFormat` rather than its own `recHeaderFormat` ([#4550](https://github.com/supercollider/supercollider/pull/4550)).

The `NodeProxy` `filter` role now respects `fadeTime` ([#4278](https://github.com/supercollider/supercollider/pull/4278)).

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

On macOS, Cmd+Q used to quit both the IDE and interpreter, but it regressed and only the interpreter would quit. This has been fixed ([#4300](https://github.com/supercollider/supercollider/issues/4300)).