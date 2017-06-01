2017-05-27
==========

5 people were present: Brian, Alberto, Nathan, Julian, and Patrick.

- Brian Heim has been working on his big UTF-8 pull request which fixes
the Windows help file issue.
- Alberto de Campo has a topic branch for multiclients to improve node
and buffer allocation, and has a PR for OSX standalones.
- Nathan Ho has been working on UGen regression tests, and small help
files and class library issues.
- Julian Rohrhuber worked on File.read* methods, Rest/Operand reform,
and a quark for a Neutral object that records every message sent to it.
- Patrick Dupuis has been investigating the Ubuntu keyboard shortcut
issue and has been working on help file, class library, and
Linux-related issues.

Topics:

- Old standalone instructions are gone.
- A PR can be merged when it presents an improvement and doesn't
introduce new bugs.
- 3.9.x releases and eventual adoption of git-flow
- SCDoc, barriers for new helpfile contributors, features we can add to
the help files to make it easier to contribute
- Number of PRs open, speed of merge, filing PRs with incomplete work

2017-04-22
==========

- Nathan did nothing
- Brian worked on the Windows help file issue and include/exclude paths
for scsynth

Topics:

- Merged/closed some small PRs
- CONTRIBUTING.md, and issue and PR templates 

2017-04-01
==========

- Nathan did nothing
- Brian updated yaml-cpp, filed a PR to fix the .putPascalString crash,
and has done some work on the Windows help file bug

Topics:

- Release mode for 3.9 in about two weeks?
- sclang header refactoring
- WebView:onLinkActivated
- LPC regression tests 

2017-03-11
==========

- Brian Heim and Nathan Ho worked on sclang LPC tests
- Nathan Ho also made (marginal) progress on UGen regression tests
- Patrick Dupuis investigated openbuildservice.org and HID on Fedora

Topics:

- Plan for merging LPC test suite: get it to run, see if it catches
changes to sclang, quick review, merge
- openbuildservice.org, while good, is not a useful service for the SC
dev team since it creates a PPA/third party repository.
- Performance on MacBook Pro 2016
- Brian is pushing the Boost updates because it works towards fixing the
Windows helpfile problem
- Find people and get support for the SC_SCLANG flag:
https://github.com/supercollider/supercollider/pull/1939
- Mixed feelings on single quotes in variable names:
https://github.com/supercollider/supercollider/issues/2773
- Backing up SC:
https://github.com/supercollider/supercollider/issues/2776
- Rational numbers implementation: put off until 3.10?
- Push release date back to May 1
- sclang verbosity proposal is not a requirement for 3.9, but it's
important
- Brian and I share an opinion on the state of SC development right now:
we're overloaded with work, and the lists of issues and PRs often feel
like a huge wall of noise. We've been cutting down on multitasking and
trying to focus on what's important, and have felt increasingly
nonchalant about proposals for new features. 

2017-03-04
==========

What we did:

- Tom Murphy did nothing.
- Brian Heim has been working on regression tests for sclang, which
should be ready to merge within a few days. He has a working proof of
concept using the recent nested multiline comment fix.
- Rainer Schütz is working on making SC buildable on VS 2015. The
difficult parts are QtWebKit and supernova.
- Nathan Ho worked on a bunch of small things as usual, FINALLY fixed
the Linux tooltip issue with Rainer, and has made some progress on UGen
regression tests.
- Patrick Dupuis is looking into HID issues on Fedora Linux (the help
file contains an Ubuntu-specific udev rule).

Topics:

- appear.in supports stickers, as we discovered this meeting
- Cross-platform compatibility of the older Python sclang tests.
- April 1 was a bit optimistic for 3.9 (we only have 2 out of 8 major
issues outlined in January), but we can still try to push to finish some
important issues.
- Issues with packaging. Looked at openbuildservice.org and discussed
Travis CI, AWS, and Linux PPAs. We don't really have a documented
release process right now.
- Our thoughts on the recent mailing list discussion:
   - It's okay if we use a mailing list even if they're out of vogue
   - It's *not* okay that people are sending messages to the list through
