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

Fixed PSinGrain growing in amplitude after it was supposed to finish ([#3494](https://github.com/supercollider/supercollider/pull/3494)).

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
