# UGen-Quality standards

UGens proposed for inclusion in the main SuperCollider project should meet more rigorous standards than those found "in the wild." These are standards the community has agreed upon for new UGens:

- **General software quality concerns:**
  - UGens in core should never break backward compatibility.
  - UGens should be fully documented, with a clear explanation of what it does and an appropriate collection of
    examples. Be sure to document which UGen inputs are modulatable at which rates.
  - UGens should be efficient. SuperCollider takes pride in being easy on the CPU, and UGens should help support that
    reputation.
  - The UGen should be deemed useful enough to the general SC user base.
  - Each UGen should be in a separate C++ source file (or multiple source files if it's really that long).
  - Don't leave any unnecessary print statements lying around.
- **Safety:**
  - Check input rates in the sclang class.
  - UGens should be real-time safe. Ross Bencina's ["Real-time audio programming 101"]
    (http://www.rossbencina.com/code/real-time-audio-programming-101-time-waits-for-nothing) is required reading.
    Here is a quick and incomplete blocklist of dangerous features:
    - `malloc`/`free`/`new`: use `RTAlloc` instead.
    - `throw`/`catch`: use return codes instead.
    - `dynamic_cast`
    - System calls. These are complicated to handle and require use of an NRT thread.
  - Any calls to `RTAlloc` should check the result for `NULL`. This usually happens when there
    isn't enough real-time memory left. The server will crash if this check is not made.
  - The Ctor sample should be initialized. If this is not done, very nasty bugs can occur.
  - Zap dangerous values (subnormals, infinities, nans) in feedback loops to zero. SC provides a
    `zapgremlins` function that does this for you.
- **Utility:**
  - UGens should have both `.ar` and `.kr` methods if applicable.
  - Sample rate and block size independence should be maintained if applicable. For example, audio UGens shouldn't sound
    radically different if the sample rate is increased.
  - For audio UGens, control-rate inputs should be interpolated if applicable.
  - Don't arbitrarily make certain inputs nonmodulatable just for programming convenience -- carefully anticipate what's
    worth modulating. Either way, don't forget to document it.
- **Modernization and deprecated features:**
  - When writing a new UGen from scratch, it is recommended to use the modern C++ style seen in `SC_PlugIn.hpp`.
  - Don't use `mul` and `add` arguments. These were originally introduced for efficiency, but now `Foo.ar * 2 + 1` gets
    optimized into a `MulAdd`.
  - Don't use a `doneAction` argument. Set the done flag instead.
