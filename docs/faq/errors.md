# Errors

## ERROR: Primitive 'BasicNew' failed. Index not an Integer

### If you're writing a SynthDef

It's quite likely that the error means you're trying to dynamically change the number of channels inside a SynthDef, which is something you can't do - SynthDefs need to have a fixed layout.  
For example, this is a simple attempt to make pink noise over a variable number of channels:

```supercollider
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

```supercollider
(
SynthDef(\simplepink, { |out=0|
    Out.ar(out, PinkNoise.ar)
}).add
)
```

and create one `\simplepink` synth for each channel. Or you could create one SynthDef for each number of channels you expect to use.  
For example if you might use between 1 and 5 channels:

```supercollider
(
(1..5).do{ |n|
SynthDef("simplepink_%".format(n).asSymbol, { |out=0|
    Out.ar(out, {PinkNoise.ar}.dup(n))
}).add
}
)
```

Then you'd need to invoke `\simplepink_4` or whatever, as appropriate.

## Language (client) issues

### Calling gui primitives from a SystemClock routine

When calling gui primitives from a SystemClock routine will cause an error:

```supercollider
SystemClock.sched(0,{ Window.new.front })
```

```
ERROR: Qt: You can not use this Qt functionality in the current thread. Try scheduling on AppClock instead.
ERROR: Primitive '_QWindow_AvailableGeometry' failed.
```

To avoid this issue use the AppClock:

```supercollider
AppClock.sched(0,{ Window.new.front })
```

or the defer method:

```supercollider
SystemClock.sched(0,{ { Window.new.front }.defer })
```

### Binary operations order

Because of the way SuperCollider evaluates expressions, the usual order of execution of mathematical expressions is not respected.  
In SuperCollider everything is an object, and evaluation happens from left to right, so:

```supercollider
5 + 3 * 2
```

will evaluate as (5 + 3 ) \* 2.  

This happens because the expression becomes:

```supercollider
5.performBinaryOpOnSimpleNumber('+',3).performBinaryOpOnSimpleNumber('*',2) 
```

Therefore, in algebraic expressions parenthesis must be used when left to right orders is not what is desired:

```supercollider
5 + (3 * 2)
```

## SynthDef Issues

### "If" statements inside a SynthDef

It's only a matter of time before a user tries to write something like this in a `SynthDef`:

```supercollider
SynthDef(\kablooie, { |x = 0|
    var signal;
    if(x > 0) {
        signal = SinOsc.ar
    } {
        signal = Saw.ar
    };
});
```

... with the disturbing result: `ERROR: Non Boolean in test.`

"Non Boolean in test"? But *x \> 0* is a comparison, and surely should produce a Boolean, right?

This should be the first clue that Boolean logic in the server is a very different animal from the so-called "normal" use of conditionals on the client side (in the language).

### What is a Boolean in the server?

In fact, there is no such thing. The server handles floating-point numbers. It doesn't have *true* or *false* entities.

Since everything in the server is a number, the result of the comparison must also be a number. The server follows the same convention as other DSP environments (Max/MSP, pd etc.):

- `True` is represented by 1.0
- `False` is represented by 0.0

### Why is `x \> 0` "non-Boolean" in the "test"?

This goes back to the general issue of handling operators in the server.  
Math operators in a SynthDef are not calculations to do *right now*.  
They *describe* calculations that will be done *in the future*, many thousands of times.

```supercollider
var x = 1;
x > 0;
// -> true
```

```supercollider
SynthDef(\kablooie, { |x = 0|
    "x: ".post; x.postln;
    "(x > 0): ".post; (x > 0).postln;
});
```

```supercollider
x: an OutputProxy
(x > 0): a BinaryOpUGen
```

The precise value of *x* is unknown at the time you execute the SynthDef code.  
*x* actually represents an unlimited number of values, which will be provided to Synths using argument lists. So, it's meaningless to
determine, once and for all, whether *x \> 0* or not. *x* may be *\> 0* now and *\< 1* a split second later. So, instead of producing a Boolean, *x \> 0* produces a **Binary Operator UGen** that repeatedly executes the comparison.

Going back to this:

```supercollider
if (aBinaryOpUGen) { ... } { ... };
```

To do this, the language must know which function (true or false) to execute. But there is no way to know which one the BinaryOpUGen will be.  
So, SuperCollider throws an error.

### If you can't branch, what good is a comparison in the server?

Comparisons have a lot of uses, actually.

- **Choosing one of two signals:** This is the closest we can get to *if-then-else* in the server. Both *then* and *else* must be running continuously. That's a requirement of how the server works: the number and arrangement of unit generators within a single Synth cannot change. Instead, you can choose *which of those signals makes it downstream*. One will be used and the other ignored.  
Since true is 1 and false is 0, you can use a conditional to index into an array using Select.

```supercollider
Select.kr(aKrSignal > anotherKrSignal, [false_signal, true_signal]);
```

- **Generating triggers:** A trigger occurs whenever a signal is \<= 0, and then becomes \> 0. Extending this to comparisons, it means that *a trigger occurs when a comparison is false for a while, and then becomes true*. Comparing a signal to a threshold may then be used anywhere that a trigger is valid.  
For a simple example, take the case of sending a message to the language when the microphone input's amplitude crosses a threshold.

```supercollider
var mic = In.ar(8, 1), amplitude = Amplitude.kr(mic);
SendTrig.kr(amplitude > 0.2, 0, amplitude);
```

- **Passing or suppressing triggers:** You might need to generate triggers continuously, but permit the triggers to take effect only when a condition is met. Multiplication handles this nicely:  
*condition \* trigger*. Since the condition evaluates as 0 when false, the trigger will be replaced by 0 and nothing happens, as desired.  

For a simple case, let's refine the mic amplitude example by suppressing triggers that occur within 1/4 second after the previous.

```supercollider
var mic = In.ar(8, 1),
    amplitude = Amplitude.kr(mic),
    trig = amplitude > 0.2,
    timer = Timer.kr(trig), // how long since the last trigger?
    filteredTrig = (timer > 0.25) * trig;

