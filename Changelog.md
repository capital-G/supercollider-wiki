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

Instances of Rest, as well as the Rest class itself, now respond correctly to `isRest` ([#2495](https://github.com/supercollider/supercollider/pull/2495)).