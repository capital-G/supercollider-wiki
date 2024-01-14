# Refactoring the server implementatin

The Server implementation (`Server.sc`) has become bloated over time [2], but has now been refactored. There are still some possible improvements, which we keep track of here.

_please feel free to edit!_

## General Remarks/Observations

- One of the main problems seems to be the handling of ids, in particular those which have some kind of special status (e.g. "persistant ones").
- in terms of efficiency and design, we have a trade off between has-a and is-a

### Ideas/Details

#### NetAddr and Server

- Iannis Zannos idea: It may be much more efficient to make server as subclass of NetAddr - in a sense it <i>is</i> just that. (But: then we cannot swap in a BundleNetAddr: s.bind / openBundle would have to be done with an if statement for every message send. This is still more efficient though. See [1]).

- Depending on protocol, behavior may be different. 
Tim suggested: for TCP one should explicitly connect/disconnect. as it is based on connections, sending/receiving without a connection just doesn't make any sense.
- This would be something to be done for NetAddr, too, probably best by passing the protocol type as a symbol.

_here is a general design decision:_
Should the different behaviours be in one class or in several? We have:

- local/internal/remote (any reason not to drop internal support?)
- delayed(bundling)/instantaneous
- connected/connectionless

And where does it belong?

- If the server _is a_ NetAddr, which should it be?
- Should a NetAddr know how to collect a bundle or is it the server's job? (I think the Addr should know it, one could simply give it a bundle instvar and add to it if it isn't nil)
- To really gain the efficiency, it would be necessary to modify the primitive ````prNetAddr_SendMsg```` (etc.) to add to the bundle if there is one.[3]

***

#### GUI

- platform dependent GUI instance variables need to be abstracted away (emacsbuf)

#### Server State

- allocators may need to go into one class, but the disadvantage is that this then needs delegation. Better keep them in the server.
- perhaps all state that is queried could go in a dictionary
- server options should be cached at boot time in order to have some information about the currently running server.
- or: server options should be queriable via OSC from the server (s.query).
- queryAllNodes shouldn't just post the info, but make it available as a string / unify with plotNodeTree ?
- the already refactored Volume is good, but quite complicated. If it is really that hard, it should be made a general technique not restricted to this class.
- bug: server calls volume.free, but Volume doesn't implement free <https://github.com/supercollider/supercollider/issues/2551>.

#### State Update

- different server control (internal, local, remote). for local servers a subprocess should be used to manage the server life.

#### Additional Functionality

- scoping should not be in server, but in a dedicated class.
- make explicit where things like record and volume nodes should be placed, and check if they can also be kept running on cmd-period.
- Possibly, it would make sense to introduce a second default group (e.g. "postprocessing group") that can contain everything that can be kept alive with no harm.

#### What a new implementation should allow for

- cleanly configure cmd-period behaviour, so that nodes may be kept alive (e.g. recording) while still being able to reset the node id allocator.
- allocators should be able to manage node recovery

## Structure

NetAddr
has a:

- NetConnection (or none)
- bundle (or none)

Server (is a NetAddr)
has a:

- ServerOptions (initial conditions)
- ServerState (updating) different classes for: local and remote (and maybe internal)
- Volume
- Recorder

ServerState could be a subclass of a general observer class that collects the status of an object by active lookup (using SkipJack). It could hold a dictionary.

## Notes

[1] Comparing the efficiency between delegation and an if statement with a simple test, it turns out that the if statement is still 50% more efficient than a delegation to a second method (as it is now), and without he if statement it is only 55 % more efficient. (this is just a basic timing benchmark). The tests are about the same for instance methods instead of class methods.

```supercollider
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
```

[2] Here is just the code that has the instance variables, to add comments about what may be handled where:

```supercollider
Server {
	classvar <>local, <>internal, <default, <>named, <>set, <>program, <>sync_s = true;

	var <name, <>addr, <clientID=0;
	var <isLocal, <inProcess, <>sendQuit, <>remoteControlled;
	var <serverRunning = false, <serverBooting = false, bootNotifyFirst = false;
	var <>options, <>latency = 0.2, <dumpMode = 0, <notify = true, <notified=false;
	var <nodeAllocator;
	var <controlBusAllocator;
	var <audioBusAllocator;
	var <bufferAllocator;
	var <scopeBufferAllocator;
	var <syncThread, <syncTasks;

	var <numUGens=0, <numSynths=0, <numGroups=0, <numSynthDefs=0;
	var <avgCPU, <peakCPU;
	var <sampleRate, <actualSampleRate;

	var alive = false, booting = false, aliveThread, <>aliveThreadPeriod = 0.7, statusWatcher;
	var <>tree;

	var <window, <>scopeWindow;
	var <emacsbuf;
	var recordBuf, <recordNode, <>recHeaderFormat="aiff", <>recSampleFormat="float";
	var <>recChannels=2;

	var <volume;

	var <pid;
	var serverInterface;

	var reallyDeadCount = 0;
```

[3] We can't make a branch in a call with a primitive:

```supercollider
// this won't compile
sendMsg { arg ... args;
	bundle !? { bundle = bundle.add(args) };
	_NetAddr_SendMsg
	^this.primitiveFailed;
}
```

So it has to be done in this method (not sure how is best):

```cpp
static int prNetAddr_SendMsg(VMGlobals *g, int numArgsPushed)
{
	PyrSlot* netAddrSlot = g->sp - numArgsPushed + 1;
	PyrSlot* args = netAddrSlot + 1;
	big_scpacket packet;

	int numargs = numArgsPushed - 1;
	int error = makeSynthMsgWithTags(&packet, args, numargs);
	if (error != errNone)
		return error;

	return netAddrSend(slotRawObject(netAddrSlot), packet.size(), (char*)packet.buf);
}
```
