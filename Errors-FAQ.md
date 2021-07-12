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