Nabble and we can't do anything about their messages ending up in limbo
   - We should replace Nabble, not the list
- Concerns over scvim development rate
- Unanimous support for deprecating OSC(path/r)esponder[Node]
- Missing sclang features: .asStringPrec with trailing zeros (see
http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/asStringPrec-td5826156.html),
converting a hex string to an integer, binomial coefficient
- SC decision-making processes, then and now. Conference calls vs GitHub
vs sc-users vs sc-dev for discussions.
- Extension of this discussion:
http://new-supercollider-mailing-lists-forums-use-these.2681727.n2.nabble.com/Github-in-web-editing-disable-td7630916.html

2017-02-25
==========

- Brian Heim has been working on regression tests for lexer/parser/compiler, which will ensure that changes such as #2673 and #52 can be safely fixed. Also started work on refactoring Document.
- Nathan Ho didn't do much, aside from starting to replace OSCpathResponder, etc. with OSCFunc.
- Luca Danieli has been working with Scott Wilson on making it easier to extend the IDE.

Topics:

- Migrating Contributing page from website to the repository itself
- Introducing a new issue template
- The changelog has gotten too long, time to clean out entries before 3.6.6 

2017-02-18
==========

Tom (@vivid-synth), Brian (@brianlheim), Rainer (@bagong) were present.

Recent work:
- Tom has been investigating UGen stability, and reports that Select is a prime example of a highly stable UGen
- Brian has been working on a refactor of the Document class
- Rainer has been working on the SC_SCLANG/MACOS_FHS build options

Topics:
- Full Windows support: obstacles are readline+Visual Studio (and the suggested alternative linenoise-ng), and the ongoing filesystem bug
- A possible structure for the new Document (and possibly IDE) classes - no decision reached
- Meeting frequency and format - we agreed that it might be a good idea to try to have once-a-month meetings as a larger group, and that the other weekly meetings could be smaller status updates. We'd also like to choose meeting topics ahead of time so that people with relevant experience will be more likely to participate.

2017-02-11
==========

What we did:

- Brian Heim has been trying to build SC on Fedora. Investigating
MacBook Pro 2016 performance issues with Sam Pluta. Details are very
unclear right now due to lack of data, could be a mix of a hardware
issue and a bug in SuperCollider. Drafted proposals for sclang
regression testing and verbosity.
- Nathan Ho made a small amount of progress on UGen regression testing
with an NRT mode version of loadToFloatArray.
- Tom Murphy has been reading the server code.

Topics:

- Boost submodules again
- Method table issue:
https://github.com/supercollider/supercollider/issues/1450

2017-01-28
==========

What we worked on:
- Tom Murphy worked on a minor control bus issue (issue 1280) and has been assigning trustworthiness labels to UGens.
- Alberto de Campo has three ongoing projects: multiclient server, improving node ID allocation, and improving the Quarks system so one can trace the quark associated to a given class.
- Nathan Ho did nothing aside from some small help fixes.
- Brian Heim sketched out verbosity levels in sclang.

Topics:
- Potential compatibility issues with the node ID allocation refactor
- Definition of sample-rate independence for UGens
- Automated testing pool for UGens
- Regression tests for the parser and lexer
- SourceForge must die
- Post-3.9, consider expanding our set of filters and reverbs
- Assigning a theme to each release and/or a funny name
- Making Boost a submodule, such as using the boost library instead of fopen
- Brian's ongoing PyrLexer rewrite 

2017-01-21
==========

What we worked on:

- Brian Heim managed to get SC built on Windows and has dug a bit into
the Windows helpfile issue, and has been working on a huge refactor of
PyrLexer.cpp (largely untouched since the initial commit!).
- Nathan Ho slacked off with some miscellaneous changes such as a Ctor
bug in FOS, and investigated OSC v1.1 "compliance."

