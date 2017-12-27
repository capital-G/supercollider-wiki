## Added ##

A new "booted" stage has been added to Server objects that have been booted but may not be running yet, accessible via `Server:hasBooted` and `Server:allBootedServers` ([#3275](https://github.com/supercollider/supercollider/pull/3275)).

## Changed ##

The TOC in SCDoc has been redesigned so that it always pops out to the left ([#3346](https://github.com/supercollider/supercollider/pull/3346)).

`clientID` is now protected from being changed while the server is running ([#3275](https://github.com/supercollider/supercollider/pull/3275)).

## Deprecated ##

`Server:userSpecifiedClientID` is deprecated. Use `Server:clientID` instead ([#3275](https://github.com/supercollider/supercollider/pull/3275)).

## Fixed ##

History and HistoryGui have been cleaned up ([#3267](https://github.com/supercollider/supercollider/pull/3267)).

Fixed duplicate node IDs involving `Server.initTree` ([#3265](https://github.com/supercollider/supercollider/pull/3265)).

Fixed supernova crashing when too many controls are used ([#3196](https://github.com/supercollider/supercollider/issues/3196)).

`Volume` now respects lag time when it is instantiated or destroyed ([#3332](https://github.com/supercollider/supercollider/pull/3332)).

`Server:waitForBoot` broke in the first beta. It has been restored now ([#3276](https://github.com/supercollider/supercollider/pull/3275)).

