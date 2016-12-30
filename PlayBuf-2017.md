This page is a work in progress proposal for a new buffer player, tentatively called `XFadePlayBuf` or `PlayBufX` or `PlayBuf2`, that adds crossfading and more looping capabilities to PlayBuf. The discussion is at [#2600](https://github.com/supercollider/supercollider/issues/2600).

## Proposal ##

The schedule is to release this UGen in sc3-plugins for 3.9 and later migrate it to core for 3.10. Given its complexity, the UGen should be thoroughly covered by unit tests and the code should be documented.

The UGen's `ar` and `kr` methods shall have the following signature:

    numChannels, bufnum = 0, rate = 1, startPos = 0, startLoop = 0, endPos = -1, endLoop = -1, isLooping = 0, fadeTime = 1e-3, fadeCurve = \lin

- `numChannels`: the number of channels of the buffer provided.
- `bufnum`: the index of the buffer to play.
- `rate`: the playback rate. At `rate = 1` (default), the buffer is played back at original speed, automatically applying a `BufRateScale` translation between buffer sample rate and server sample rate, if they differ. At `rate = 0.5`, the buffer is played back at half speed, at `rate = 2.0`, the buffer is played back at double speed. At `rate = -1.0`, the playback is reversed. This can be modulated.
- `startPos`: sample frame position (inclusive) in the buffer where playback starts.
- `startLoop`: sample frame position (inclusive) in the buffer where playback resumes in loop. This can be modulated.
- `endPos`: sample frame position (exclusive) in the buffer where where playback ends. When `< 0` (default), the length of the buffer is used instead. This can be modulated.
- `endLoop`: sample frame position (exclusive) in the buffer where where looping rewinds. When `< 0` (default), the length of the buffer is used instead. This can be modulated.
- `isLooping`: a flag that indicates, when `> 0`, that the playback should loop. This can be modulated.
- `fadeTime`: a cross-fade duration in seconds. This is the actual duration of the cross-fade and independent of the playback rate. The cross-fade happens at the end of the loop span, i.e. `fadeTime` seconds before `endLoop` is reached, the previous playback begins to fade out, and a new playback starting at `startLoop` begins to fade in. When `endLoop` is reached, the previous playback has completely faded out, and the new playback has completely faded in. A value of zero indicates no cross-fade. This can be modulated. 
- `fadeCurve`: the type of curvature used for the cross-fade. This is the same as the `curve` parameter used in an `Env`. The cross-fade can be visualized as `Env([[0, 1], [1, 0]], [fadeTime, fadeTime], fadeCurve).plot`, e.g. `Env([[0, 1], [1, 0]], [1, 1], \lin).plot` for a linear (equal energy) cross-fade or `Env([[0, 1], [1, 0]], [1, 1], \welch).plot` for a square-root (equal power) cross-fade. Note that for exponential fades, where `fadeCurve = \exp`, a floor value of -60.dbamp is used instead of zero. This can be modulated.

This UGen sets the 'done' flag iff `isLooping > 0` and the read pointer reaches `endPos`.

There is no `doneAction` argument. Use `Done`, `FreeSelfWhenDone`, or `PauseSelfWhenDone`.


### Comments:

when `endPos` is given at low precision, the loop duration loses precision as you increase `startLoop`. I'd suggest `loopLength` (in frames or seconds) instead. A precise duration seems more important than a precise end, because we crossfade anyway. [@telephon]

## Why we can't use BufRd ##

BufRd has insurmountable precision issues if the buffer is longer than 16,777,216 frames because the `phase` input to BufRd is a float. It is impossible with the architecture of scsynth to upgrade this to a double.

## Why we can't add arguments to PlayBuf ##

Adding arguments to UGens is a dangerous practice in the era of alternate clients. If the server believes PlayBuf has eight arguments while the client believes it has seven, the client compiles a SynthDef that causes the server to read the eighth argument from garbage memory. Even if the API change is widely broadcast, we would need to live in a perfect world where all client developers are keeping up to date with SC development. You could argue that an outdated client is the client developer's responsibility, but PlayBuf is one of the most popular UGens ever and we should be very conservative proposing changes to it.