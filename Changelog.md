How to maintain this changelog
==============================

This changelog documents the publicly visible changes since the most recent SuperCollider release. A change is worth putting here if it affects users, such as breaking changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

The website [Keep a CHANGELOG](http://keepachangelog.com/en/0.3.0/) is a major inspiration for the organization of the changelog. Changes to each component of SuperCollider are subdivided into Added, Changed, Deprecated, Removed, Fixed, and Security, in that order.

Please provide the link to the PR with every entry in the changelog for easy navigation.

Try to exercise common sense in keeping this log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. In case of doubt, prefer inclusion over exclusion.

Release to-do list
------------------

Write a blurb to overview the release. Use this node.js package to generate a list of contributors, and add it to the end of the changelog: https://gist.github.com/crucialfelix/c37441a2381efbfe97fbcc8ca286f061

Post the changelog to the following announcement channels:

- README
- GitHub release page
- "News in 3.x" helpfile
- GitHub website
- sc-users mailing list
- Facebook group
- Reddit (/r/supercollider)

All links to pull requests should be removed except for the GitHub release page, README, and website.

General: Added
-----

scvim has seen numerous enhancements now that an actively maintained fork has been merged in ([scvim #11](https://github.com/supercollider/scvim/pull/11)).

SuperCollider can now be built on Windows using the MSYS2 toolchain, thanks in particular to @awson and @bagong. ([PortAudio #1](https://github.com/supercollider/portaudio/pull/1), [HIDAPI #5](https://github.com/supercollider/hidapi/pull/5), [#2473](https://github.com/supercollider/supercollider/pull/2473), [#2704](https://github.com/supercollider/supercollider/pull/2704))

SuperCollider can now be built on FreeBSD, thanks to @shamazmazum ([#2834](https://github.com/supercollider/supercollider/pull/2834), [#2704](https://github.com/supercollider/supercollider/pull/2704), [HIDAPI #8](https://github.com/supercollider/hidapi/pull/8)).

General: Changed
-------

The macOS plist file now shows the full version number for both the Version String and Shortened Version String ([#2487](https://github.com/supercollider/supercollider/pull/2487)).

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

A typo in the build system prevented the `-msse` compiler flag from being properly set for gcc and clang ([#2623](https://github.com/supercollider/supercollider/pull/2623)). This *may* fix subnormal number issues in scsynth that some users have been experiencing.

Fixed a fontification break in scel when too many classes are defined ([#2508](https://github.com/supercollider/supercollider/pull/2508)).

General: Security
--------

scsynth and supernova: Added
-----

scsynth and supernova now support a `/version` command, which responds with a message of the form `/version.reply program major minor patch branch commit` ([#2546](https://github.com/supercollider/supercollider/pull/2546), [#2598](https://github.com/supercollider/supercollider/pull/2598)). See the Server Command Reference for full details.

scsynth and supernova: Changed
-------

On macOS, if scsynth's input and output devices have mismatched sample rates, an error is thrown and the server does not boot. Setting the number of input channels to 0 (`-i 0` on the command line and `s.options.numInputBusChannels = 0` in sclang) now bypasses this error ([#2610](https://github.com/supercollider/supercollider/pull/2610)).

Disabled Nagle's algorithm for TCP communication in scsynth ([#2613](https://github.com/supercollider/supercollider/pull/2613)). Nagle's algorithm increases bandwidth at the cost of delay, which is undesirable in the context of SuperCollider. Both supernova and sclang have it turned off.

scsynth and supernova: Deprecated
----------

scsynth and supernova: Removed
------

scsynth and supernova: Fixed
-----

The `/b_read` and `/b_readChannel` messages experienced intermittent failures to read sound files, most notably affecting `Buffer.cueSoundFile`. This has been fixed ([#2793](https://github.com/supercollider/supercollider/pull/2793)).

scsynth and supernova: Security
--------

UGens: Added
-----

A new UGen, `Sanitize`, replaces infinities, NaNs, and subnormals with another signal, zero by default ([#2561](https://github.com/supercollider/supercollider/pull/2561)).

The `doneAction` argument to DetectSilence can now be modulated ([#2379](https://github.com/supercollider/supercollider/pull/2379)).

UnaryOpUGen now supports the bitwise not operator `bitNot` ([#2381](https://github.com/supercollider/supercollider/pull/2381)). It used to simply fail silently.

UGens: Changed
-------

**Breaking change:** `FOS.ar` with control-rate coefficient inputs incorrectly initialized its coefficients at 0 and ramped to the correct values over the first control period. This has been fixed ([#2658](https://github.com/supercollider/supercollider/pull/2658)). To restore old behavior, multiply each coefficient by `Line.ar(0, 1, ControlDur.ir)`.

UGens: Deprecated
----------

`Donce`, a demand-rate UGen with no identifiable purpose, is deprecated ([#2564](https://github.com/supercollider/supercollider/pull/2562)). It was most likely used in the production of electronic donce music.

UGens: Removed
-------

UGens: Fixed
-----

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

Fixed a bug with `TGrains` ignoring the `amp` parameter ([#2809](https://github.com/supercollider/supercollider/pull/2809)).

`Dibrown` no longer ignores the `length` argument ([#2654](https://github.com/supercollider/supercollider/pull/2654)).

UGens: Security
--------

sclang: Added
-----

Regression tests for the sclang lexer, parser, and compiler have been added ([#2751](https://github.com/supercollider/supercollider/pull/2751)). This will make it easier to make fixes to these components in the future.

sclang: Changed
-------

**Breaking change:** sclang's nestable multiline comments had some mistakes. In particular, sometimes sclang's lexer would incorrectly process overlapping combinations of `/*` and `*/`, so e.g. `*/*/` would be interpreted like `*/ /* */`. This has been fixed ([#2625](https://github.com/supercollider/supercollider/pull/2625)).

The maximum number of MIDI ports has been increased from 16 to 128 ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

sclang: Deprecated
----------

sclang: Removed
-------

sclang: Fixed
-----

Fixed a crash in `Object:perform` when the selector is an Array whose first element is not a Symbol, e.g. `0.perform([0])` ([#2617](https://github.com/supercollider/supercollider/pull/2617)).

`thisProcess.nowExecutingPath` is no longer corrupted by `Routine:stop` ([#2620](https://github.com/supercollider/supercollider/pull/2620)).

`TextView:selectedString_` now works when the selection size is zero ([#2648](https://github.com/supercollider/supercollider/pull/2648)).

Fixed a crash when a method or class/instance variable is named "`none`" ([#2638](https://github.com/supercollider/supercollider/pull/2638)).

Exceptions occurring in primitives no longer print unavoidable error messages even when wrapped in try-catch ([#2876](https://github.com/supercollider/supercollider/pull/2876)).

Fixed a crash when `Dictionary:keysValuesArrayDo` is called with `nil` as an argument ([#2799](https://github.com/supercollider/supercollider/pull/2799)).

sclang: Security
----------------

Class library: Added
-----

Added four new class methods to `File` for convenience: `readAllString`, `readAllSignal`, `readAllStringHTML`, `readAllStringRTF` ([#2410](https://github.com/supercollider/supercollider/pull/2410)).

`Pstep` accepts an array as a duration argument ([#2511](https://github.com/supercollider/supercollider/pull/2511)).

Help files originating from extensions now display a plaque for visibility ([#2449](https://github.com/supercollider/supercollider/pull/2449)).

For consistency with other `Platform` class methods, `Platform.recordingsDir` may be used instead of `thisProcess.platform.recordingsDir` ([#2877](https://github.com/supercollider/supercollider/pull/2877)).

`SequenceableCollection` has two new instance methods: `flatten2` and `flatBelow` ([#2527](https://github.com/supercollider/supercollider/pull/2527)). Additionally, `flatten` is faster now.

The `~callback` function is now available for all `Event` types instead of just "on" events ([#2376](https://github.com/supercollider/supercollider/pull/2376)).

New aliases for done actions, e.g. `Done.freeSelf == 2`, are introduced for better readability ([#2616](https://github.com/supercollider/supercollider/pull/2616)). See the `Done` helpfile for details.

A new class, `Recorder`, allows recording independently of the `Server` object ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

`SequenceableCollection:reduce` supports an adverb argument ([#2863](https://github.com/supercollider/supercollider/pull/2863)).

A `recordingsDir` method has been added directly to `Platform`, which transparently calls `thisProcess.platform.recordingsDir` ([#2877](https://github.com/supercollider/supercollider/pull/2877)).

`View:-resizeToBounds`, `View:-resizeToHint`, and `Window:-resizeToHint` were added to make it easier to force Views and Windows to automatically resize ([#2865](https://github.com/supercollider/supercollider/pull/2865)).

`Maybe` now supports collection methods `at`, `atAll`, `put`, `putAll`, `add`, `addAll` ([#2437](https://github.com/supercollider/supercollider/pull/2437)).

`BusPlug:-play` can now accept a `Bus` object ([#2845](https://github.com/supercollider/supercollider/pull/2845)).

Breadcrumb links in helpfiles now have separate links for each node in the hierarchy, and pages with multiple categories have separators between the categories ([#2916](https://github.com/supercollider/supercollider/pull/2916)).

`SoundFile:*openWrite` now takes additional parameters ([#2926](https://github.com/supercollider/supercollider/pull/2926)).

Two new instance methods were added to Symbol: `isBinaryOp` and `isIdentifier` ([#2955](https://github.com/supercollider/supercollider/pull/2955)).

Class library: Changed
-------

**Breaking change:** Fixed a mistake where `Pen.quadCurveTo` used the primitive for a cubic Bézier instead of quadratic ([#2553](https://github.com/supercollider/supercollider/pull/2553)). To restore the old behavior, change `Pen.quadCurveTo` to `Pen.curveTo`.

**Breaking change:** The convenience instance methods `Env:kr` and `Env:ar` had the arguments `mul` and `add` renamed to `levelScale` and `levelBias`, since they don't behave like typical `mul` and `add` arguments ([#2866](https://github.com/supercollider/supercollider/pull/2866)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

The maximum number of MIDI ports has been increased ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

Attempting to use a control-rate signal as an input to `Hasher.ar` now results in an error ([#2589](https://github.com/supercollider/supercollider/pull/2589)).

The "Cleaning up temp synthdefs..." post message is suppressed if there is nothing to clean up ([#2629](https://github.com/supercollider/supercollider/pull/2629)).

To match `Out` and `ReplaceOut`, `LocalOut` and `XOut` now correctly validate their input, checking for a non-zero number of channels ([#2659](https://github.com/supercollider/supercollider/pull/2657), [#2659](https://github.com/supercollider/supercollider/pull/2659)).

The argument to `Pattern:fin` has a default of 1 for consistency with `Object:fin` ([#2480](https://github.com/supercollider/supercollider/pull/2840/files)).

`Complex:reciprocal` is faster now ([#2890](https://github.com/supercollider/supercollider/pull/2890)).

Many minor improvements were made to the look and feel of the documentation ([#2944](https://github.com/supercollider/supercollider/pull/2944), [#2945](https://github.com/supercollider/supercollider/pull/2945), [#2947](https://github.com/supercollider/supercollider/pull/2947)).

Class library: Deprecated
----------

`Speech` is deprecated ([#2424](https://github.com/supercollider/supercollider/pull/2424)), and will be removed in 3.10. The rationale is that its audio output is independent of the server (severely limiting use in compositions), it depends on a proprietary macOS API with no prospect of cross-platform compatibility, and it is too niche to justify inclusion in the core library.

The WiiMote classes (`WiiMote`, `WiiMoteIRObject`, `WiiCalibrationInfo`, `WiiMoteGUI`, `WiiRemoteGUI`, `WiiNunchukGUI`) are deprecated ([#2698](https://github.com/supercollider/supercollider/pull/2698)). They never reached a stable state and have gone unmaintained and unused for years.

`AudioIn` is deprecated and will be removed in some future version ([#2482](https://github.com/supercollider/supercollider/pull/2482)). It was provided only for backward compatibility with SC2, so its deprecation is long overdue. Use `SoundIn` instead.

`SplayZ` has been deprecated for a long time, but it's finally on the "official" deprecation track and will be removed in 3.10 ([#2631](https://github.com/supercollider/supercollider/pull/2631)). Use `SplayAz` instead.

`TDuty_old` has been deprecated for a long time, but it now emits a warning and will be removed in 3.10 ([#2677](https://github.com/supercollider/supercollider/pull/2677)). Use `TDuty` instead.

`Watcher` is an old alias for `SkipJack` provided for backward compatibility. It is officially deprecated and will be removed in 3.10 ([#2700](https://github.com/supercollider/supercollider/pull/2700)).

`Server:recordNode` is deprecated. Use `Recorder:recordNode` instead (e.g. `s.recorder.recordNode`) ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

The `Server.set` class variable is deprecated. Use `Server.all` instead ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

Class library: Removed
-------

Removed non-functional stub methods and classes related to Image: the classes ImageFilter and ImageKernel, and the Image instance methods lockFocus, unlockFocus, applyFilters, filters, filteredWith, addFilter, removeFilter, flatten, invert, crop, applyKernel ([#2867](https://github.com/supercollider/supercollider/pull/2867)).

`Module`, an unmaintained and unused class for serialization of Synths, has been moved to a quark ([#2703](https://github.com/supercollider/supercollider/pull/2703)).

Class library: Fixed
-----

The `useRanger` option in `EnvirGui` broke in 3.7. This has been fixed ([#2418](https://github.com/supercollider/supercollider/pull/2418)).

`IdentityDictionary` methods `collect`, `select`, and `reject` retain references to the `parent` and `proto` objects ([#2507](https://github.com/supercollider/supercollider/pull/2507)).

On Linux, some MIDI methods created method override warnings. These have been silenced ([#2717](https://github.com/supercollider/supercollider/pull/2717)).

The "key" argument to `Pn` was not properly set on the first repeat. This has been fixed ([#2833](https://github.com/supercollider/supercollider/pull/2833)).

Fixed errors when using a DragSource inside a CompositeView object ([#2804](https://github.com/supercollider/supercollider/issues/2804)).

Fixed an interpreter crash when defining a SynthDef whose name is too long ([#2821](https://github.com/supercollider/supercollider/pull/2821)). More specifically, the inputs to `UnixFILE:putPascalString` and `CollStream:putPascalString` are now validated.

Server crashes are better handled by the interpreter ([#2453](https://github.com/supercollider/supercollider/pull/2453)).

The time display and the "start recording", "pause recording", and "stop recording" menu items now cooperate better with running `Server:record`, `Server:pauseRecording`, and `Server:stopRecording` ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

`Server:makeGui` and `Server:makeWindow` broke in 3.8 — the fields in the windows went blank. They are working again ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

A timing error with `NodeProxy:-clear` was fixed ([#2845](https://github.com/supercollider/supercollider/pull/2845)).

`SoundFileView` correctly displays its grid and does not draw the grid on top of the selection box ([#2872](https://github.com/supercollider/supercollider/pull/2872)).

The macOS plist file now shows the full version number for both the Version String and Shortened Version String ([#2487](https://github.com/supercollider/supercollider/pull/2487)).

Fixed instances of accidentally silencing error messages caused by neglecting to call `Object:primitiveFailed` ([#2908](https://github.com/supercollider/supercollider/pull/2908)).

Patched the possibility of inconsistent `TempoClock` state when the tempo is set via `setTempoAtSec` ([#2078](https://github.com/supercollider/supercollider/pull/2078)).

Class library: Security
--------

scide: Added
-----

Entries in the Documents docklet can be reordered, and document tabs will automatically reorder to reflect this ([#2555](https://github.com/supercollider/supercollider/pull/2555)).

"Edit > Preferences > Editor > Display" has a new option that allows replacing tabs with a dropdown whose items are alphabetically ordered ([#2555](https://github.com/supercollider/supercollider/pull/2555)). This makes navigation easier in some performance contexts.

scide: Changed
-------

Changed "occurrences" to "matches" in the status bar in the Find and Replace features ([#2702](https://github.com/supercollider/supercollider/pull/2702)).

scide: Deprecated
----------

scide: Removed
-------

scide: Fixed
-----

Some Linux systems had unreadable font colors in the autocomplete tooltips. This has been (finally) fixed ([#2672](https://github.com/supercollider/supercollider/pull/2762)).

Fixed a bug where `Document:selectedString_` had no effect ([#2849](https://github.com/supercollider/supercollider/pull/2849)).

Fixed the "Find in page..." feature in the help viewer skipping every other occurrence ([#2903](https://github.com/supercollider/supercollider/pull/2903)).

scide: Security
--------

Miscellanea
-----------

Additional and/or improved documentation is available for the following:
- Classes
  - Array
  - Char
  - CombN,L,C
  - DelayN,L,C
  - DetectSilence
  - DoubleArray
  - DynKlank
  - Float
  - FloatArray
  - Formlet
  - Hasher
  - HenonC
  - Image
  - Interpreter
  - Klank
  - LanguageConfig
  - LeakDC
  - LeastChange
  - Method
  - MIDIOut
  - MostChange
  - NetAddr
  - Object
  - Pstutter
  - Ringz
  - Schmidt
  - String
  - Symbol
- Guides
  - OSC Communication
- Overviews
  - JITLib
  - Operators
- Reference
  - Control Structures
  - Literals
  - Server Command Reference

Two old, non-functional files were removed from the repository:
- SCClassLibrary/Common/Core/Infinitum.sc
- SCClassLibrary/Common/Control/OSC.sc