The Server implementation (Server.sc) has become bloated over time.
What are the current problems?

#### NetAddr and Server:
- Iannis Zannos idea: It may be much more efficient to make server as subclass of NetAddr - in a sense it <i>is</i> just that. (But: then we cannot swap in a BundleNetAddr).
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


#### State Update
- different server control (internal, local, remote). for local servers a subprocess should be used to manage the server life.
- aliveThread should be a general object for this purpose.
- s.hasShmInterface shouldn't return false after computer was sleep (bug).

## Additional Functionality
- recording should be moved outside: allow several instances of recorders with specified paths and busses


