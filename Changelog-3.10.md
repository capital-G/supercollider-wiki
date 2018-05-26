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

scel (the emacs package) is now a submodule ([#3519](https://github.com/supercollider/supercollider/pull/3519)).

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

Fixed a build failure with the CMake option `SYSTEM_YAMLCPP=on` ([#3558](https://github.com/supercollider/supercollider/pull/3558)).

Fixed a misleading deprecation warning when `CMAKE_INSTALL_PREFIX` is set to the home directory in Linux ([#3613](https://github.com/supercollider/supercollider/pull/3613)).

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

sclang: Added
-----

`FileDialog` and `Dialog` now support a "path" argument that specifies a default directory when the dialog appears ([#3508](https://github.com/supercollider/supercollider/pull/3508)).

`QTreeView` has a new method: `setColumnWidth` ([#3560](https://github.com/supercollider/supercollider/pull/3560)).

sclang: Changed
-------

Printing a float that is equal to an integer will always produce a decimal point -- for example, a floating point value of 3 is printed as 3.0 ([#3585](https://github.com/supercollider/supercollider/pull/3585)).

sclang: Deprecated
----------

sclang: Removed
-------

Removed some unused Qt dependencies from the build system ([#3472](https://github.com/supercollider/supercollider/pull/3472)).

sclang: Fixed
-----

Class library: Added
-----

Class library: Changed
-------

Internal calls to `.interpret` have been removed from `Color.fromHexString` and `History.unformatTime`, improving both performance and security ([#3527](https://github.com/supercollider/supercollider/pull/3527)).

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