SendTrig.kr(filteredTrig, 0, amplitude);
```

### Logical operators: And, Or, Not, Xor

Logical operators have simple arithmetic equivalents.

- **And = multiplication:** *(x \> 0) \* (y \> 0)* means both conditions must be true (nonzero) for the result to be nonzero.  

- **Or = addition:** *(x \> 0) + (y \> 0)* means nonzero in either condition is enough to make the result nonzero.  
  
NOTE: If both are true, then the result will be 2, not 1. In some cases, the 2 may not be acceptable. That can be fixed by wrapping the Or in another comparison -- *((x \> 0) + (y \> 0)) \> 0* -- because 2 \> 0 evaluates to 1!

- **Not:** I prefer to negate a condition by comparing it to zero:  
*condition \<= 0*. 0 \<= 0 is 1 (i.e., not 0), and 1 \<= 0 is 0 (not 1).  
If you're certain the logical expression will only ever be 0 or 1 exactly, you can also negate by subtraction: *1 - condition*.

- **Xor:** Exclusive-or is true if one or the other condition is true, but not both. We can add the two conditions and compare it to 1. The syntax is a little bit tricky because `==` doesn't turn into a BinaryOpUGen automatically.  
We have to create the BinaryOpUGen by hand.

```supercollider
BinaryOpUGen('==', (x > 0) + (y > 0), 1)
```

### `ERROR: SynthDef not found`

Sending a SynthDef to the server requires a little bit of time, which means that running a block of code with both SynthDef definitions and instances of those SynthDefs won't be guaranteed to work unless this slight delay is accounted for. There are two main ways to do this: 

First way: put the SynthDefs and the main code in a Task and put some kind of `.wait` time between them.

```supercollider
Task({
    // put your SynthDefs here
    0.2.wait;
    // put the rest of your code here
}).play;
```

Second way: use `.sync`:

```supercollider
Routine({
    // put your SynthDefs here
    s.sync; // assuming that 's' is the server
    // put the rest of your code here
}).play
```

### `FAILURE /s_new alloc failed, increase server's memory allocation`

**What it means:** While initializing the unit generators in a new Synth node, the server ran out of real-time memory.

**Solution:** Increase the amount of real-time memory available to the server. This size is set, as the error message says, in the
`ServerOptions` object associated with the server. It is a server startup option; you must quit the server and reboot it, or the new
setting will not take effect.

