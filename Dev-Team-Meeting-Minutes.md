2017-12-16
=========

Members Present:

Brian, Patrick

Discussion Topics:

3.8.1:
- waiting on Nathan to release this small update
- purely meant for Arch Linux packaging
- just source code, no binaries

3.9.0:
- Alberto merged Brian's PR into the 3275 PR
- Patrick's PR cleaning up TestServer is ready to be merged
- Plan (tentative): merge 3275 within a week and release a second beta by Dec 23

Thanks to all who attended! The next meeting has been set for December 23, 2017 at https://appear.in/sc-dev-meeting.

2017-12-09
=========

Members Present:

Brian, Patrick, Nathan, David (Runge)

Discussion Topics:

3.8.0:
- possibly releasing 3.8.1 with a header include fix so that it builds with latest gcc toolchain
- see discussion in #3015/3029, would help with Arch Linux

Debian packaging: ongoing woes. Might contact umlaeute (Debian packager for pd)

PRs for 3.9:
- 3275 (lockClientIDWhileRunning):
  - Patrick has no issues with branch, has been using for awhile
  - Brian is ready to review
  - Julian should also review
- 3332:
  - Fixes an issue with the default server Volume synth

3.10:
- Brian wondered about starting to update libraries (like Boost) on develop branch in advance of 3.10
  - is OK, but should still focus efforts on 3.9.0/3.9.x

Thanks to all who attended! The next meeting has been set for December 16, 2017 at https://appear.in/sc-dev-meeting.

2017-12-02
=========

Members Present:

Brian, Patrick, Nathan, Josh P., Julian

Discussion Topics:

PRs for 3.9:
- 3317: merged, closing 3196
- 3318: maybe a bit of testing before merge
- 3275: still needs some work
- 3267: merged

Issues remaining for 3.9:
- 3266: still an open question
- 3176: Nathan can fix but is busy, might not go into second beta

3.9.1 issues and PRs:
- 3 good-to-go PRs already queued up
- 1390: "Error: ScIDE not connected": possibly not able to tackle in 3.9.1
- 3310: milestoned as 3.10

Nathan wants to work on new UGens for 3.10 

Josh: plan out things to unit test in 3.9.1, .2, .x based on issues we're running into now – e.g.: server booting process; synthdef loading

Future of Supernova and Scsynth – could one be merged into the other?

Library maintenance for 3.10: boost upgrade, Qt upgrade

Thanks to all who attended! The next meeting has been set for December 9, 2017, 21:00 UTC, at https://appear.in/sc-dev-meeting.

2017-11-18
=========

Members Present:

Brian, Patrick, Ben, James (McCartney)

Discussion Topics:

