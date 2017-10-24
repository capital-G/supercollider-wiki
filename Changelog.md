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

SuperCollider can now be built on FreeBSD, thanks to @shamazmazum and @yurivict ([#2834](https://github.com/supercollider/supercollider/pull/2834), [#2704](https://github.com/supercollider/supercollider/pull/2704), [HIDAPI #8](https://github.com/supercollider/hidapi/pull/8), [#3131](https://github.com/supercollider/supercollider/pull/3131)).

Detailed documentation on creating macOS standalone applications with SuperCollider has been added, thanks to @adcxyz ([#2881](https://github.com/supercollider/supercollider/pull/2881)).

Support for multiple sclang clients connecting to the same server is greatly improved, thanks to @adcxyz.

A CODE_OF_CONDUCT.md and CONTRIBUTING.md have been added to the repository ([#3001](https://github.com/supercollider/supercollider/pull/3001)).

Higher-resolution raster versions of the SC cube logo have been added to the top-level `icons/` directory ([#3023](https://github.com/supercollider/supercollider/pull/3023)), and a retina-friendly `.icns` file ([#3060](https://github.com/supercollider/supercollider/pull/3060)).

General: Changed
-------

**Breaking change:** `sc_gcd` in the plugin interface now conforms to `gcd(n, 0) == n` instead of `gcd(n, 0) == abs(n)` ([#2980](https://github.com/supercollider/supercollider/pull/2980)). This also affects the method `SimpleNumber:gcd`.

The macOS plist file now shows the full version number for both the Version String and Shortened Version String ([#2487](https://github.com/supercollider/supercollider/pull/2487)).

General: Deprecated
----------

General: Removed
------

General: Fixed
-----

A typo in the build system prevented the `-msse` compiler flag from being properly set for gcc and clang ([#2623](https://github.com/supercollider/supercollider/pull/2623)). This *may* fix subnormal number issues in scsynth that some users have been experiencing.

Fixed a fontification break in scel when too many classes are defined ([#2508](https://github.com/supercollider/supercollider/pull/2508)).

Fixed build failures on FreeBSD ([#3126](https://github.com/supercollider/supercollider/pull/3126)), GCC 7 ([#3226](https://github.com/supercollider/supercollider/pull/3226)), and newer versions of Boost ([#3227](https://github.com/supercollider/supercollider/pull/3227)).

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

**Breaking change:** The application binary interface (ABI) for server plugins has changed ([#3129](https://github.com/supercollider/supercollider/pull/3129)). This has an important impact: **plugin binaries compiled for SuperCollider 3.8 will not work with SuperCollider 3.9** and vice versa. Please recompile your plugins.

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

`Pitch` no longer ignores the `median` argument ([#2953](https://github.com/supercollider/supercollider/pull/2953)).

Fixed a build error in DiskIOUGens on Windows ([#3015](https://github.com/supercollider/supercollider/pull/3015)).

Fixed `AudioControl` outputting garbage data if a bus is mapped to it but nothing is playing to the bus ([#3063](https://github.com/supercollider/supercollider/pull/3063)).

Fixed incorrect math in `PanAz.ar` with audio-rate input signal and position ([3139](https://github.com/supercollider/supercollider/pull/3139)).

UGens: Security
--------

sclang: Added
-----

Regression tests for the sclang lexer, parser, and compiler have been added ([#2751](https://github.com/supercollider/supercollider/pull/2751)). This will make it easier to make fixes to these components in the future.

sclang: Changed
-------

**Breaking change:** sclang's nestable multiline comments had some mistakes. In particular, sometimes sclang's lexer would incorrectly process overlapping combinations of `/*` and `*/`, so e.g. `*/*/` would be interpreted like `*/ /* */`. This has been fixed ([#2625](https://github.com/supercollider/supercollider/pull/2625)).

The maximum number of MIDI ports has been increased from 16 to 128 ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

The startup post "NumPrimitives = #" is reworded to "Found # primitives" ([#3139](https://github.com/supercollider/supercollider/pull/3139)).

sclang: Deprecated
----------

sclang: Removed
-------

Removed some unhelpful memory addresses from call stack output in error printing ([#2951](https://github.com/supercollider/supercollider/pull/2951)).

Removed some accidentally retained debug posts when the language starts up ([#3135](https://github.com/supercollider/supercollider/pull/3135)).

sclang: Fixed
-----

Fixed help files failing to open on Windows if the user's name contains a non-ASCII character ([#2861](https://github.com/supercollider/supercollider/pull/2861)).

Fixed non-ASCII characters breaking the Visual Studio debugger ([#2861](https://github.com/supercollider/supercollider/pull/2861)).

Fixed a crash in `Object:perform` when the selector is an Array whose first element is not a Symbol, e.g. `0.perform([0])` ([#2617](https://github.com/supercollider/supercollider/pull/2617)).

`thisProcess.nowExecutingPath` is no longer corrupted by `Routine:stop` ([#2620](https://github.com/supercollider/supercollider/pull/2620)).

`TextView:selectedString_` now works when the selection size is zero ([#2648](https://github.com/supercollider/supercollider/pull/2648)).

Fixed a crash when a method or class/instance variable is named "`none`" ([#2638](https://github.com/supercollider/supercollider/pull/2638)).

Exceptions occurring in primitives no longer print unavoidable error messages even when wrapped in try-catch ([#2876](https://github.com/supercollider/supercollider/pull/2876)).

Fixed a crash when `Dictionary:keysValuesArrayDo` is called with `nil` as an argument ([#2799](https://github.com/supercollider/supercollider/pull/2799)).

Fixed `WebView:onLinkActivated` handler failing to fire ([#3003](https://github.com/supercollider/supercollider/pull/3003)).

Fixed GUI objects failing to display when launched from the `action` of `unixCmd` ([#3009](https://github.com/supercollider/supercollider/pull/3009)). You will still need `{ }.defer`, however.

Fixed `QImage:getColor` always returning zero for the green channel ([#3190](https://github.com/supercollider/supercollider/pull/3190)).

sclang: Security
----------------

Class library: Added
-----

The UnitTest quark has been incorporated into the main repository ([#3168](https://github.com/supercollider/supercollider/pull/3168)).

Added a `rewind` method to `CollStream` ([#2400](https://github.com/supercollider/supercollider/pull/2400)).

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

Added three convenience methods: `View:resizeToBounds`, `View:resizeToHint`, and `Window:resizeToHint` ([#2865](https://github.com/supercollider/supercollider/pull/2865)).

Added `Collection:asEvent` for easy conversion to an `Event` ([#2871](https://github.com/supercollider/supercollider/pull/2871)).

`DeprecatedError` now shows you the file path of the deprecated method ([#3039](https://github.com/supercollider/supercollider/pull/3039)).

Added two new methods to `SimpleNumber`: `snap` and `softRound` ([#3160](https://github.com/supercollider/supercollider/pull/3160)).

`ReadableNodeIDAllocator` offers a new optional replacement for `PowerOfTwoAllocator` that assigns node IDs in a way more readable to humans when working with multiclient setups ([#3179](https://github.com/supercollider/supercollider/pull/3179)).

Class library: Changed
-------

**Breaking change:** Rests in the patterns system have been restructured ([#2802](https://github.com/supercollider/supercollider/pull/2802)). Instead of using the `isRest` event property, events are considered rests if one of their properties is a `Rest` object. You must use instances of `Rest` rather than the rest class itself -- use of `Rest` instead of `Rest()` is now deprecated.

**Breaking change:** Fixed `Dictionary:==` only comparing the values of the two dictionaries, not the keys ([#2737](https://github.com/supercollider/supercollider/issues/2737)).

**Breaking change:** Fixed a mistake where `Pen.quadCurveTo` used the primitive for a cubic Bézier instead of quadratic ([#2553](https://github.com/supercollider/supercollider/pull/2553)). To restore the old behavior, change `Pen.quadCurveTo` to `Pen.curveTo`.

**Breaking change:** The convenience instance methods `Env:kr` and `Env:ar` had the arguments `mul` and `add` renamed to `levelScale` and `levelBias`, since they don't behave like typical `mul` and `add` arguments ([#2866](https://github.com/supercollider/supercollider/pull/2866)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

The maximum number of MIDI ports has been increased ([#2494](https://github.com/supercollider/supercollider/pull/2494)).

Attempting to use a control-rate signal as an input to `Hasher.ar` now results in an error ([#2589](https://github.com/supercollider/supercollider/pull/2589)).

The "Cleaning up temp synthdefs..." post message is suppressed if there is nothing to clean up ([#2629](https://github.com/supercollider/supercollider/pull/2629)).

To match `Out` and `ReplaceOut`, `LocalOut` and `XOut` now correctly validate their input, checking for a non-zero number of channels ([#2659](https://github.com/supercollider/supercollider/pull/2657), [#2659](https://github.com/supercollider/supercollider/pull/2659)).

The argument to `Pattern:fin` has a default of 1 for consistency with `Object:fin` ([#2480](https://github.com/supercollider/supercollider/pull/2840/files)).

`Complex:reciprocal` is faster now ([#2890](https://github.com/supercollider/supercollider/pull/2890)).

`Buffer:write` takes floating point arguments, truncating them to integers ([#2547](https://github.com/supercollider/supercollider/pull/2547)).

Conversion methods among collection types has been improved and documented ([#2871](https://github.com/supercollider/supercollider/pull/2871)).

Class library: Deprecated
----------

`OSCresponder`, `OSCresponderNode`, and `OSCpathResponder` now emit deprecation messages, and will be removed after at least a year ([#2870](https://github.com/supercollider/supercollider/pull/2870)). Use `OSCFunc` or `OSCdef` instead.

`Speech` is deprecated ([#2424](https://github.com/supercollider/supercollider/pull/2424)), and will be removed in 3.10. The rationale is that its audio output is independent of the server (severely limiting use in compositions), it depends on a proprietary macOS API with no prospect of cross-platform compatibility, and it is too niche to justify inclusion in the core library.

The WiiMote classes (`WiiMote`, `WiiMoteIRObject`, `WiiCalibrationInfo`, `WiiMoteGUI`, `WiiRemoteGUI`, `WiiNunchukGUI`) are deprecated ([#2698](https://github.com/supercollider/supercollider/pull/2698)). They never reached a stable state and have gone unmaintained and unused for years.

`AudioIn` is deprecated and will be removed in some future version ([#2482](https://github.com/supercollider/supercollider/pull/2482)). It was provided only for backward compatibility with SC2, so its deprecation is long overdue. Use `SoundIn` instead.

`SplayZ` has been deprecated for a long time, but it's finally on the "official" deprecation track and will be removed in 3.10 ([#2631](https://github.com/supercollider/supercollider/pull/2631)). Use `SplayAz` instead.

`TDuty_old` has been deprecated for a long time, but it now emits a warning and will be removed in 3.10 ([#2677](https://github.com/supercollider/supercollider/pull/2677)). Use `TDuty` instead.

`Watcher` is an old alias for `SkipJack` provided for backward compatibility. It is officially deprecated and will be removed in 3.10 ([#2700](https://github.com/supercollider/supercollider/pull/2700)).

`Server:recordNode` is deprecated. Use `Recorder:recordNode` instead (e.g. `s.recorder.recordNode`) ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

The `Server.set` class variable is deprecated. Use `Server.all` instead ([#2422](https://github.com/supercollider/supercollider/pull/2422)).

`SimpleNumber:quantize` is deprecated. Use `SimpleNumber:snap` instead ([#3160](https://github.com/supercollider/supercollider/pull/3160)).

Class library: Removed
-------

Removed non-functional stub methods and classes related to Image: the classes ImageFilter and ImageKernel, and the Image instance methods lockFocus, unlockFocus, applyFilters, filters, filteredWith, addFilter, removeFilter, flatten, invert, crop, applyKernel ([#2867](https://github.com/supercollider/supercollider/pull/2867)).

`Module`, an unmaintained and unused class for serialization of Synths, has been moved to a quark ([#2703](https://github.com/supercollider/supercollider/pull/2703)).

Removed the `openHelpFile` instance methods of `Object`, `String`, `Method`, and `Quark`. These methods have been deprecated since 3.8.

Removed `String:openTextFile` and `Symbol:openTextFile`. Use `String:openDocument` and `Symbol:openTextFile` instead. These methods have been deprecated since 3.8.

Class library: Fixed
-----

A number of instance methods in `Buffer` and `Bus` did not properly check to see if the object has already been freed, and would act on buffer #0 or bus #0 (which is especially dangerous for the `free` instance method). They now safeguard against this case and throw errors ([#2936](https://github.com/supercollider/supercollider/pull/2936), [#2960](https://github.com/supercollider/supercollider/pull/2960), [#2993](https://github.com/supercollider/supercollider/pull/2993)).

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

Fixed memory spikes when using `MIDIFunc.sysex` with a large `srcID` ([#3005](https://github.com/supercollider/supercollider/pull/3005)).

Fixed spaces sometimes being rendered as `%20` in links in SCDoc ([#3033](https://github.com/supercollider/supercollider/pull/3033)).

Fixed `Function:plot` showing an empty graph if the server wasn't booted when the method was invoked ([#3047](https://github.com/supercollider/supercollider/pull/3047)).

Fixed blatant errors in `Collection:asAssociations` and `Collection:asPairs` where elements were dropped ([#3101](https://github.com/supercollider/supercollider/pull/3101)).

Fixed bugs in `NodeProxy` when using external servers ([#3103](https://github.com/supercollider/supercollider/pull/3103)).

`History` now outputs a correct timestamp on Windows ([#3045](https://github.com/supercollider/supercollider/pull/3045)).

Fixed Volume control failing to be persistent when rebooting the server ([#3125](https://github.com/supercollider/supercollider/pull/3125)).

Fixed `SimpleNumber:asTimeString` producing nonsensical results with the "precision" argument ([#3166](https://github.com/supercollider/supercollider/pull/3166)).

`Server:clientID` can now be changed, allowing multiple clients connect to the same server ([#3178](https://github.com/supercollider/supercollider/pull/3178)).

Class library: Security
--------

IDE & SCDoc: Added
-----

Entries in the Documents docklet can be reordered, and document tabs will automatically reorder to reflect this ([#2555](https://github.com/supercollider/supercollider/pull/2555)).

"Edit > Preferences > Editor > Display" has a new option that allows replacing tabs with a dropdown whose items are alphabetically ordered ([#2555](https://github.com/supercollider/supercollider/pull/2555)). This makes navigation easier in some performance contexts.

IDE & SCDoc: Changed
-------

Server actions, which were previously in the "Language" menu, have been moved out to their own "Server" menu ([#3049](https://github.com/supercollider/supercollider/pull/3049)).

Changed "occurrences" to "matches" in the status bar in the Find and Replace features ([#2702](https://github.com/supercollider/supercollider/pull/2702)).

Many minor improvements were made to the look and feel of the documentation ([#2944](https://github.com/supercollider/supercollider/pull/2944), [#2945](https://github.com/supercollider/supercollider/pull/2945), [#2947](https://github.com/supercollider/supercollider/pull/2947), [#2948](https://github.com/supercollider/supercollider/pull/2948), [#2967](https://github.com/supercollider/supercollider/pull/2967), [#3006](https://github.com/supercollider/supercollider/pull/3006), [#3022](https://github.com/supercollider/supercollider/pull/3022), [#3025](https://github.com/supercollider/supercollider/pull/3025), [#3034](https://github.com/supercollider/supercollider/pull/3034), [#3175](https://github.com/supercollider/supercollider/pull/3175)).

IDE & SCDoc: Deprecated
----------

IDE & SCDoc: Removed
-------

IDE & SCDoc: Fixed
-----

Fixed SCDoc refusing to index any further documents if one document has a malformed `copymethod::` command ([#3050](https://github.com/supercollider/supercollider/pull/3050)).

Some Linux systems had unreadable font colors in the autocomplete tooltips. This has been (finally) fixed ([#2672](https://github.com/supercollider/supercollider/pull/2762)).

Fixed a bug where `Document:selectedString_` had no effect ([#2849](https://github.com/supercollider/supercollider/pull/2849)).

New tabs are now inserted to the right of the current tab instead of all the way at the end ([#3053](https://github.com/supercollider/supercollider/pull/3053)).

The help browser now has keyboard shortcuts for navigating back and forward ([#3056](https://github.com/supercollider/supercollider/pull/3056)). These shortcuts are OS-dependent and given to us by [Qt](http://doc.qt.io/qt-5.9/qkeysequence.html#standard-shortcuts).

Fixed the "Find in page..." feature in the help viewer skipping every other occurrence ([#2903](https://github.com/supercollider/supercollider/pull/2903)).

Fixed HTML checkboxes appearing in the upper left of the help viewer ([#3028](https://github.com/supercollider/supercollider/pull/3028)).

Fixed the right-click menu for the tabs appearing in the wrong place in macOS ([#3042](https://github.com/supercollider/supercollider/issues/3042)).

IDE & SCDoc: Security
--------

Miscellanea
-----------

A packaging Python script is now compatible with both Python 2 & 3 ([#2896](https://github.com/supercollider/supercollider/pull/2896)).

Additional and/or improved documentation is available for the following:
- Classes
  - Array
  - Char
  - CombN,L,C
  - Compander
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
  - LevelIndicator
  - Method
  - MIDIOut
  - MostChange
  - NetAddr
  - Object
  - Pstutter
  - ReplaceOut
  - Ringz
  - Schmidt
  - String
  - Symbol
- Guides
  - OSC Communication
  - Internal Snooping
- Overviews
  - JITLib
  - Operators
- Reference
  - Control Structures
  - Literals
  - Server Command Reference
  - Server Architecture

Two old, non-functional files were removed from the repository:
- SCClassLibrary/Common/Core/Infinitum.sc
- SCClassLibrary/Common/Control/OSC.sc