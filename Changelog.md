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

## sclang ##

Nothing here yet.

## Class library ##

The useRanger option in EnvirGui broke in 3.7. This has been fixed ([#2418](https://github.com/supercollider/supercollider/pull/2418)).

`Rest().isRest` and `Rest.isRest` now return true ([#2495](https://github.com/supercollider/supercollider/pull/2495)).

`Collection:processRest` returns the processed collection rather than the original ([#2497](https://github.com/supercollider/supercollider/pull/2497)).

## Help files ##

Nothing here yet.