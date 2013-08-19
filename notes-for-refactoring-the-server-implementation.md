The Server implementation (Server.sc) has become bloated over time.
What are the current problems?

### General Remarks/Observations:
- One of the main problems seems to be the handling of ids, in particular those which have some kind of special status (e.g. "persistant ones").
- in terms of efficiency and design, we have a trade off between has-a and is-a

### Ideas/Details:

#### NetAddr and Server:
- Iannis Zannos idea: It may be much more efficient to make server as subclass of NetAddr - in a sense it <i>is</i> just that. (But: then we cannot swap in a BundleNetAddr: s.bind / openBundle would have to be done with an if statement for every message send. This is still more efficient though. See [1]).

- Depending on protocol, behavior may be different. 
Tim suggested: for TCP one should explicitly connect/disconnect. as it is based on connections, sending/receiving without a connection just doesn't make any sense.
- This would be something to be done for NetAddr, too, probably best by passing the protocol type as a symbol.

#### GUI
- platform dependent GUI instance variables need to be abstracted away (emacsbuf)

#### Server State
- allocators may need to go into one class, but the disadvantage is that this then needs delegation. Better keep them in the server.
- perhaps all state that is queried could go in a dictionary
- server options should be cached at boot time in order to have some information about the currently running server.
- or: server options should be queriable via OSC from the server (s.query). 
- queryAllNodes shouldn't just post the info, but make it available as a string / unify with plotNodeTree ?
- the already refactored Volume is good, but quite complicated. If it is really that hard, it should be made a general technique not restricted to this class.
- bug: server calls volume.free, but Volume doesn't implement free.

#### State Update
- different server control (internal, local, remote). for local servers a subprocess should be used to manage the server life.
- (Q: couldn't this also help for remote servers? they would remain responsive even while a larger async task is going on).
- this might solve: s.hasShmInterface shouldn't return false after computer was sleep (bug).
- aliveThread should be a general object for this purpose, or better even for general purpose.


#### Additional Functionality
- recording should be moved outside: allow several instances of recorders with specified paths and busses
- recording currently simply uses one buffer outside the range (why does this work? probably some more buffers are allocated internally by the server application?). This looks like a hack.
- make explicit where things like record and volume nodes should be placed, and check if they can also be kept running on cmd-period.
- Possibly, it would make sense to introduce a second default group (e.g. "postprocessing group") that can contain everything that can be kept alive with no harm.

#### What a new implementation should allow for
- cleanly configure cmd-period behaviour, so that nodes may be kept alive (e.g. recording) while still being able to reset the node id allocator.
- allocators should be able to manage node recovery




## Notes:
[1] Comparing the efficiency between delegation and an if statement with a simple test, it turns out that the if statement is still 50% more efficient than a delegation to a second method (as it is now), and without he if statement it is only 55 % more efficient. (this is just a basic timing benchmark).

````
Test {

	*redirect3 { |x, y, z|
		this.prRedirect3(x, y, z)
	}

	*prRedirect3 { |x, y, z|
		^x + y + z
	}

	*condition3 { |x, y, z|
		if(x.isNil) { ^x + y + z };
		^x + y + z
	}


	*redirect1 { |x|
		this.prRedirect1(x)
	}

	*prRedirect1 { |x|
		^x + 1
	}

	*condition1 { |x|
		if(x.isNil) { ^x + 1 };
		^x + 1
	}

}

/*

bench { 100.do { Test.redirect3(1, 1, 1) } };
bench { 100.do { Test.condition3(1, 1, 1) } }; // about 50 % more efficient.
bench { 100.do { Test.prRedirect3(1, 1, 1) } };

bench { 100.do { Test.redirect1(1) } };
bench { 100.do { Test.condition1(1) } }; // about 50 % more efficient.
bench { 100.do { Test.prRedirect1(1, 1, 1) } }; // about 50 % more efficient.

*/
````