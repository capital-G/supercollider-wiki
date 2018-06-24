*This is a draft of a new comprehensive guide to recording in SC. Unfortunately the most important part, non-real-time recording, is currently incomplete.*

## Recording with `Server:record` ##

After making sure the server is booted, this is how you record in SuperCollider:

    Server.default.record;

That's it. To stop recording, run `Server.default.stopRecording` or hit Cmd+Period. SuperCollider outputs the recording to an AIFF file whose path is printed in the post window.

(By default, the global variable `s` refers to `Server.default`, so in all code samples in this document, you may replace `Server.default` with `s` if you're lazy: `s.record`. It's shorter, but also less robust, since the variable `s` can be reassigned. Feel free to use it when trying things out interactively, but it's not recommended in production code of any kind.)

If you're using SCIDE, it's even easier — if you open the "Language" menu on the toolbar or click on the server status bar, "Start recording" and "Stop recording" are available as menu items. The server status bar also has an "R" symbol that turns red if the server is recording.

**Warning:** The output file will be corrupted if the server quits or crashes before you call stopRecording!

### More options ###

Familiarize yourself with some of the arguments that `Server.default.record` lets you specify:

- **path** - Manually specify the output path. SuperCollider will figure out what format to write based on the extension. (As we'll cover in a later section, don't try an .mp3 path here. It won't work.)
- **bus** - Record from a specific Bus object or bus number. Defaults to 0.
- **numChannels** - Number of channels to record, defaults to the number of channels of server output.
- **node** - The Node to record after. If you're a beginner, don't worry about this.
- **duration** - If specified, the recording will be automatically stopped after this number of seconds of recording.

`s.pauseRecording` will cause SC to stop writing to the file (resume by running `Server.default.record` again). It will not write silence — it will just create skipped time in the output file. In SCIDE, this functionality is accessible on the same menu as "Start recording" and "Stop recording."

The timer for the "duration" argument waits for paused recordings. "duration" the length of the output file, not the real time spent between the beginning and end of recording.

### Exporting MP3 files ###

SuperCollider doesn't export MP3 files.

This is very easy to work around. Just export to WAV (say) and convert that WAV to MP3 using an external tool such as LAME. If that tool is accessible from the command line, you can use ```.unixCmd``` to perform conversion automatically after recording.

### `Server:record` and compositions ###

`Server:record` is very basic. It takes the real-time output of SuperCollider (or a specific Bus) and writes it to disk. It doesn't make any assumptions or interactions with your composition, other than that it produces audio output. The exact way to incorporate recording functionality into your work is up to you.

If you're designing a real-time performance interface, it's straightforward: add buttons or MIDI/OSC responders that call `Server.default.record` and `Server.default.stopRecording`. For a nicer interface, you can figure out whether the server is currently recording by calling `Server.default.isRecording` (returns a Boolean), and you can use `Server.default.recorder.duration` to determine the number of seconds elapsed in the recording.

Other users might have works that are relatively fixed-media (nondeterministic SynthDefs and generative sequencing notwithstanding). Recording your piece is simply a matter of calling `Server.default.record` and `Server.default.stopRecording` at the right times, which fits nicely into the common paradigm of using a `Routine` to sequence a composition. A nontrivial example is appropriate here, so here's short drone piece that plays a Synth for 10 seconds:
```supercollider
    (
    Routine.run {
        var s, synth, release;
        s = Server.default;

        SynthDef(\drone, {
            |out = 0, freq = 440, amp = 0.1, gate = 1, attack = 0.3, release = 0.3|
            var snd, ffreq, res;
            snd = { Gendy1.ar(1, 1, 1, 1, freq * 0.99, freq * 1.01) }!5;
            snd = Splay.ar(snd);
            ffreq = LFNoise2.kr(1).exprange(100, 3000);
            res = LFNoise2.kr(3).range(1.0, 0.3);
            snd = RLPF.ar(snd, ffreq, res);
            snd = snd * amp * Env.asr(attack, 1, release).ar(2, gate);
            Out.ar(out, snd);
        }).add;

        s.sync;

        s.record(path: "~/out.wav".standardizePath);

        release = 0.3;
        synth = Synth(\drone, [freq: 30.midicps, release: release]);
        10.wait;
        synth.set(\gate, 0);

        // Wait for the Synth to release before stopping the recording.
        release.wait;
        s.stopRecording;
    };
    )
```
In the above example, we knew exactly the amount of time before it was safe to stop recording without cutting off the audio. But with effects like reverb and echo, it may not be easy to compute when the tails end. You can just take a guess and trim trailing silence when mastering, or you can do something fancier. This example ends recording the next time all inputs are silent:
```supercollider
    (
    // This SynthDef has no output, only stereo input.
    // It frees itself the next time the input audio is silent.
    SynthDef(\freeSelfOnSilence, {
        |in = 0, threshold = (-80.dbamp), time = 0.1|
        var snd;
        snd = In.ar(in, 2);
        // This weird construction is explained in the DetectSilence help file.
        FreeSelf.kr(
            DetectSilence.ar(snd + Impulse.ar(0), threshold, time).product
        );
    }).add;
    )

    (
    var detector = Synth(\freeSelfOnSilence);
    // Watch the node, and stop recording when it frees itself.
    NodeWatcher.register(detector);
    detector.onFree({
        Server.default.stopRecording;
    });
    )
```
You can get even fancier than this and add a fade out, but we'll leave that up to you. The takeaway here is that since recording can be controlled programmatically, the possibilities are endless.

### Exporting stems ###

SuperCollider isn't specifically designed for mixing and mastering. There are mixing and mastering tools written by third parties, but many prefer to use familiar software like a traditional DAW. To accomplish this, you will want to record in multitrack.

The first step to stem export is to set up your composition so that it actually has multiple tracks in the first place. Instead of routing all your Synths to a master output, organize things into Buses, and route Buses into each other and to output. The ddwMixerChannel quark is highly recommended for this purpose, since it takes care of a lot of abstraction, providing an easy-to-use multitrack infrastructure with fading, panning, and effects groups.

[...]

### Problems with Recorder ###

Real-time recording with Recorder should be satisfactory for a lot of SuperCollider users, but it's not a perfect solution for all.

The first problem is that you can't render and record audio faster than real time. What if we wanted to stretch our drone piece out for an hour? Then we'd have to wait an hour for it to render.

The second problem is that you can't render and record audio slower than real time. If you put too much strain on the CPU, you will get buffer overruns and underruns. These can cause severe timing jitter between the server and client, which is unacceptable in many musical contexts (and also causes audible glitches and dropouts, but these happen at a lower level than SC and won't show up in the recording).

It's not only xruns that you need to worry about — sometimes sclang experiences hiccups too. These can be caused by exogenous factors, like other processes on the system hogging CPU cycles. [<= is this true?]

"Don't write music that experiences timing problems" is an ostensible workaround. But if you're not writing music intended to be performed in real time, then this becomes a stupid and arbitrary restriction.

## Non-real time recording ##

The solution to both of these problems is non-real time (NRT) mode. When scsynth/supernova runs in NRT mode, it no longer connects to audio drivers. Like an ordinary command-line program, it simply produces an output audio file. It renders audio as fast as possible, and it doesn't suffer from xruns.

Unfortunately, using NRT mode is completely different from using RT mode. It requires you to assemble an OSC score file, which is a collection of OSC messages tagged with timestamps. (Quick review for beginners: sclang communicates to scsynth over OSC. The OSC score file is equivalent to a record of all OSC messages that are sent to scsynth.)

[Go into Ctk, OSC recording]