```supercollider
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

### Array arguments

Sometimes, you need to send an array to a series of Control inputs in a SynthDef (often called "_array arguments_").

```supercollider
Synth(\xyz, [freqs: [300, 400, 500]]);
```

There are two primary ways to do this:

- Supply a literal array -- `\#[1, 2, 3]` -- as the default for the argument name in the function.  
This is discussed in [SynthDef's help file](https://doc.sccode.org/Classes/SynthDef.html).

```text
SynthDef(\xyz, { |freqs = #[1, 2, 3]|
    // ...
})
```

- Or, use `NamedControl`.  
This is the only way to do it if you want to construct the array's size dynamically, or based on a variable. See [NamedControl help](https://doc.sccode.org/Classes/NamedControl.html).

```text
SynthDef(\xyz, {
    var freqs = NamedControl.kr(\freqs, #[1, 2, 3]);
    // ...
});
```

### Why does it have to be a literal array?

The reason comes from the process of building a SynthDef:

1. First, look at the function arguments to figure out what the Control inputs should be.
2. Then create Control units (usually just one, if they're all normal arguments without prefixes or special rates). Each channel is represented by an `OutputProxy`.
3. Then run the SynthDef function, passing the output proxies to the arguments.
4. Then sort the UGens into the right order, etc. etc.

To do steps \#1 and \#2, the SynthDef builder has to know the size of an array argument *before* running the function. That's possible only if it's a literal array: `\#[1, 2, 3, 4, 5]`. Any other array notation creates the array *while running the function* (step \#3). But then it's too late -- the SynthDef builder already created a non-array control channel for it!

```supercollider
SynthDef(\notArray, { |a = (1..5)|
    a.debug("a is");
});
```

`a is: an OutputProxy`

```text
SynthDef(\array, { |a = #[1, 2, 3, 4, 5]|
   a.debug("a is");
});
```

`a is: [ an OutputProxy, an OutputProxy, an OutputProxy, an OutputProxy, an OutputProxy ]`

(Note, if 'a' printed as [ 1, 2, 3, 4, 5 ], then you wouldn't be able to change the values in a Synth using .set!)

## Server issues

### How to trigger a function from the server

The first and most important point: **Functions are client-side only.**  
The server doesn't know what functions are, doesn't understand them and has no way to execute them.  
**Only the client can execute a function.**

Therefore, if you want a function to execute when something happens in the server, the only way is for the server to tell the client to take the action.

The server can communicate messages back to the client using one of two unit generators: `SendTrig` and `SendReply`.  
`SendTrig` is simpler and less flexible (it can send only a `/tr` message, and only one data value).  
`SendReply` allows you to name the message anything you like, and can send arrays with the message.  
We'll use SendReply here because of its greater flexibility.

Within the language, you also need an object to receive the message and act on it. Usually this is `OSCresponderNode` or `OSCpathResponder`.  In this example, `OSCpathResponder` filters messages not just on the name `/bleep` but also on the synth's ID. This way, you could have multiple triggering synths, with a different responder and a different action per synth.

```supercollider
(
a = {
    var trig = Dust.kr(8),
    decay = Decay2.kr(trig, 0.01, 0.1),
    sig = SinOsc.ar(TExpRand.kr(200, 600, trig), 0, 0.1) * decay;
    SendReply.kr(trig, '/bleep', trig);
    sig ! 2
}.play;

o = OSCpathResponder(s.addr, ['/bleep', a.nodeID], { |time, thisResponder, msg|
    msg.postln;
}).add;
)

a.free; o.remove;
```

#### Helpfile references

- [`SendTrig`](https://doc.sccode.org/Classes/SendTrig.html), [`SendReply`](https://doc.sccode.org/Classes/SendReply.html)
- [`OSCresponderNode`](https://doc.sccode.org/Classes/OSCresponderNode.html), [`OSCpathResponder`](https://doc.sccode.org/Classes/OSCpathResponder.html), [`OSCresponder`](https://doc.sccode.org/Classes/OSCresponder.html), [OSC communication](https://doc.sccode.org/Guides/OSC_communication.html)

### Exception in World_OpenUDP: unable to bind udp socket

Sometime when booting the server one gets a message: ` Exception in World_OpenUDP: unable to bind udp socket `.

This is usually caused by an instance of scsynth that as hanged but has not released the osc port, perhaps because it SuperCollider crashed.  To fix this, just hit the *"k"* button in the server window to kill all scsynth processes, and then boot again.

## Other issues

### Error while loading shared libraries: libsclang.so: cannot open shared object file

This usually happens after building on Linux and it means that your system is unaware of newly installed shared libraries. Running ldconfig
(as root) solves the problem:

`# /sbin/ldconfig`
