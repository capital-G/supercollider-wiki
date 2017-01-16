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

*This section affects alternate clients.*

A typo in the build system prevented the `-msse` compiler flag from being properly set ([#2623](https://github.com/supercollider/supercollider/pull/2623)). This *may* fix subnormal number issues that some users have been experiencing.

## scsynth and supernova ##

*This section affects alternate clients.*

scsynth and supernova now support a `/version` command, which responds with a message of the form `/version.reply program major minor patch branch commit` ([#2546](https://github.com/supercollider/supercollider/pull/2546), [#2598](https://github.com/supercollider/supercollider/pull/2598)). See the Server Command Reference for full details.

On macOS, if scsynth's input and output devices have mismatched sample rates, an error is thrown and the server does not boot. Setting the number of input channels to 0 (`-i 0` on the command line and `s.options.numInputBusChannels = 0` in sclang) now bypasses this error ([#2610](https://github.com/supercollider/supercollider/pull/2610)).

## UGens ##

*This section affects alternate clients.*

A number of UGens were discovered to have serious initialization bugs ([#2333](https://github.com/supercollider/supercollider/issues/2333)) where the UGen would output an initial sample of garbage memory. This can create audio explosions if the buggy UGen's output is fed into certain filter UGens like LPF or Delay1. These bugs have been fixed, affecting:

- BeatTrack
- BeatTrack2
- CoinGate
- Convolution
- Convolution2
- Convolution2L
- Convolution3
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
- StereoConvolution2L
- Unpack1FFT

The `doneAction` argument to DetectSilence can now be modulated ([#2379](https://github.com/supercollider/supercollider/pull/2379)).

UnaryOpUGen now supports the bitwise not operator `bitNot` ([#2381](https://github.com/supercollider/supercollider/pull/2381)). It used to simply fail silently.

`Donce`, a demand-rate UGen with no identifiable purpose, is deprecated ([#2564](https://github.com/supercollider/supercollider/pull/2562)).

A new UGen, `Sanitize`, replaces infinities, NaNs, and subnormals with another signal, zero by default ([#2561](https://github.com/supercollider/supercollider/pull/2561)).

## sclang ##

**API change:** sclang's nestable multiline comments had some mistakes. In particular, sometimes sclang's lexer would incorrectly process overlapping combinations of `/*` and `*/`, so e.g. `*/*/` would be interpreted like `*/ /* */`. This has been fixed ([#2625](https://github.com/supercollider/supercollider/pull/2625)).

The maximum number of MIDI ports has been increased from 16 to 128 ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

Fixed a crash in `Object:perform` when the selector is an Array whose first element is not a Symbol, e.g. `0.perform([0])` ([#2617](https://github.com/supercollider/supercollider/pull/2617)).

`thisProcess.nowExecutingPath` is no longer corrupted by `Routine:stop` ([#2620](https://github.com/supercollider/supercollider/pull/2620)).

`TextView:selectedString_` now works when the selection size is zero ([#2648](https://github.com/supercollider/supercollider/pull/2648)).

## Class library ##

**API change:** Fixed a mistake where `Pen.quadCurveTo` used the primitive for a cubic Bézier instead of quadratic ([#2553](https://github.com/supercollider/supercollider/pull/2553)). To restore the old behavior, change `Pen.quadCurveTo` to `Pen.curveTo`.

`Speech` is deprecated ([#2424](https://github.com/supercollider/supercollider/pull/2424)), and will be removed in 3.10. The rationale is that its audio output is independent of the server (severely limiting use in compositions), it depends on a proprietary macOS API with no prospect of cross-platform compatibility, and it is too niche to justify inclusion in the core library.

`AudioIn` is deprecated and will be removed in some future version ([#2482](https://github.com/supercollider/supercollider/pull/2482)). It was provided only for backward compatibility with SC2, so its deprecation is long overdue. Use `SoundIn` instead.

`SplayZ` has been deprecated for a long time, but it's finally on the "official" deprecation track and will be removed in 3.10 ([#2631](https://github.com/supercollider/supercollider/pull/2631)). Use `SplayAz` instead.

The `Server` class underwent a refactoring ([#2422](https://github.com/supercollider/supercollider/pull/2422)), with the following effects:

- A new class, `Recorder`, allows recording independently of the `Server` object.
- `Server:recordNode` is deprecated. Use `Recorder:recordNode` instead (e.g. `s.recorder.recordNode`).
- The `Server.set` class variable is deprecated. Use `Server.all` instead.
- If the server crashes, recovery is more graceful ([#2453](https://github.com/supercollider/supercollider/pull/2453)).
- The IDE's time display and the "start recording", "pause recording", and "stop recording" menu items now cooperate better with running `Server:record`, `Server:pauseRecording`, and `Server:stopRecording`.
- `Server:makeGui` and `Server:makeWindow` broke in 3.8 — the fields in the windows went blank. They are working again.

The `useRanger` option in `EnvirGui` broke in 3.7. This has been fixed ([#2418](https://github.com/supercollider/supercollider/pull/2418)).

`Rest().isRest` and `Rest.isRest` now return true ([#2495](https://github.com/supercollider/supercollider/pull/2495)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

`Pstep` accepts an array as a duration argument ([#2511](https://github.com/supercollider/supercollider/pull/2511)).

`Function:loadToFloatArray` is now accessible to an sclang build without Qt ([#2380](https://github.com/supercollider/supercollider/pull/2380)).

Help files originating from extensions now display a plaque for visibility ([#2449](https://github.com/supercollider/supercollider/pull/2449)).

`SequenceableCollection` has two new instance methods: `flatten2` and `flatBelow` ([#2527](https://github.com/supercollider/supercollider/pull/2527)). Additionally, `flatten` is faster now.

The maximum number of MIDI ports has been increased ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

The `~callback` function is now available for all `Event` types instead of just "on" events ([#2376](https://github.com/supercollider/supercollider/pull/2376)).

`IdentityDictionary` methods `collect`, `select`, and `reject` retain references to the `parent` and `proto` objects ([#2507](https://github.com/supercollider/supercollider/pull/2507)).

Attempting to use a control-rate signal as an input to `Hasher.ar` now results in an error ([#2589](https://github.com/supercollider/supercollider/pull/2589)).

The "Cleaning up temp synthdefs..." post message is suppressed if there is nothing to clean up ([#2629](https://github.com/supercollider/supercollider/pull/2629)).

## scide ##

Entries in the Documents docklet can be reordered, and document tabs will automatically reorder to reflect this ([#2555](https://github.com/supercollider/supercollider/pull/2555)).

"Edit > Preferences > Editor > Display" has a new option that allows replacing tabs with a dropdown whose items are alphabetically ordered ([#2555](https://github.com/supercollider/supercollider/pull/2555)). This makes navigation easier in some performance contexts.

## Help files ##

Nothing here yet.