Brian: 
- planning to debug beta-related issues (#3196)

Patrick:
- wants to test Alberto’s PRs (#3275, #3286)

Ben:
- has been working on building SC on Windows to get familiar with the build process
- will start working on Supernova n_order issue (#3100)

James:
- just came to lurk

Issues before next beta release: with everyone's planned combined efforts, it sounds like we should be able to address most of the relevant issues in the next few weeks!

Symposium 2019 discussion on mailing list: yay

Thanks to all who attended! The next meeting has been set for November 25, 2017 at https://appear.in/sc-dev-meeting. We will try to keep the same time: 4 PM EST.

2017-11-04
=========

Members Present:

Brian, Nathan, Josh, Patrick

Discussion Topics:

Issues arising from AudioControl changes (#3266, #3196)
History cleanup PR – can be merged once done (#3267)
SCDoc UI - Nathan wants to make TOC popout only to smooth over bad behavior of dropdown TOC
Lock client ID while Running PR (#3275)

Priority: fix audio control issues for 3.9.0, possibly releasing a second beta

Dan Stowell’s blog post about Linux packaging
Should remove outdated PPA mention from website
Use Docker for testing
Pulseaudio/Jack woes
Would like to add documentation on buffer allocators

3.9.1:
Will be mainly our testing ground for shorter release cycle.
Nathan wants to fix two issues (auto-indent in IDE, default font on macOS)

Thanks to all who attended! The next meeting has been set for November 11, 2017, time TBD.

2017-10-28
==========

Members present: Brian, Julian, Nathan, and Patrick

We are moving the next meeting to 6pm eastern.

We are just about to announce the 3.9 beta, and we're currently waiting to test the windows builds.

Development cycle for 3.9.x releases will tighten considerably -- maybe about two months between each one, or about 20 pull requests. We are also aiming for a fairly short 3.10, something around six months.

To help motivate development progress, each patch release has one required major bugfix. For 3.9.1, we should fix two longstanding IDE problems: auto-indent and the default font on macOS.

Some other good issues that we should turn our attention to, but arent required for 3.9.1: Integer:forBy bug and CPU hog with Qt-less sclang. "Edit on github" feature is almost done. Brian is also interested in fixing a lot of our development infrastructure such as the tests system.

Release of stable version is done by merging 3.9 branch into develop, and then 3.9 into master.

We are changing our approach to milestones. 3.9, 3.9.1, and 3.10 milestones are all strict -- if an issue or PR is categorized under them, those issues MUST be resolved before release. 3.9.x milestone means issues that aren't required, but it would be nice if we could fix them in a patch release soon. Issues can be moved from 3.9.x to 3.9.1 if it is decided that it's practical to complete them in time for release.

2017-09-30
=========

Members Present:

- Brian:
- Nathan
- Patrick

Discussion Topics:

- Patrick’s PRs to the supercollider.github.io site and his plans for future work on the site
- The last few things that are ready to be done before 3.9 release (getting very close)
- Issue https://github.com/supercollider/supercollider/issues/3211
- git flow maintenance of the release and develop branches

2017-09-23
==========

Present: Brian, Nathan, Lucas, Edmond, Patrick

- Brian: GitHub edit link with Cian, distance-based amplitude panning (DBAP) UGen
- Nathan: Linux packaging, Debian packaging
- Patrick: working on help system soon
- Lucas: introduced himself, interested in contributing when possible
- Edmond: introduced himself, interested in contributing C++

### Discussion Topics

Multi-client ID PR:

- still failing on Travis because of test integration issues
- either fix test integration or disable tests temporarily

New UGens:

- Nathan wants to work on more UGens after 3.9 release

Cleanup:

- Brian wants to work on documentation for new contributors and cleanup/organizational work for the codebase

main SC site:

- Needs love
- Feature more projects
- Update text

Moving out Emacs submodule:

- Open issue (https://github.com/supercollider/supercollider/issues/3066)
- Will wait until post-3.9 and ask on dev list

Thanks to all who attended! The next meeting has been set for September 30, 2017, at 16:00 UTC (12p EST) at https://appear.in/sc-dev-meeting .

2017-09-16
==========

4 members were present: Brian, Alberto, Cian, and Nathan

Recent work:

+ Brian: documentation, especially unit testing documentation
+ Alberto: multi-client ID PRs
+ Cian: Ableton Link work, forBy interpreter bug
+ Nathan: pitch shift window size PR

Discussion topics:

+ issues with ReadableNodeIDAlloc PR
+ unit testing documentation
+ creating a template/generator for unit test code
+ documenting C++ source code
+ adding a link to help files to go to editing the help file on GitHub
+ removed email notifications from GitHub to sc-dev
+ getting the help browser to open a GitHub edit link in default OS browser

Thanks to all who attended! The next meeting has been set for September 23, 2017, at 16:00 UTC (12p EST) at https://appear.in/sc-dev-meeting .

2017-09-09
==========

Five members were present: Cian (@cianoc), Nathan (@snappizz), Brian (@brianlheim), Alberto (@adcxyz), and Jack (@jarmitage)

Recent work:

+ Brian: travisCI, unit testing, organizational documentation
+ Nathan: Debian packaging
+ James: interested in helping out (currently mainly a user)
+ Alberto: multi-client ID PR
+ Cian: fixing help files, potential Ableton Link support in 2-3 upcoming PRs

Topics of discussion:
multi-client ID PR:

- Alberto has raised new issues on GitHub to target specific design problems that arose in the PR
- He plans to rework #3106 (the current PR) into a few smaller PRs to avoid stagnation
- We talked about whether to put it in 3.9 or 3.10, and agreed that some of it should definitely go in 3.9 (see discussion below)

Suggestions from Cian:

- improve documentation for new supercollider users (coming from i.e. Ableton)
- add a UGen overview
- add a Quark overview

3.9 critical todos:

- block allocators portion of multi-client ID fix
- sendNotifyRequest extension of multi-client ID fix
- after that, release! OK to push a beta without full Linux packaging
- continue to work on Linux packaging, hoping to have a good release 

Adding UnitTest and test suite in common:

- Nathan pointed out there are issues with the UnitTest class that should be worked on
- We discussed (and tentatively agreed on) putting the test suite in the main class library
- This would be aided by adding a helpfile for unit tests documenting how to disable unit tests if desired

Thanks to all who attended! The next meeting has been set for September 16, 2017, at 16:00 UTC (12p EST).

2017-06-10
==========

Three members were present: Brian (@brianlheim), Nathan (@snappizz), and Julian (@telephon).

Topics of discussion were:

- Till's recent email to the dev list, sc3-plugins and maintenance of SC's "satellite" projects
- some close-to-being-merged PRs: we talked about what was needed to merge
- method table: Brian agreed to test the performance of the language (both memory and speed) with a high number of methods defined, to either put to rest or confirm old rumors
- PR backlog: Julian agreed to move a number of his inactive PRs to the PR backlog (https://github.com/supercollider/supercollider/projects/7).

Thanks to all who attended!

2017-06-03
==========

- Brian finished the breadcrumbs link issues and filesystem UTF-8 support.
- Nathan didn't do much aside from participating in discussions

topics:

- we merged 10 pull requests and closed 16 issues this week! holy hell!
- Rest refactor is pretty much ready. Nathan should review it, merge within the next week, and we can then do a post-mortem
- current open discussions regarding style guides, and issues with design by committee in free software communities
- should we really dedicate time to sc3-plugins?

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