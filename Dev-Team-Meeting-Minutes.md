2018-12-01
==========

Members present: Brian, Edmond, Josh, Nathan, Patrick

At the current rate of development, 3.10.1 should be ready to go in a week or to.

Issues in SerialPort.devices and SerialPort.open, and QtWebEngine

nan printing issues: https://github.com/supercollider/supercollider/issues/4139. Possible solution is to introduce `Float.nan` or `Float.quietNan`.

Edmond has been maintaining the SuperCollider PlanetCCRMA release.

2018-11-18
==========

Members present: Brian, Bruno, Geoffroy, Nathan, Patrick

Geoffroy and Bruno introduced themselves.

3.10 is all set for release on Saturday (Nov 24). 3.10.1 should be released 1-2 weeks after. #4010 (QtWebEngine) is the priority but not blocking. Nathan has offered to work on it.

#4139 (floating point compile string) can be fixed this week.

#4132 (starting sclang as a systemd service) is more of an issue with systemd.

Confirmed legitimacy of #4133 (split window can crash IDE).

Geoffroy offered to work on redesigning the website. We agreed that it's much easier to just start from scratch.

Bruno is interested in doing GSoC work for SuperCollider. We will wait for the survey to make a decision on how he can best help the project.

New tutorials are chugging along, slowly...

Patrick brought up ways we could improve performance for embedded Linux -- particularly denormal issues on ARM processors.

Nathan discussed how the BEQSuite could be replaced with a faster and more numerically stable set of EQ ugens using state variable filters.

We discussed the future of sc3-plugins. Should we get rid of the trash and slim it down to an "incubator" for core ugens? Should we introduce the incubator as a new repository? Or should we let things be?

2018-11-13
==========

Members present: Brian, Nathan, Patrick

We're back !!!!!!!!

Merged #4105, an important issue for 3.10.

3.10.0-rc1 is ready. Between 3.10-rc1 and 3.10, only help fixes should be done.

We should take a look at #4137 soon.

Thanks to Scott C, UnitTesting class library issue is mostly resolved.

Nathan wrote a new compressor UGen that is almost ready for 3.10.1.

This weekend we'll comb over the 40 open pull requests and look at reviving GitHub project boards.

2018-09-24
==========

Members present: Nathan, Patrick

