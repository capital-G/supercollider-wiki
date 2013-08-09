* subclass of NetAddr?
* protocol-specific behavior (UDP datagrams vs TCP connections)
* server control (internal vs subprocess vs remote)
* move recording to a separate class (maybe a generic ServerRecorder, that records arbitrary busses)
* move allocators to separate class?
* platform-dependent gui variables (emacsbuf, window, scopewindow) should be abstracted, moved to a separate class or put to a dictionary
* server-options should be cached when booting the server. then it can be used as reliable source to read properties of the booted server