The Server implementation (Server.sc) has become bloated over time.
What are the current problems?

#### NetAddr and Server:
- Iannis Zannos idea: It may be much more efficient to make server as subclass of NetAddr - in a sense it <i>is</i> just that. (But: then we cannot swap in a BundleNetAddr: s.bind / openBundle would have to be done differently).
- Depending on protocol, behavior may be different. 
Tim suggested: for TCP one should explicitly connect/disconnect. as it is based on connections, sending/receiving without a connection just doesn't make any sense.
- This would be something to be done for NetAddr, too.

#### GUI
- platform dependent GUI instance variables need to be abstracted away (emacsbuf)

#### Server State
- allocators may need to go into one class
- perhaps all state that is queried could go in a dictionary
- server options should be cached at boot time in order to have some information about the currently running server.
- or: server options should be queriable via OSC from the server (s.query). 
- queryAllNodes shouldn't just post the info, but make it available as a string / unify with plotNodeTree ?
- the already refactored Volume is good, but quite complicated. If it is really that hard, it should be made a general technique not restricted to this class.

#### State Update
- different server control (internal, local, remote). for local servers a subprocess should be used to manage the server life.
- aliveThread should be a general object for this purpose.
- s.hasShmInterface shouldn't return false after computer was sleep (bug).

#### Additional Functionality
- recording should be moved outside: allow several instances of recorders with specified paths and busses
- make explicit where things like record and volume nodes should be placed, and check if they can also be kept running on cmd-period.

#### What a new implementation should allow for
- cleanly configure cmd-period behaviour, so that nodes may be kept alive (e.g. recording) while still being able to reset the node id allocator.
- allocators should be able to manage node recovery