- Nathan hasn't done much
- Patrick looked for a solution for the UnitTesting conflict bug and found that quarks has a "compatibility" feature which we could use
- We discussed a new issue with [scel](https://github.com/supercollider/supercollider/issues/4074) helpbrowser loading failure
- We delisted [#3869](https://github.com/supercollider/supercollider/pull/3869) from 3.10 since its urgency is not clear
- Three issues remain before 3.10.0-rc1 is to be released:
  - Ndef fadein
  - Syntax colors affect IDE colors
  - keyDownAction message

2018-09-15
==========

Members present: Brian, Nathan, Patrick

- Critical issues in the wake of 3.10 beta 2:
    - Ndef fadeTime bug: Julian has fixed, test needs a touch up
    - Syntax theme changing the UI colors (better IDE customization)
    - Daniel reported that HelpBrowser doesn't load
    - Float printing side effects via adclib: if you override `Float:asCompileString` it's kinda your problem buddy
    - Issues running on older Macs
    - QtWebEngine only runs on macOS 10.9 or later and macOS 10.10 SDK
- Next beta: Brian will write up a quick blurb on how to properly report issues.
- On release, point people to a guide on how to report issues
- Brian reformatted the repository's whitespace in a branch
- Nathan has been working on making QtWebEngine optional
- Patrick:
    - https://github.com/supercollider/supercollider/pull/3968 - closed
    - https://github.com/supercollider/supercollider/pull/3728 - critical (pressure from Norns devs)
    - https://github.com/supercollider/supercollider/pull/3870 - not critical, change milestone to 3.10.x
    - https://github.com/supercollider/supercollider/pull/3221 - not critical, but should be reviewed
- Cookiecutter ugens
- UnitTesting quarks duplicate class error: we need to open an issue for this...
- Bela denormal test

2018-09-13
==========

Members present: Brian, Nathan

- Brian has been working on a template for generating UGen projects
- Nathan has been working on tutorials

Topics discussed:

- Ways we could simplify and improve sclang path searching
- macOS bundling problem is fixed!
- Ways we can improve our CMake code
- Debian packaging
- Brian has been working on automatically reformatting whitespace. After 3.10 release is the perfect time to do that.
- Release 3.10-beta2 as soon as mac thing is fixed

2018-08-19
==========

Members present: Alex Goldsmith, Brian, Nathan, Patrick, Scott, Thomas

3.10.0-beta1 is out!!!!!!!!!!!!!!! (not announcing yet until sc3-plugins beta is ready)

Member updates:

- Alex uses gen~ a lot and would like to see single-sample feedback for more fine-grained DSP goodies such as TPT filters & ladder filters with customizable nonlinearities, and discrete summation formulas. He had some trouble with HID, which was last touched 4-5 years ago
- Brian hasn't done much
- Scott hasn't done much
- Patrick has a bandage for his HelpBrowser issues, developed a new quark called SATI
- Nathan is working on improving the look of the IDE

Topics:

- We'll be (privately) putting together a survey after 3.10 release to get a good idea of the direction for 3.11, which we hope will be released very quickly
- New forum is going well: questions are getting answered, lots of little mini-articles
- We have tried to get sclang into some major syntax highlighting packages like Highlight.js but most of them have gone without response
- A priority for 3.10 is packaging supernova in the official release for Mac
- Brian's big projects moving forward are improving the test suite and standardizing C++ formatting across the codebase
- Pinning test for ugens
- Rendering SCDoc and uploading CI
- Remaining "big annoying projects:" SCIDE startup sequence unreliability, debian packaging, supernova on windows, command line on windows
- Brian suggested that Alex work on compiler warnings
- Possible new official tutorial development with e.g. gitbook, outside SC help system
- "Clear post window" menu item
- Aaaaaaaaableton Liiiiiiiiiink: going slow, going steady

2018-08-12
==========

Members present: Brian, Nathan, Patrick, Thomas Capogreco

- `Signal:==` random true/false PR
- Patrick is still having help browser issues and will file a ticket
- Luke's UI colors PR
- Thomas's work involves connecting SC to modular synths, which requires clock synchronization

2018-08-05
==========

Members present: Brian, James Harkins, Josh, Nathan, Patrick, Scott Carver

- Status of the 3.10 release:
  - Linux help browser shortcuts fixed
  - Help browser shortcut almost fixed
  - SerialPort almost done
  - FileDialog hangup and SCIDE look and feel still not started
- Josh have been working on package manager for plugins
- James is working on Score/NRT helpfile improvements
- Brian suggested that we release beta this week, documenting the 2 remaining issues
- Issue + PR templates: good idea, a bit too long right now
- File object, File APIs
- Time for a new logo?
- Resurrecting the UI refresh branch
- Design documents as a method for preventing pull requests that attract huge amounts of nitpicky comments
- Nathan brought up a safe output clipping proposal
- Patrick is having a bizarre issue with the help browser

This week:
- Merge SerialPort and the Cmd+Enter help browser
- Release beta with "known issues list"
- Josh will take initiative on logo redesign
- Nathan will work on SCIDE
- Scott will work on FileDialog
- Put out a user survey

2018-07-28
==========

Members present: Josh, Julian, Nathan, Patrick

- State of 3.10 and "project docs task force"
- getToFloatArray PR
- HOAUGens sc3-plugins PR
- Divide between new forum and lists
- Examples were historically a huge part of SC
- Ideas for improving official tutorials, e.g. a "choose your own adventure" format allowing choices between JITlib, architectural info, and tours of UGens

2018-07-20
==========

Members Present: Josiah Oberholtzer, Nathan, Patrick, Scott C.

- New Discourse site, legal concerns and Code of Conduct, longevity of the forum, diversity and community health
- Suppressing dock icon when sclang is built with Qt
- Josiah is working on real-time server without audio driver ("null driver"), building headless SC on travis
- Being decisive about replacing bespoke components (e.g. SCDoc) with established software
- State of unit testing in SC
- Merged Windows Qt issue
- Rebasing server menu issue
- SerialPort and Windows PR is basically ready to go, but tests should be skipped if the user doesn't have socat/com0com installed
- Various shortcut issues evaluating code in SCIDE
- Embedding a code font on SCIDE: the defaults are really blinding, and a consistent visual style is nice
- Idea: merge Yvan's ServerOptionsGui quark into core for 3.11? (with some improvements to deal with cross-platform differences)
- Scott has a lead on the KDE FileDialog issue -- the real mystery is that it's not happening on other platforms
- Patrick's help browser issues
- Scott's SynthDef specs PR: 3.10 or not?

2018-07-12
==========

Members Present: Brian, Luke, Nathan, Patrick, Scott C

We reviewed the remaining to-do tasks for 3.10:

- Linux SCIDE theme -- Luke has decided to look into it
- KDE FileDialog issue
- Scrollbar issue delisted for 3.10
- SerialPort is 99% ready, but RPi and Windows tests are a good idea.
- Help browser code evaluation bugs (#3777, #3829)
- Scrolling userview with non-integer device pixel ratios
- Ableton Link PR has stalled despite attempts in the past month to revive it. There are current disagreements about latency issues.
    - Arguments for inclusion in 3.10: we promised it, and it's okay to merge an imperfect feature and fix it later
    - Arguments for exclusion in 3.10: we've already done a lot for 3.10 and it's not a mortal sin to wait another release

Overall, we've been doing well! We hit 2000 stars on github and we're closing a dozen pull requests each week. We could be improving ways to help new contributors find the best way to have a good impact on the project. The "good first issue" label helps. We could also be making good use of the Projects feature to map out the next 2 or 3 releases and give a good idea of what to work on.

 How do we chip away at 600 open issues (only 200 of which are tagged as bugs)?

- An extreme solution would be "bug bankruptcy:" closing ALL bugs except things currently being worked on. If a bug really is important, users will ask the issue to be reopened. Too radical right here and right now.
- Establish limits on the number of open issues?

Experienced developers working on and discussing small issues isn't necessarily optimal. If someone files an issue, someone more experienced can point them to a fix.

We haven't really worked out a process for giving push access to new contributors.

We've reached a point where we have some PRs we don't want in 3.10, so it's time to make a 3.10 branch.

Scott got some emails back from 3rd-party devs of SC-adjacent software, and for a dev meeting in the near future, we will be inviting some of them.

In addition, we should also get talking with the user base a bit more about the long-term direction of the project, perhaps with a new survey, to help close the gap between what many users want and what developers are working on.

We discussed some fantastical ideas about GPU SuperCollider and VST integration.

2018-06-10
==========

Members present: Luke Nihlen, Nathan, Patrick

Recent work:
- Nathan worked on the Linux README and investigated the no-Qt CPU hog issue
- Patrick has been working on the long-stalled HOAUGens pull request in sc3-plugins, and has several class library PRs going
- Luke made his first PR, which fixes a crash in the `Array:lace` primitive

Discussion topics:
- Various growing pains in UnitTest that have been causing delays in language and class library pull requests
- UnitTest clogging up the quark pipes is a pretty serious issue but it's not receiving any discussion right now
- The remaining 3.10 features are Windows SerialPort and Ableton Link
- State of SuperCollider tutorials

2018-05-25
==========

Members present: Brian, Nathan, Patrick, Scott Carver

Recent work:
- Nathan wrote NHHall UGen -> sc3-plugins, wrote a spec for antialiasing UGens
- Scott has been working with pattern library and thinking about improving consistency w/ multichannel expansion
- Patrick has submitted some small and helpful PRs
- Brian has reviewed some PRs and has ported SerialPort to Windows

Topics:
- Denormals - we want them to be always flushed, but it sounds like on ARM (and sometimes on x86) they aren't (reported by Nathan)
- HOAUGens - Patrick will help move this PR through
    - need to remove the units that don't build on other platforms
- Scott has been working with ATK members on their HOA generators - may be a better HOA implementation for SC project

3.10:
- Target goals: Qt update, Qt Menu support, SerialPort port, UnitTest/Quarks issue, LinkClock
- Release mode when?: will revisit soon

3.9.4:
- discussed possibility. Nathan is unconvinced of the need for this, will possibly revisit.

Norns/Embedded:
- recent popularity bump. Should work on improving tutorials
- interest in SC on embedded devices may be ramping up
- consider focusing on improving RPi-SC experience for 3.11 (in the same way 3.9/3.10 were about improving Windows experience)

Documentation:
- Brian has an "edit this doc on GitHub" button

Bela:
Bela has a remedy (not a complete fix) for this nasty issue when building without Qt: https://github.com/supercollider/supercollider/issues/2144.  This is a pretty bad issue especially as SC finds use in embedded systems like the Norns. Maybe the Bela team's patch should be merged in?

Another important performance issue for embedded SC: https://github.com/supercollider/supercollider/issues/3524

Scott offered to reach out to the Monome, TidalCycles, and Sonic Pi teams via email and improve communication with big commercial and open-source projects.

Pushed 3.10 milestone due date to June 30th

2018-03-31
==========

Members Present: Brian, Nathan

Discussion Topics:

- 3.9.3 release:
    - (Kind of) necessary to patch regression in Score (fixed in https://github.com/supercollider/supercollider/pull/3608)
    - Could also backport https://github.com/supercollider/supercollider/pull/3558
    - Updated release date to April 7

- 3.10 goals:
    - Still agree that Qt 5.9 branch and Ableton Link support are among the top goals

2018-03-03
==========

Members Present: Brian, Nathan, Patrick

Recent work:
- Brian: reviewing & merging PRs
- Patrick: website PRs
- Nathan: reverb development

Discussion Topics:

- 3.9.2 release - what to merge before releasing
    - 3486 (Alberto - fix re-login behavior)
    - 3521 (James - isRest backport)
    - 3544 (Julian - asScore)
- Issues for 3.9.2:
    - 3396 (Go back/Go forward) - maybe close as wontfix
    - 3454 (GC bug) - move to 3.9.x
    - Remaining moved to 3.9.3
- Move back 3.9.2 release date to March 10 to allow for last PRs to merge
- Agreed to focus on 3.10 after 3.9.2, but still allow work on 3.9 branch
- Patrick mentioned he knows someone who has an issue with HiDPI & performance stuff on macOS

- Goals for 3.10:
    - Ableton Link integration
    - Upgrade to newer Qt versions
    - Make SerialPort available on Windows
    - Fix startup IPC among components

- SCDoc replacement?
    - Nathan vouched for Sphinx

- Nathan discussed his anti-aliased UGens (SawPoly1, reverb)

2018-02-24
==========

Members Present:

Brian, Julian, Patrick, Scott C.

Recent work:
- Brian: primitive-defining macro for cleaning up sclang
- Julian: neurological SC, project with Dutch CS/math prof; ideas about having extra sclang processes in background; small PRs
- Patrick: testing HOAUGens PR, Issue 3396 (Help browser navigation)
- Scott: cleanup on Qt WebEngine PR, Atk-related HOA, generic primitive wrapper (to bind to Boost.Math headers), calling native C functions from sclang using dyncall (proof-of-concept)

Discussion Topics:

- Issue 3396
    - Scott thinks this is a Qt problem and may not be under our control

- Julian: could we unify the code editor and help browser?
    - Scott: would take a lot of rebuilding; possible as a big project; could make a rich-text webview using existing open-source editors

- Scott C's PR to update the help browser to QtWebEngine
    - Allows us to move to newer versions of Qt
    - Also fixes HiDPI-related issues
    - Qt Menu addition would ideally be merged not long after

- Qt Menu idea - could make it easier to add system menu items for the IDE from sclang

- Julian: would like to add more examples to Help system
    - Scott: been doing overview-type work, have examples for WebView

- Making it easier to submit bugs/changes from the Help Browser

- CMake: update to 3.x because of Ableton Link PR
    - Scott: use CMake 3.9.4 (what we have on Travis)
    - Make sure smiarx gets credit
    - Patrick: maybe 3.5 (Ubuntu) or 3.7 (Debian)
    - Scott: be transparent about what we use on Travis

- Scott: create a "template" for repos to easily make your own repo w/ auto-released binaries
    - Make easy alternatives if we're going to say no

- Do a better job of announcing/promoting 3.10 and its improvements
    - Get links to Eli Fieldsteel's tutorials
    - Get links to the DX7 project
    - Show how to link to other DAWs

2018-02-17
==========

Members Present:

Patrick, Nathan

Recent work:

- Patrick has been removing some old crap on the website
- Nathan has been refactoring the new reverb for efficiency

Topics:

- 3.9.1 announcement delay
- Recent advances in Debian packaging
- Timing of introduction of scel and Ableton Link submodules
- 3.9.2 release date moved to March 3rd
- Two Rest-related issues for 3.9.2
- Some issues tagged as 3.9.2 have been moved back to 3.9.x since nobody is actively working on them
- Refactoring scsynth to improve the API, advantages and disadvantages of moving to modern C++ practices
- Timing of the creation of 3.10 branch (in my opinion, creation of the 3.10 branch indicates that it is closed for new features)

2018-02-03
==========

Members Present:

Nathan, Brian, Patrick

Discussion Topics:

- 3.9.1 is ready to release
- VBAP panning bug in sc3-plugins was fixed by Nathan
- Brian is working on a unit testing guide
- Nathan is working on unit tests for scsynth and for unit generators
- HOAUgens are nearly ready to be merged to sc3-plugins
- people have learned a bit more about CMake recently
- considering moving to CMake 3(.1?) - seems well-supported at this point

2018-01-27
==========

Members Present:

Brian, Patrick, Nathan

Discussion Topics:

Recent work:
* Patrick: lots of small website fixes, sc3-plugins PRs
* Nathan: custodial stuff, UGen testing, planning to work on UGens for school project
* Brian: couple of minor fixes, Boost update PR, custodial stuff, looked at Qt update PR

sc3-plugins
* PR #146 has some issues
* It's still an open question of how to best add Faust-to-SC plugins to sc3-plugins
* Would be nice to have a minimal checklist for things that go in

3.9.1:
* Ready to start the release process
* Merge #3469 as last item for 3.9.1 (?)
* Nathan has created a 3.9.2 milestone

Unit-testing:
* Guidelines are badly needed
* A future goal is to move most (if not all) of UGen testing code to C++ for speed and dependability

2018-01-20
==========

Members present: Nathan, Brian, and Patrick

- 3.9 release went well -- downloaded over 1000 times.
- 3.9.1 has 14 closed pull requests, which is plenty enough for a patch release. Although we are not in any rush, we could easily release well ahead of the scheduled date of January 31st.
- Brian has been working on AppVeyor integration, monitoring LiveCode Slack for new issues.
- Unit tests are not written consistently due to lack of documentation.
- Unit & integration tests for UGens can be written in C++ using Boost.
- Various ways the appearance and usability of the IDE could be improved:
  - For 3.9.1, let's just make auto-indent optional instead of fixing it entirely. Unfortunately, there is no reliable way to test changes to auto-indent.
  - Embedding volume meter and other basic controls.
  - Difficulties making SCIDE look attractive on arbitrary native themes, and the possibility of
  - Replacing the default light theme entirely.
  - Making the Documents docklet match the theme for visual consistency.
  - Making the Documents docklet match the theme for visual consistency (much more difficult!).
  - Licensing of themes.
- SCDoc regressions
- FreqScope improvements -- afterimage, antialiasing
- SuperCollider installation on Raspberry Pi is absurd, involving manually moving files
- Debian packaging has mostly hit a wall :(
- Adam's Guard configuration PR can go into 3.9
- Release signing
- Travis is back in order

2018-01-13
==========

Members Present:

Brian, Julian, Patrick, Nathan

- Work remaining for the 3.9 release (laments about Travis issues)
- Licensing concerns for new editor themes
- "Known issues" section in changelog

2018-01-06
==========

Members Present:

Brian, Patrick, Gerard (g-roma)

We just discussed the SuperColliderAU PR/project and where it belongs in the SC org repository constellation.

2017-12-30
==========

Members Present:

Nathan, Patrick

Discussion Topics:

- 3.9.0-rc1 needs to be announced to Facebook...
- Currently waiting for users to test 3.9.0-rc1. If all goes well, we will make a decision on January 6th 
- Merged last remaining PR for 3.8.1.
- Fragmentation of SC community across different platforms.
- Would be a good idea to revive sc-dev and have more in-depth discussions on the list instead of on GitHub.
- We should announce major PRs to the list and regular updates about what we're working on.
- Decided against creating a 3.9.1 branch for simplicity. 3.9.1 patches can wait until the 3.9.0 release.
- Speed of release schedule can be improved by being less choosy about what needs to go into each release. If something holds back the release instead of pushing it forward, it needs to be delayed.
- Patrick redesigned the download page for the website to be up to date for Linux users.
- Nathan has been working on Debian packaging but has mostly been hitting dead ends.
- Bela port of SuperCollider has diverged considerably from core, we need to consider what to merge in.
- Future website redesign could probably be done as a quick weekend project.

2017-12-23
=========

Members Present:

Brian, Nathan, Patrick

Discussion Topics:

3.8.1:
- Merged #3348, will update changelog and release 3.8.1 soon.
- Because of #3348, will also have to add binaries to release.
- Nathan has created a draft release.
- Will have to be tagged on 3.8 branch since master already has 3.9 stuff in it.

3.9.0:
- Nathan will review and merge 3275
- And after that, release next instance because it closes all open 3.9 milestones
- #3266 - no longer milestoned as 3.9. Marked as "waiting for information" since cause is unclear
- Decided to call it a "release candidate" since all bugs from 3.9.0 beta are eliminated and signals that we are very close to release
- 3.9.0 release set for 1/1 unless major issues arise

3.9.1:
- Nathan wants to release 3.9.1 a month after 3.9.0. Ambitious but we are setting the bar low for the number of changes going in.

Wanted for 3.10:
- Nathan: new UGens (will work on as an independent project for school)
- Ableton Link synch (#3351)
- Brian: Update Boost, update Qt version
- Brian: Fix SerialPort on Windows

SuperColliderAU PR (#3350)
- SuperColliderAU reboot that runs from current develop.
- Agreed it would be better to move some of the project to a submodule

scsynth allocator PR (#3318)
- milestoned 3.10 at Brian's request

Patrick: safeguard for syntax errors in startup files.
- Right now it causes a mysterious error with no indication that it came from the startup file.
- Could easily be fixed for quality of life improvement

Thanks to all who attended! The next meeting has been set for December 30, 2017 at https://appear.in/sc-dev-meeting.

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