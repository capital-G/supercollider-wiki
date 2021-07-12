- [ERROR: Primitive 'BasicNew' failed. Index not an Integer](https://github.com/supercollider/supercollider/wiki/Errors-FAQ#error-primitive-basicnew-failed-index-not-an-integer)
- [Language (client) issues](https://github.com/supercollider/supercollider/wiki/Errors-FAQ/_edit#language-client-issues)


# ERROR: Primitive 'BasicNew' failed. Index not an Integer

### If you're writing a SynthDef

It's quite likely that the error means you're trying to dynamically change the number of channels inside a SynthDef, which is something you can't do - SynthDefs need to have a fixed layout.  
For example, this is a simple attempt to make pink noise over a variable number of channels:

```js
(
SynthDef(\thiswillfail, { |out=0, numChannels=2|
    Out.ar(out, {PinkNoise.ar}.dup(numChannels))
}).add
)
```

It fails because we're trying to make the number of pink noise generators involved, actually changeable.  
You can't do that - when the SynthDef is compiled, the language needs to know **exactly** how many UGens will be involved and how they are connected. This is because a SynthDef represents an efficient fixed-layout synth that the server can instantiate.

### So what to do instead?

Think of SynthDefs as tiny fixed reusable components, and design your logic to reuse them in whatever combinations are needed.

To go back to the simple example above (the pink noise generator), you could simply do:

```js
(
SynthDef(\simplepink, { |out=0|
    Out.ar(out, PinkNoise.ar)
}).add
)
```

and create one `\simplepink` synth for each channel. Or you could create one SynthDef for each number of channels you expect to use.  
For example if you might use between 1 and 5 channels:

```js
(
(1..5).do{ |n|
SynthDef("simplepink_%".format(n).asSymbol, { |out=0|
    Out.ar(out, {PinkNoise.ar}.dup(n))
}).add
}
)
```

Then you'd need to invoke `\simplepink_4` or whatever, as appropriate.


# Language (client) issues

### Calling gui primitives from a SystemClock routine

When calling gui primitives from a SystemClock routine will cause an error:

```js
SystemClock.sched(0,{ Window.new.front })
```

```
ERROR: Qt: You can not use this Qt functionality in the current thread. Try scheduling on AppClock instead.
ERROR: Primitive '_QWindow_AvailableGeometry' failed.
```

To avoid this issue use the AppClock:

```js
AppClock.sched(0,{ Window.new.front })
```

or the defer method:

```js
SystemClock.sched(0,{ { Window.new.front }.defer })
```


### Binary operations order

Because of the way SuperCollider evaluates expressions, the usual order of execution of mathematical expressions is not respected.  
In SuperCollider everything is an object, and evaluation happens from left to right, so:

```js
5 + 3 * 2
```

will evaluate as (5 + 3 ) \* 2.  

This happens because the expression becomes:

```js
5.performBinaryOpOnSimpleNumber('+',3).performBinaryOpOnSimpleNumber('*',2) 
```

Therefore, in algebraic expressions parenthesis must be used when left to right orders is not what is desired:

```js
5 + (3 * 2)
```


# SynthDef Issues

### Using “If” Statements inside a SynthDef

This is covered on the page [If statements in a SynthDef](If-statements-in-a-SynthDef.html)

### `ERROR: SynthDef not found`

Sending a SynthDef to the server requires a little bit of time, which means that running a block of code with both SynthDef definitions and instances of those SynthDefs won't be guaranteed to work unless this slight delay is accounted for. There are two main ways to do this: 

First way: put the SynthDefs and the main code in a Task and put some kind of `.wait` time between them.

```js
Task({
    // put your SynthDefs here
    0.2.wait;
    // put the rest of your code here
}).play;
```

Second way: use `.sync`:

```js
Routine({
    // put your SynthDefs here
    s.sync; // assuming that 's' is the server
    // put the rest of your code here
}).play
```

### `FAILURE /s\_new alloc failed, increase server's memory allocation (e.g. via ServerOptions)`

**What it means:** While initializing the unit generators in a new Synth node, the server ran out of real-time memory.

**Solution:** Increase the amount of real-time memory available to the server. This size is set, as the error message says, in the
`ServerOptions` object associated with the server. It is a server startup option; you must quit the server and reboot it, or the new
setting will not take effect.

```js
myServer.quit;
myServer.options.memSize = 65536;  // e.g., could be different for you
myServer.boot;
```

`myServer.options.memSize` is given in KB. The default is 8192KB, or 8MB.

**What it *really* means:** Many unit generators require internal memory buffers, such as delay lines, comb filters, allpass delays, some FFT manipulators, reverb units etc.  
These internal buffers are not allocated directly from the operating system, but rather from a "real-time memory
pool."  
This is because direct allocation from the OS, by functions such as `malloc()`, is not real-time safe.  
The OS may take too long to return the new block, causing glitches in the audio.  
To solve this problem, the server allocates a chunk of memory when it starts up and parcels it out to unit generators as needed.

If you use a large number of delays, the server may run out of real-time memory. The default `8192KB` setting can support 47.55 seconds of delay at a sampling rate of 44.1 kHz.  
This goes away quickly when using lots of synths with multiple channels of delay.

**Alternate solution:** For delay units, you may use preallocated delay buffers -- `Buffer.alloc()` -- and the "Buf" delay units:  
`BufDelayN`, `BufDelayL`, `BufDelayC`, `BufCombL` etc.  
`Buffer.alloc()` does not use the real-time pool and is not subject to the memSize limitation. This approach will not help with FFT units.