Brian proposed that 3.9 be delayed until every important issue regarding
compatibility (in particular Qt 5.7, command line REPL, Windows help
files) is fixed, making it arguably the first fully cross-platform
release of SC. After that, 3.10 could concentrate on improving
user-friendliness by improving SCIDE and Qt GUI. 

2017-01-14
==========

What we worked on:
- Tom Murphy worked on benchmarking TCP/UDP, and on the new PlayBuf
proposal.
- Brian Heim read PyrObject and PyrLexer classes and filed a number of
sclang PRs.
- Nathan Ho mostly worked on help files.
- I couldn't hear Julian Rohrhuber very well, but I know he worked on
various (mostly classlib) tasks.

Topics:
- Brian discussed parser changes, e.g. "var" statements after other
statements.
- Julian discussed how difficult it is to trust the "_" notation.
- Julian's server refactor isn't quite complete -- server crashes aren't
completely graceful, but still better than before.
- Problems with class library standardization. Example would be the
various problems with the Rest system.
- Brian is concerned that the huge backlog of issues and PRs is
overwhelming. We could be more aggressive closing old issues and PRs,
and also be less shy asking people to finish things up.
- Fredrik Olafsson suggested using larger SynthDefs containing
collections of UGens in addition to pinning tests that target single
UGens.
- Julian talked about using mocking/stubbing in class library tests.
- Tom brought up issue #1209, a small mistake in the class library that
blocks headless systems.
- We should go through all the UGens and assign a confidence rating to
each one.
- Nathan started a draft of a comprehensive guide on how to record in
SC.
- Ways to improve our git workflow:
   - Consider a stable master with develop branch
   - Codify rules about when to merge things.
   - Only approve a PR if you've read the code and tested it, and say
what you did in the approval message.
   - If you don't understand a PR, don't be shy about prodding for an
explanation.
- The dev team should specialize formally -- put up a list of major
components of SuperCollider and who is assigned to what.
- Created two GitHub projects, respectively compiling the most important
issues for 3.9 and listing the long-term projects in SC:
https://github.com/supercollider/supercollider/projects/1,
https://github.com/supercollider/supercollider/projects/2

2017-01-07
==========

Development progress:

- Tom Murphy: started PlayBuf 2017 proposal, currently reading through
scsynth and supernova code.
- Brian Heim: generally exploring the code base, especially sclang;
submitted miscellaneous help file fixes; found a mysterious bug possibly
related to GC.
- Nathan Ho: lots of class lib and help miscellany.
- Scott Carver: connection quark, finishing up Qt menus, discussions
with the ATK devs about splitting from sc3-plugins.

Everything else we discussed, in roughly chronological order:

- Probably release beta for 3.9 in April.
- Scott discussed progress on the QtWebKit -> QtWebEngine port, which
faces difficulties due to the asynchronous nature of QtWebEngine.
- Code review and better docs for core features that need to work, like
GC and SynthDef optimization.
- Mounting complaints that SC is getting slower.
- Nathan should break the ice on unit tests by writing "pinning" tests
for UGens to guard against accidental behavior changes.
- Getting more people involved in Windows development, esp. fixing that
blasted help file bug.
- Ron Kuivila had some general comments:
     - Confusing abstractions in the Patterns system, such as the
opaqueness of EventStreamPlayers.
     - Making SCIDE more user-friendly. A larger pool of built-in
SynthDefs and/or integration with sccode.org.
     - Embedding sclang in Max, better connectivity to openFrameworks.
- TCP vs. UDP: create a new quark for automated benchmarking to allow
easy testing across different systems.
- Website improvements. Redesign can probably wait until later, but we
definitely need better resources for users interested in development.
- Brian volunteered to lead a "documentation drive" to help drum up more
user participation. Establish guidelines on how to write good help
files. Don't request minor changes like typo fixes on help PRs, just
merge and fix later. 