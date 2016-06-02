There are various ways to use SC with other applications.
By sending [Open Sound Control OSC] network messages to the SC Server one can control
sound processes from other clients.

To send osc messages from the shell (terminal) see [sendOSC](http://archive.cnmat.berkeley.edu/OpenSoundControl/clients/sendOSC.html).

## Clients Using SC Server
* Scheme
  -  [rsc3](http://slavepianos.org/rd/?t=rsc3) is an [r6rs scheme](http://www.r6rs.org/) supercollider client.
* Haskell
  - [hsc3](http://www.slavepianos.org/rd/?t=hsc3) is a [haskell](http://www.haskell.org) supercollider client.
  - [Vivid](http://www.vivid-synth.com/) is a haskell supercollider client.
  - [Tidal](http://tidalcycles.org/) is a pattern live coding language built on Haskell, frequently paired with SC as the audio backend.
* SmallTalk
  - A squeak OSC-Client by Marcus Gälli, which works with SC: [http://map1.squeakfoundation.org/sm/accountbyid/13fa7a75-1e76-471e-8f42-b676f4d8e373/package/61f807be-83a3-4944-bfa1-686ddac7153c OSC-Client]
* Perl
  - Alex McLean's article [http://www.perl.com/pub/a/2004/08/31/livecode.html "Hacking Perl in Nightclubs"]
* Impromptu
  - SCIMP, an SC Server library for Impromptu (Scheme) [Impromptu Libraries](http://impromptu.moso.com.au/libs.html)
* Python
  - scosc, python OSC for supercollider: [http://www.patrickkidd.com/ http://www.patrickkidd.com/]
  - SC 0.2, python client for SuperCollider [http://pypi.python.org/pypi/SC/0.2 http://pypi.python.org/pypi/SC/0.2]
  - Installation of PySCLang (sclang for python): [here](http://jonathansaggau.com/sc/sclangEmacsPySCLang.rtf) is a quick installation tutorial by Johnathan Saggau
  - [Supriya](https://github.com/josiah-wolf-oberholtzer/supriya)
* Q
  - Albert Graef lets his Q functional programming language for multimedia applications talk specially to SC3 through OSC: http://q-lang.sourceforge.net/
* Pure
  - Pure is the successor to Q: http://pure-lang.googlecode.com/
  - OSC is already [http://code.google.com/p/pure-lang/wiki/Addons#pure-liblo implemented], but the SC3 interface needs to be ported from [Q](http://q-lang.sourceforge.net/addons.html) to Pure
* Java
  - As much as Mühlethaler and Schuppisser with their Sonificator do this with java: http://www.substring.ch/sound/
  - scream, a system based on java: http://audio.egregious.net/scream/
  - JCollider duplicates some of SCLang's client side representation classes to simplify the building of Java based clients (project is beta state): http://www.sciss.de/jcollider
* Processing
  - [http://www.erase.net/projects/p5_sc/ P5_SC] is a [Processing](http://processing.org/) client for SC Synth. It replicates the main classes of SC-lang, e.g., Bus, Group, Buffer, Bus, etc.
* CommonMusic
  - Rick Taube's algorithmic library for LISP. [Page at sourceforge](http://commonmusic.sourceforge.net/doc/cm.html)
* ML
  - [smlsc3](http://www.slavepianos.org/rd/?t=smlsc3) is a [Standard ML](http://standardml.org/) supercollider client.
* Scala
  - Scala provides type safety, and at the same time offers compactness that makes UGen graph creation look very close to their sclang equivalents. http://github.com/Sciss/ScalaCollider
* Clojure
  - [Overtone](http://github.com/overtone/overtone) is a [Clojure](http://clojure.org/) based musical generation and manipulation system for live-coding and more.
* JavaScript
  - https://github.com/crucialfelix/supercolliderjs tools for working with scsynth and sclang. OSC messaging, process management, sclang interpreter. NodeJS and includes a websocket bridge for web browsers.
* Ruby
  - [Sonic Pi](http://sonic-pi.net/) is a very popular live coding synth with SuperCollider as a server.

## Editors
* [scvim](http://www.x37v.info/scvim/) vim scripts for supercollider
* Emacs - sc.el is included with the standard SuperCollider distribution
* [Supercollider Atom](https://atom.io/packages/supercollider) Super Collider IDE for Atom
* [sced](http://artfwo.googlepages.com/sced) a gedit plugin
* [scate](http://github.com/jleben/Scate) a Kate plugin
* [scfront](http://aug.ment.org/scfront) a Tcl/Tk frontend
* [supercollider-tmbundle](http://github.com/rfwatson/supercollider-tmbundle/tree/master supercollider-tmbundle) Rob Watson's TextMate bundle

## GUI
* [SwingOSC](https://github.com/Sciss/SwingOSC) is an OpenSoundControl (OSC) server intended for scripting Java. SwingOSC was useful back before SC's built-in GUI was cross-platform, but now it is obsolete and no longer maintained.
* [SCVamp](http://the3rd2nd.com/SCVamp/) improvisation with multiple SuperCollider synths and patterns through a graphical user interface.
* SCUM is an OpenSoundControl (OSC) GUI server based on FLTK.

## Other Systems
* [faust](http://faust.grame.fr/) a functional language for real-time audio processing, which can compile DSP expressions to C++ SuperCollider plugin code (as well as to other formats).
* [OpenObject](http://www.fredrikolofsson.com/f0blog/?q=node/401) a [quark](http://quarks.sourceforge.net/) for easily controlling synths with external applications (like Max, Pure Data, Processing, or openFrameworks) using OSC
* [OctaveSC](http://www.sonification.de/projects/sc3/index.shtml) a class to interface with the free powerful math package [GNU Octave](http://www.octave.org/) (GNU clone of MATLAB).
* [vst2osc](http://www.realizedsound.net/downloads): sending osc messages from any VST-compatible application
* [SuperColliderAU](http://supercolliderau.sourceforge.net/):  AudioUnits wrapper for scsynth, now part of SC.
* [javaosc](http://www.illposed.com/software/javaosc.html) a library for talking the Open Sound Control (OSC) protocol in Java.
* communication  from Cocoa with sc http://www.mat.ucsb.edu/~c.ramakr/illposed/objcosc.html
* a java based system for creation of spatialisation data: http://sourceforge.net/projects/meloncillo/
* a java based sound editor using scsynth: http://www.sciss.de/eisenkraut
* a soundfile segmentor that comes with supercollider classes: [Meapsoft](http://labrosa.ee.columbia.edu/meapsoft/docs.php)
* open sound control library for lisp [http://fo.am/darcs/osc/ cl-osc]

## Hardware Connections
* [lemur-tutorial for supercollider](http://www.jazzmutant.com/workshop_softrelatedissueslist.php?id=supercollider)
* iPod Touch and iPhone OSC clients: http://poly.share.dj/projects/#mrmr open source, multi-user, server configured
* [oscemote](http://lux.vu/blog/oscemote/) auto-connect, UI customizable via html/css
