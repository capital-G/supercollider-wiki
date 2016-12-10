## How to maintain this changelog ##

This changelog documents the publicly visible changes since the most recent SuperCollider release. A change is worth putting here if it affects users, such as API changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

Please provide the link to the PR with every entry in the changelog for easy navigation.

Try to exercise common sense in keeping this log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. In case of doubt, prefer inclusion over exclusion.

### Release to-do list ###

Write a blurb to overview the release. Use this node.js package to generate a list of contributors, and add it to the end of the changelog: https://gist.github.com/crucialfelix/c37441a2381efbfe97fbcc8ca286f061

Post the changelog to the following announcement channels:

- README
- GitHub release page
- "News in 3.x" helpfile
- GitHub website
- sc-users mailing list
- Facebook group

For the helpfile, blog post, mailing list, and Facebook group, all the links to pull requests should be removed.

## General ##

Nothing here yet.

## scsynth and supernova ##

Nothing here yet.

## UGens ##

*This section affects alternate clients.*

A number of UGens were discovered to have serious initialization bugs ([#2333](https://github.com/supercollider/supercollider/issues/2333)) where the UGen would output an initial sample of garbage memory. This can create audio explosions if the buggy UGen's output is fed into certain filter UGens like LPF or Delay1. These bugs have been fixed, affecting:

- BeatTrack
- BeatTrack2
- CoinGate
- DetectSilence
- DiskIn
- DiskOut
- IFFT
- KeyTrack
- LFGauss
- PartConv
- PV_JensenAndersen
- PV_HainsworthFoote
- RunningSum
- Unpack1FFT

The `doneAction` argument to DetectSilence can now be modulated ([#2379](https://github.com/supercollider/supercollider/pull/2379)).

UnaryOpUGen now supports the bitwise not operator `bitNot` ([#2381](https://github.com/supercollider/supercollider/pull/2381)). It used to simply fail silently.

## sclang ##

The maximum number of MIDI ports has been increased from 16 to 128 ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

## Class library ##

The `Server` class underwent a refactoring. Here are some of the resulting changes:

- There is a separate `Recorder` class that can be used independently of the server object (https://github.com/supercollider/supercollider/pull/2422).
- The "start recording", "pause recording", and "stop recording" menu items, as well as the time display in the IDE now cooperate better with running `Server:record`, `Server.pauseRecording`, and `Server:stopRecording` ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

- `Server:makeGui` and `Server:makeWindow` broken in 3.8 — the fields in the windows went blank. They are working again ([#2422](https://github.com/supercollider/supercollider/pull/2422)).
- If the server crashes, recovery is more graceful ([#2453](https://github.com/supercollider/supercollider/pull/2453)).


The `useRanger` option in `EnvirGui` broke in 3.7. This has been fixed ([#2418](https://github.com/supercollider/supercollider/pull/2418)).

`Rest().isRest` and `Rest.isRest` now return true ([#2495](https://github.com/supercollider/supercollider/pull/2495)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

`Pstep` accepts an array as a duration argument ([#2511](https://github.com/supercollider/supercollider/pull/2511)).

`Function:loadToFloatArray` is now accessible to an sclang build without Qt ([#2380](https://github.com/supercollider/supercollider/pull/2380)).

Help files originating from extensions now display a plaque for visibility ([#2449](https://github.com/supercollider/supercollider/pull/2449)).

`SequenceableCollection` has two new instance methods: `flatten2` and `flatBelow` ([#2527](https://github.com/supercollider/supercollider/pull/2527)). Additionally, `flatten` is faster now.

The maximum number of  MIDI ports has been increased ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

Event: The `~callback` function is now available for all event types ([#2376](https://github.com/supercollider/supercollider/pull/2376)).

## scide ##

Nothing here yet.

## Help files ##

Nothing here yet.