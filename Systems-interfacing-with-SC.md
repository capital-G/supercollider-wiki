There are various ways to use SC with other applications. By sending `Open Sound Control OSC` network messages to the SC Server one can control sound processes from other clients.

To send osc messages from the shell (terminal) see [sendOSC](http://cnmat.org/OpenSoundControl/clients/sendOSC.html).

## Clients Using SC Server

- Scheme
  - [rsc3](http://slavepianos.org/rd/?t=rsc3) is an [r6rs scheme](http://www.r6rs.org/) supercollider client
- Common Lisp
  - [cl-collider](https://github.com/byulparan/cl-collider) is a Common Lisp supercollider client
- Haskell
  - [hsc3](http://www.slavepianos.org/rd/?t=hsc3) is a [haskell](http://www.haskell.org) supercollider client
  - [Vivid](http://www.vivid-synth.com/) is a haskell supercollider client
  - [TidalCycles](http://tidalcycles.org/) is a pattern live coding language built on Haskell, controlling a backend written in SuperCollider
- Smalltalk
  - A squeak OSC-Client by Marcus Gälli, which works with SC:
    [OSC-Client](http://map1.squeakfoundation.org/sm/accountbyid/13fa7a75-1e76-471e-8f42-b676f4d8e373/package/61f807be-83a3-4944-bfa1-686ddac7153c)
- Perl
  - Alex McLean's article ["Hacking Perl in Nightclubs"](http://www.perl.com/pub/a/2004/08/31/livecode.html)
- Impromptu
  - SCIMP, an SC Server library for Impromptu (Scheme) [Impromptu Libraries](http://impromptu.moso.com.au/libs.html)
- Python
  - [FoxDot](https://foxdot.org/), "Live Coding with Python & SuperCollider"
  - [SC 0.3.1](https://pypi.python.org/pypi/SC/0.3.1), python client for SuperCollider
  - [Supriya](https://github.com/josiah-wolf-oberholtzer/supriya)
  - [python-supercollider](https://github.com/ideoforms/python-supercollider), a SuperCollider client for Python 3 
- Q
  - Albert Graef lets his Q functional programming language for multimedia applications talk specially to SC3 through OSC:
    http://q-lang.sourceforge.net
- Pure
  - Pure is the successor to Q: https://agraef.github.io/pure-lang/ 
  OSC is already [implemented](http://code.google.com/p/pure-lang/wiki/Addons#pure-liblo), but the SC3 interface needs to be ported from [Q](http://q-lang.sourceforge.net/addons.html) to Pure
- Java
  - JCollider duplicates some of SCLang's client side representation classes to simplify the building of Java based clients (project is beta state): http://www.sciss.de/jcollider
- Processing
  - [P5_SC](http://www.erase.net/projects/processing-sc/) is a [Processing](http://processing.org/) client for SC Synth. It replicates the main classes of SC-lang, e.g., Bus, Group, Buffer, Bus, etc
- CommonMusic
  - See documentation: http://commonmusic.sourceforge.net/cm2/doc/dict/supercollider-topic.html
- ML
  - [smlsc3](http://www.slavepianos.org/rd/?t=smlsc3) is a [Standard ML](http://standardml.org/) supercollider client
- Scala
  - Scala provides type safety, and at the same time offers compactness that makes UGen graph creation look very close to their sclang equivalents
    http://github.com/Sciss/ScalaCollider
- Clojure
  - [Overtone](https://overtone.github.io/) is a [Clojure](http://clojure.org/) based musical generation and
    manipulation system for live-coding and more.
- Lua
  - [Lua2SC](https://github.com/sonoro1234/Lua2SC) is a Lua client with ide, debugging...
- Ruby
  - [Sonic Pi](http://sonic-pi.net/) is a very popular live coding synth with SuperCollider as a server
- JavaScript / TypeScript
  - [supercollider.js](https://crucialfelix.github.io/supercolliderjs/) is a full featured client for the server and the language
- Elixir
  - [ExSCSoundServer](https://github.com/olafklingt/sc_ex_scsoundserver) Elixir libary to interact with scsynth/supernova


## Editors

- [scvim](https://github.com/supercollider/scvim) VIM plugin for SuperCollider
- [scnvim](https://github.com/davidgranstrom/scnvim) NeoVim frontend for SuperCollider
- [scel](https://github.com/supercollider/scel) Emacs interface for SuperCollider
- [Supercollider Atom](https://atom.io/packages/supercollider) Super Collider IDE for Atom
- [Sublime Text](https://github.com/geoffroymontel/supercollider-package-for-sublime-text) Supercollider package for Sublime Text 2
- [supercollider-tmbundle](http://github.com/rfwatson/supercollider-tmbundle) TextMate
- [sced](http://artfwo.googlepages.com/sced) a gedit plugin
- [scate](http://github.com/jleben/Scate) a Kate plugin
- [scfront](http://aug.ment.org/scfront) a Tcl/Tk frontend


## GUI

- [SwingOSC]() is an OpenSoundControl (OSC) server intended for scripting Java. It was written before SC had cross-platform unification of GUI, and is now no longer maintained.


## Other Systems

- [faust](http://faust.grame.fr/) a functional language for real-time audio processing, which can compile DSP expressions to C++ SuperCollider plugin code (as well as to other formats)
- [OpenObject](http://www.fredrikolofsson.com/f0blog/?q=node/401) a [quark](https://github.com/supercollider-quarks/quarks) for easily controlling synths with external applications (like Max, Pure Data, Processing, or openFrameworks) using OSC
- [OctaveSC](http://www.sonification.de/projects/sc3/index.shtml) a class to interface with the free powerful math
  package [GNU Octave](https://www.gnu.org/software/octave/) (GNU clone of MATLAB)
- [SuperColliderAU](http://doc.sccode.org/Guides/SuperColliderAU.html): AudioUnits wrapper for scsynth, now part of SuperCollider
- [javaosc](http://www.illposed.com/software/javaosc.html) a library for talking the Open Sound Control (OSC) protocol in Java
- communication from Cocoa with sc http://www.illposed.com/software/objcosc.html
- a java based system for creation of spatialisation data: http://sourceforge.net/projects/meloncillo/
- a java based sound editor using scsynth: http://www.sciss.de/eisenkraut
- open sound control library for lisp [cl-osc](http://fo.am/darcs/osc/)


## Hardware Connections

- [lemur-tutorial for supercollider](http://www.jazzmutant.com/workshop_tutorialslist.php?id=supercollider)
- Chimaera documentation: direct conection via UDP/TCP to SuperCollider server [chimaera](http://open-music-kontrollers.ch/chimaera/usage/#supercollider)