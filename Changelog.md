This changelog documents the publicly visible changes since the most recent SuperCollider release. On release, this should be posted to the following announcement channels:

- README
- GitHub release page
- "News in 3.x" helpfile
- GitHub website
- mailing list
- Facebook group

A change is worth putting here if it affects users, such as API changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

Please provide the link to the PR with every entry in the changelog for easy navigation. These links should be retained only for the README and the GitHub release page, since they generally add unnecessary clutter to the more "social" announcement outlets.

Try to exercise common sense in keeping this log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. It's important to demonstrate that SC is actively developed, so in case of doubt, prefer inclusion over exclusion.

This all may seem nitpicky, but releases cause a lot of users to face tricky decisions like "do I upgrade SuperCollider or will it break all my compositions?" High quality changelogs not only allay FUD for users who intend to upgrade, but they also suggest high quality software and a development team that is mindful of its user base.

## General ##

Nothing here yet.

## scsynth and supernova ##

Nothing here yet.

## UGens ##

A number of UGens were discovered to have serious initialization bugs ([#2333](https://github.com/supercollider/supercollider/issues/2333)) where the UGen would output an initial sample of garbage memory. This can create audio explosions under certain conditions -- namely, the garbage memory evaluates to a large number (which is more likely to happen when the server is recording), and the buggy UGen's output is fed into certain filter UGens like LPF or Delay1. These bugs have been fixed, affecting:

- BeatTrack
- BeatTrack2
- CoinGate
- DetectSilence
- KeyTrack
- LFGauss
- PartConv
- PV_JensenAndersen
- PV_HainsworthFoote
- RunningSum
- Unpack1FFT

The `doneAction` argument to DetectSilence can now be modulated ([#2379](https://github.com/supercollider/supercollider/pull/2379)).

## sclang ##

The maximum number of MIDI ports has been increased from 16 to 128 ([2494](https://github.com/supercollider/supercollider/pull/2494)).

## Class library ##

The useRanger option in EnvirGui broke in 3.7. This has been fixed ([#2418](https://github.com/supercollider/supercollider/pull/2418)).

`Rest().isRest` and `Rest.isRest` now return true ([#2495](https://github.com/supercollider/supercollider/pull/2495)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

`Pstep` accepts an array as a duration argument ([#2511](https://github.com/supercollider/supercollider/pull/2511)).

## Help files ##

Nothing here yet.