2020-04-12
==========

People present: Nathan H, Brian H, Patrick D, Geoffrey M, James S, Gianluca E, Josh P

Welcoming Gianluca!

What people are up to
- Geoffrey: looking at autoindent in IDE, waiting for review on #4797
- James: reviews, working on implementing spelling correction suggestions in sclang parser
- Nathan: working on other projects
- Patrick: refactoring TestBuffer to break out server-requiring tests
- Josh: managing releases
- Brian: reviewing, beginning to implement RFC #1

3.11.1
- discussed Brian's cherry-pick PR
- need to merge in scel update for support on ubuntu
- decided to postpone outstanding issues (#4544, #4826)
- decided to release ASAP

sc3-plugins
- discussed merging Scott C's PR and doing a release
- Josh P said he thinks we should merge it and include in 3.11, general agreement

Other PRs and issues
- Patrick asked about best practice quitting servers in unit testing

2020-03-29
==========

Members present: Brian H, James S, Nathan H, Marcin P, Patrick D, Clare M, Tejaswi P

3.11.0 release:
- Josh P will make new sc3-plugins release and source tarball for sc 3.11.0 as soon as possible

3.11.1 release:
- #4703 close to merge
- #4583 waiting on Brian's review
- discussed Wayland issue
- discussed cherry-picking
    - Nathan suggested documenting git process w/branches in readme
- #4826 - no progress yet, will revisit

Patrick brought up #4136 GPU issue on macOS

3.12.0:
- Nathan suggested we should make sure we decide on / have at least one new big feature before making a minor release
- RFC process needs a bit of a kick-start
- Patrick wanted to have a release in <1 year
- Clare talked about her experience with release schedules
    - what worked: commit to a regular release schedule (quarterly at her work)
    - just release whatever is available (could be patch or minor)
- discussion about release schedules & universities
    - more frequent releases => departments install more recent versions

other:
- Nathan would like to release some new (personal) UGens soon
- Clare would like to start contributing again in the next few months
- Patrick wants to help with the sc3-plugins release
- discussed anxiousness about reviewing
- discussed review behaviors and commit messages

2020-03-15
==========

Members present: Brian H, Josh P, James S, Tejaswi P, Nathan H, Marcin P, Julian R

3.11.1: discussed PRs and release date
- Make an RC by April 15, release by April 30
- #4544 is priority for 3.11.1 or 3.11.2
- #4826 also recommended
- Marcin recommended #4599, we agreed it should be included
- Julian recommended #4779, we agreed it should be included
- Brian recommended all "Cherry-pick to 3.11" PRs

3.12.0: discussed release date
- Josh suggested 6 months from 3.11.0 release. Discussed impact of COVID-19 outbreak and associated instability on development
- Nathan recommended focusing on a single project for next release

Julian brought up his concept for an "AbstractObject"/"Neutral" RFC
- discussed design and possible implementation

Discussed open and future RFCs

Discussed deprecation policy

2020-03-01
==========

Members present: Brian H, Josh P, James S, Tejaswi P, Patrick D, Marcin P, Geoffrey M

3.11 beta out - what issues before release candidate?

https://github.com/supercollider/supercollider/pull/4784
https://github.com/supercollider/supercollider/pull/4783

Downloads - 25 Mac OS , 20 times for Windows

Tag needs prefix of ‘Version-3.11.0-beta1’

RC in a week - 

Merge 3.11 to develop soon

Verify Supernova on Mac is included.

3.12 ? - review RFCs - final comment period after Josh checks with authors

Debugger for 3.12

Created a 3.11.1 board
	- check the issues that were added

Open Topics:

Patrick: https://github.com/supercollider/supercollider/pull/4786

Brian: For releases, we should create an issue for discussing the release. 
3.11.1 created

3-14 for next meeting

2020-02-09
==========

Members present: Brian H, Josh P, James S, Tejaswi P, Patrick D

SC symposium - discussed who is going and informal travel plans

GSOC - weren't able to find a second mentor, won't be doing it this year

General progress update
- Brian - busy in other projects lately, planning to get back to reviews this week
- Josh - busy in other projects lately, suggested releasing 3.11 beta soon
- Patrick - worked on updating pull requests -- wants to merge #3814, #4761
- James - busy with other projects lately, planning to review some PRs
- Tejaswi - just changed build environments, interested in reviewing PRs, added to Reviewers GitHub team

3.11 beta release - planned for Feb 16 - Josh will handle

Brian suggested doing calls every other weekend
- Josh, Patrick agreed that would be good
- James and Josh suggested doing check-ins via another medium instead of the meetings when we don't have them

Discussed moderation of the scsynth.org forum - James S said he would be interested in helping moderate

Discussed #4713 and refactoring scdoc

2020-01-26
==========

Unfortunately no minutes are available for this meeting

2020-01-19
==========

Members Present: Brian H, James P, Marcin, Tejaswi, Patrick D, Nathan H

Discussed procedure around releases and timeline for 3.11 release.
No decisions made as Nathan wasn't present yet.

Discussed some open PRs (#4599, #4704) and review process

Patrick brough up QPM PR #10 for attention

Patrick reported that he's making progress running tests in CI, ready to make a PR that runs tests in CI on Linux

Marcin asked for help with PR #4583, Brian said he would assist

2020-01-12
==========

Members Present: Josh Parmenter, Brian Heim, Nathan Ho, Patrick Dupuis

Josh, Brain, Nathan, Patrick

Brain is watching cool movies

And building laptops

Nathan is giving out Linux audio advice

TODO: announce RC2
	3.10.4 should be about ready to go

3.11 release! Check status on the mail list with James H - can we do 3.11 soonish? OR - should we be thinking about a 3.10.5 release. 
	Ask about 3.11 / Ableton readiness on mail list
	If not - 3.10.5 may be a better route (Patrick)

Discussion of release management  and documentation. Nathan to fill in some gaps and help start a document for responsibilities.

Had a question about package.sh in distribution


Document minimum required version of OS X - 10.12? (Because of Qt 5.13) - should be noted in the release.

Discussion of QPM debugging with Patrick

Discussion of shell scripting problems with QPM and environment variables

2020 - year of SC website?


2019-12-08
==========

Members Present: Brian Heim, Carlo Capocasa, Chad Cassady, James Surgenor, Josh Parmenter, Josiah Oberholtzer, Marcin Paczkowski, Nathan Ho, Patrick Dupuis, Tejaswi Prakash

Release status:
- 3.10.4: Beta release immediately.
- 3.10.5: Address three issues below.
- 3.11.0:
  - Nathan is open to resuming release manager.
  - Quality assurance for LinkClock.
  - Scott Carver's SynthDef spec PR #3814.

Release board issues (now postponed to 3.10.5):
- Issue #4214 (IDE stuck at "Sending Request"): James believes this is resolved, but needs more testing.
  - Nathan will test and look at it
  - James will write up an explanation of why this is happening and why this fixes it
- Issue #4368 (Windows Defender delays scsynth boot): not much new information
- Issue #3132 (CommonTests quark -> local UnitTests): considered ongoing, not important for 3.10.4

Other topics:
- Suggestion for high priority after the 3.10.4 release: getting the number of open PRs to 10 or fewer
  - The number of open PRs has been overwhelming since the code reformat
  - Brian's advice for reviewers: ask for information immediately whenever it is needed
  - Nathan suggested setting aside a weekend "review-a-thon" for tackling pull requests
- The Release Board has been really helpful in prioritizing the set of issues
- RFC #1 (platform support guarantees): waiting on Brian
- RFC #4 (Rest): ping James H & Julian on status of discussion
- RFC #7 (binaries in Quarks): some discussion summarized in the actual RFC thread
- RFC #5 (/s_query): awaiting another round of feedback
  - Opens up some wider discussions about how /g_queryTree is broken/weirdly designed
- Comment on the general RFC process: it's a bit difficult to see current status of RFC
- A new page for "Pre-RFCs"
  - Cannibalize the old "Long-term, large-scape projects" board into a wiki page

Action items:
- Fix a 3.10/develop merge conflict in TestUnitTest.sc.
- Create a "Pre-RFC" page.
- Release 3.10.4 beta immediately.

2019-11-24
==========

Thanks to everyone who attended the sc-dev meeting! Minutes of the meeting are below. You can find archived minutes from all our meetings on our GitHub wiki page: https://github.com/supercollider/supercollider/wiki/Dev-Team-Meeting-Minutes

The next meeting is planned for the weekend of Nov 30 / Dec 1. A meeting time poll will be sent out early in the week. If you'd like to attend but our usual meeting times aren't good for you, respond to this thread or email me privately and we'll try to work something out! We are always interested in getting new people involved in the development community.

Regards,

UR_NAME

3.10.3 Release board: https://github.com/supercollider/supercollider/projects/17

Future Release Board: https://github.com/supercollider/supercollider/projects/15

sc-dev Meeting DATE Minutes:

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠

sc-dev meeting 11-24

James S, Josh, Nathan, Patrick, Brian, Marcin, Tejaswi

Brian built an IKEA shelf

4214 - James S - after a lot of digging it looks like something with Boost ASIO dropping requests. IPC wasn’t getting established. PR 4646 - a modification made for a synchronous read step happen for setting the group policy for auditing removable devices it fixed the issue every time. BUT - if it is something else ??? - lots of concern about why the initial reads are lost - but, maybe it doesn’t matter. 

Document it?

4368 - James has some new info. Sound card / Port Audio?

3.10.4 diversion - out before end of year / holidays

3132 -  CI says latest PR passes, but Patrick says it does NOT. 
Top level YAML file is ok - but we need to send an error back to the calling script.
Probably an issue in qpm
On linux - server boots and runs the tests. But some tests don’t get run - hangs on TestNoOps. And ditches the rest. Test on local machine first to see if it works, then see if it can be fixed on Travis.
Maybe only run server tests on linux?
Shouldn’t hold up release.


4645 - ready to go, but solves the most serious issue. Josh and Brian will look tonight.

3.11 - Link is the big feature.
Nathan would like some manual QA
Look at API design

3.11 alpha at the same time as 3.10.4 and ask people to start testing it more?
Linux jack timing

https://github.com/supercollider/supercollider/pull/4599 for 3.10.4? Voted down - on to 3.11!


Manage 3.11 board for 4484 and Link

James S - Soundfile view issue - possible threading issue. The way it talks back to the Qt widget seems to lock the whole GUI.
As loading the sound file, something can hang the GUI thread. Will try to create reproducer.

Brian - all - try to tackle some SC only PRs if we have the time!

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠


2019-11-17
==========
Thanks to everyone who attended the sc-dev meeting! Minutes of the meeting are below. You can find archived minutes from all our meetings on our GitHub wiki page: https://github.com/supercollider/supercollider/wiki/Dev-Team-Meeting-Minutes

The next meeting is planned for the weekend of Nov 23-24. A meeting time poll will be sent out early in the week. If you'd like to attend but our usual meeting times aren't good for you, respond to this thread or email me privately and we'll try to work something out! We are always interested in getting new people involved in the development community.

Regards,

Josh

3.10.3 Release board: https://github.com/supercollider/supercollider/projects/17

Future Release Board: https://github.com/supercollider/supercollider/projects/15

sc-dev Meeting DATE Minutes:

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠

SC-Dev meeting 11-17

Nathan, Iannis, James S, Tejsaw, Brian, Patrick, Josh


4368 - decide next week if it stays in 3.10.4

Consider what for 3.10.4, think for 3.11 while considering 3.10.5

Nathan - update change log today

4124 - James S - maybe not an IPC issue? From the IDEs point of view it is writing to standard input - no errors reported. But the language process is NOT seeing anything on STDIN. So, the IPC never gets kicked off. Really hard to follow up - Nathan has shown that his python script probably shows it is IDE related (since sclang talks listens from python ok).

Probably something wrong with QProcess

Maybe don't subclass QProcess?

Another possible move to 3.10.5

3132 - Patrick

Some good progress, but feeling like he isn't moving forward. Server tests on Travis still don't work. Might leave server tests for another day. 

Removed common tests. Have included the test suite in the repo. QPM now runs the tests in the repo. 

Might do server tests (at least on one platform) for next release.

4363 - consensus on how to fix the crash - Nathan will do a pull request.

Josh - lots of code-signing progress, still trying to get to unsigned binary plugins.

3.11 - Abelton Link should be main new item.


Brian - talked with Andrew Beltz - works for VCV Rack (creator?). Prototyping thing that lets people write code with various scripting languages. Looking for someone to help with sc backend for prototype repo. Any interest?

Also - Brian wants his PRs merged. 4585 is merged, 4612 will be rebased to 3.10


Patrick would like someone to review:
PR 4643 Server related fixes for some UnitTests
PR 7 in supercollider-quarks repo
PR 4598 Classlib: Buffer:write should use Buffer:writeMsg

Discussed possible future improvements to UnitTest: fixtures, mocks, etc.

Talked about GitHub Actions:
- general feeling - no compelling reason to use it now, but could research it more

For next meeting:
- plan to put together a list of issues and PRs for 3.11

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠





2019-11-03
==========
Nov 3rd 2019




SUBJECT: sc-dev Meeting Minutes
Hey all,

Thanks to everyone who attended the sc-dev meeting! Minutes of the meeting are below. You can find archived minutes from all our meetings on our GitHub wiki page: https://github.com/supercollider/supercollider/wiki/Dev-Team-Meeting-Minutes

The next meeting is planned for the weekend of Nov. 9th, 2019. A meeting time poll will be sent out early in the week. If you'd like to attend but our usual meeting times aren't good for you, respond to this thread or email me privately and we'll try to work something out! We are always interested in getting new people involved in the development community.

Regards,

Josh

3.10.4 Release board: https://github.com/supercollider/supercollider/projects/17

sc-dev Meeting DATE Minutes:

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠

Present: Patrick, Brian, Clare, James S, Nathan Ho, Marcin, Iannis

Intros - welcome Clare!

Check out includecpp.org

3.10.4 board
3132:
Patrick will be pushing a branch for 3132. Can server tests run on Travis? It may work on Linux.
- may have a linux way to test
- maybe OS X?
- Is there a ‘user’ logged in with the images on Travis?

Brian will bring QPM into the org

4214:
James - ‘This is a bit of a monster’. Has had some time to look into it.
Nathan has insight into IPC between lang and sc-ide
Not a good idea to subclass QProcess … which we’ve done. It owns a NULL pointer to the IPC client in sclang. When sclang boots it fires a connect cmd. Then the IPC gets initialized and the client connects to the server on the QProcess. Signal and slot set up that registers and sets up the two way communication. When the variable gets set that triggers the issue, there is no IPC client attached. It doesn’t see that sclang has tried to connect to it.
Find a way to start VS when lang starts? Really hard to debug. Attach to process by name in VS?
Keep in the 3.10.4 board.

4368:
Maybe language related? Or - can we discount it for now?

4533:
Add to Brian’s to-do

4363:
Number 1 on Brian’s to-do. Hopefully next week.


Brian update: Preparing for and taking a vacation. Now he’s back. Maintainer tasks, mostly.

4631 - approved, Brian will merge / push

RFC 1 - support for OS’s / systems and setting up CI to show support it.

Qt tends to be a limiting factor. Other / home-brew limitations may be an issue.

Josh to comment about past support. Nathan as well will soon

RFCs to review
https://github.com/supercollider/rfcs/pull/1
https://github.com/supercollider/rfcs/pull/4

Anyone not in the meeting who can review, please do!


Qt - ask on hash include discord about Qt mic input

Clare - initial testing progress:

PR in progress that needs some rebasing. 
- builds sc-ide as a static lib
	- this lets us set up a minimal test framework so anyone who wants to add tests can do so.
- branch sc-ide-test-experiments in test suite/editors/sc-ide … (will be pushed later)
- Showed her initial setups.
- Brian thinks these can be ported into a different test framework. Perhaps commit 'catch.h' into the external part of the repo. James has used it in his personal projects, and says it is amazing.
- some licenses questions?


Josh to post notes about Mac OS notarization.

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠



2019-10-27
==========

SUBJECT: sc-dev Meeting Minutes
Hey all,

Thanks to everyone who attended the sc-dev meeting! Minutes of the meeting are below. You can find archived minutes from all our meetings on our GitHub wiki page: https://github.com/supercollider/supercollider/wiki/Dev-Team-Meeting-Minutes

The next meeting is planned for the weekend of WEEKEND_DATES. A meeting time poll will be sent out early in the week. If you'd like to attend but our usual meeting times aren't good for you, respond to this thread or email me privately and we'll try to work something out! We are always interested in getting new people involved in the development community.

Regards,

Josh

3.10.4 Release board: https://github.com/supercollider/supercollider/projects/17



sc-dev Meeting 10-27-2019 Minutes:

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠

Attending - Patrick, Josh, Marcin, James S, Iannis

3.10.4 - 
3132 - Patrick - quarks package manager to run tests - JSON in root or repo to run tests by QPM, right now those scripts pull those quarks into the tests.
JSON lets you skip tests
1st step - not install common test quark, and just make JSON to include all tests that currently are installed. All server boot needed tests can be skipped. Make a lists of tests that we want to run in Travis - might be a good first step for now. 
Figure out how to run tests that do boot the server for the future. Maybe in Docker?
Branch and have Travis build the branch

4214 - new comment, but there are a couple separate things for that. James has been busy with his Ph.D. (submitted on the 18th!). Hasn’t had time otherwise. Will look this week.
Group policy settings may have an effect, but there is a specific one that seems to be a good test. Command line is a known issue - readline prevents proper usage.

4368 - Geoffrey - windows tickets not working. Maybe related to 4214? James has  gut feeling that they may be.

4278 - Josh needs to test and we can pull this in.

4533 - Need Brian to sign off on linting change. If Brian can’t., Josh will nudge it.

4363 - Follow up with Brian and Nathan.

Signed SC maybe? Notarization may not work with sc3-plugins. Windows may have an issue with this as well? James S - maybe Steinberg can help - they’ve had similar issues. Is it viable for external plugins to have them by default?

Iannis and Josh to talk more about Server and Multi-Server classes

Josh to write up multi-server approach

Jack and Linux issues

Add https://github.com/supercollider/supercollider/pull/4599 to 3.10.4?
Josh and Brian (Josh volunteered Brian) to also look at this.

⚠ If you have any comments on topics in these meeting minutes, please start a new thread rather than replying to this one. ⚠





2019-09-22

Members Present: James Surgenor, Nathan Ho, Brian H, Patrick D, Josh P, Marcin P, Tejaswi Prakash

These notes were not taken at the meeting - apologies - but I believe this is a good summary (Josh P)

- RFC proposal will be finalized for next week's meeting (as a goal)
- Reviewed 3.10.4 release board
- Discussed possible release dates. We want to hear back from a couple people assigned to tasks at the next dev meeting then decide. But we're targeting 10-15 for a beta.
- Items on board are the ones we want to attempt to get in (we see this as our goal for a release). Other PRs / issues can be included as we see fit.
- Discussion about possibly pulling plugins out of sc3-plugins for self-hosted solutions. Brian will do some cleanup on cookie-cutter, and a couple people will look into pulling their plugins out to encourage others to do so (Josh and ???)

*** NOTES were written very much after the fact … others mostly agreed with this summary. If anyone else was on the call and has additions or suggestions, please let us know ***

2019-08-25
=========

Members Present: Iannis Zannos, James Surgenor, Nathan Ho, Tejaswi Prakash

Slow week, no real updates on the release. Only change is that Nathan put the wrong pull request on the board: meant to put https://github.com/supercollider/supercollider/pull/4510 (Plotter horizontal resize bug) rather than https://github.com/supercollider/supercollider/pull/4511 (Plotter default colors). He has rectified this error.

Iannis is interested in reworking the server boot logic (https://github.com/supercollider/supercollider/issues/3286) and clarifying some of the finer points of the server initialization process (e.g. creation of default group, loading synthdefs, etc).

2019-08-18
==========

Members present: Brian H, Nathan H, Marcin P, Patrick D, James S

SC 3.10.3-rc1 is out!

Todo issues for 3.10.3-rc2:
- https://github.com/supercollider/supercollider/pull/4511 ("Plotter: update default colors to valid colors."), which fixes a regression introduced in an earlier 3.10 release.
- Code signing - still in progress
    - Josh P has successfully codesigned the 3.10.3-rc1 app package, but an issue with codesigning server plugins also needs discussion and investigation

Nathan suggested we should continue with the 3.10 release series in 3.10.4: "I want there to be a stable version of 3.10 that people can use for a long time"

Nathan suggested that since we were able to solve all 6 items on the release board relatively quickly for 3.10.3, we should shoot for 6 for the 3.10.4 release.

We spent some time discussing which items should be in the 3.10.4, 3.11, and Future Release boards.

Marcin will review and rework his PRs in a few weeks when he is done traveling.

Brian brought up the PRs opened by Christof R for his VSTPlugin UGen (#4499, #4379) and wants to prioritize them. Some concerns were raised about #4499, mainly about maintainability. Patrick was concerned that we should not be too quick to introduce a feature that may become broken due to project decay in the future. We agreed to continue discussing it, but not unduly delay the PR since it is a project we want to support.

Nathan suggested that after the 3.10.3 release we could propose an RfC process. His initial concern is that many RfCs will be submitted at once and it will be overwhelming to prioritize and discuss them. We discussed some ideas: "first come first served", cap on active number of RfCs, use "active" and "final review" states to indicate which RfCs are currently prioritized. We agreed post-3.10.3-release would be a good time for Nathan to propose it.

James S talked a little bit about his SuperDiffuse project.

2019-08-10
==========

Members present: Brian Heim, Iannis Zannos, James Surgenor, Marcin Pączkowski, Nathan Ho, Tejaswi Prakash

Release updates:

- Josh's macOS codesigning efforts are not required for 3.10.3 and are therefore deferred due to the use of manual release
- Marcin's pull request is basically done! Awaiting James Harkins' OK on some minor changes

New item added to future release:

- macOS interpreter crash on cmd+q https://github.com/supercollider/supercollider/issues/3824

Although there are some high-priority tasks remaining, we decided against adding ANY new things to 3.10.3 largely for psychological reasons -- this release has been seriously delayed and it is unnecessarily stressful to drag it out further.

Nathan organized the slew of issues in the past few years concerning the help browser and organized them into a board. He closed all issues related to the Linux JavaScript error because, to our knowledge, this is a downstream issue with the Ubuntu packaging.

There were some recent merges which violated the process that Brian had laid out for reviewing. (This was Nathan's doing and he really needs to read the damn reviewer guide haha)

For some reason all reviewers also have write access to the SuperCollider repository, which seems wrong...

Brian believes that in a 3.10.x release, there was a change in CI that downgraded Qt 5.11 to Qt 5.9 and the consequences of it were not properly thought through.

Iannis discussed some of the design issues with NotificationCenter and has a new class, Notification, that he'd like to introduce to the core class library. He will send an email to sc-dev to propose this new change.

Nathan brought up the recent resurfacing of pre-sample initialization and sample-accuracy in SC's core UGens. Unfortunately this is a really, really difficult problem for several reasons: it will take considerable effort and will likely break backward compatibility -- in minor ways for users that don't care about it, and in potentially major ways for users who have used workarounds in their SynthDefs.

Soon, we should discuss a Request for Comment process and a reshuffling of permissions issues in the SC organization.

The roadmap for 3.11 and 3.10.4 will be discussed in a future meeting.

2019-08-04
==========

Members Present: Brian Heim, Geoffroy Montel, Iannis Zannos, James Surgenor, Luke Nihlen, Marcin Pączkowski, Nathan Ho, Patrick Dupuis, Tejaswi Prakash

The Backlog Board is hereby renamed to the Future Release Board (but still usually referred to as the backlog).

Some discussions on the structure and process:

- We discussed including the backlog *in* the Release Board, but decided against since the purpose is to create focus and avoid distraction. 
- The decision process for adding, removing, and prioritizing items (especially across different communication channels) is not very clear due to the SC community's lack of a clearly defined leadership model.
- By a quick straw poll, we decided that it's easier if the Release Board has issues in "To Do" but are replaced with PRs as soon as a PR exists.
- The release manager has to leave the process open and democratic but is responsible for watching the process and making the tougher decisions that nobody else wants to make.

3.10.3 Release Board updates:

- macOS code signing: Josh (not present) made good progress in the past few days, not far off.
- WebSocket port selection: Nathan handed it off to Brian yesterday. Essentially done, just needs a final review and merge.
- windows audio devices: Very close, some testing from Windows users is wanted.
- network sockets: Luke gave some feedback, awaiting Nathan.
- Cmd+Q: Luke reviewed. Tested on macOS and Windows, but not Linux.
- Optional QtWebEngine: DONE!

Out-of-board updates:

- Iannis received reviews on NotificationCenter help file updates and will be responding to them.
- James looked into finding the best way to properly detect and set the SSE instruction set in compiling.
- Marcin brought up matching partial device names in Windows.

New items added to backlog:

- LinkClock quantum handling and sync https://github.com/supercollider/supercollider/pull/4484
- supernova lockup on dsp helper thread https://github.com/supercollider/supercollider/issues/3461
- supernova sound input failure https://github.com/supercollider/supercollider/issues/4029
- UnitTests do not run on CI https://github.com/supercollider/supercollider/issues/3132

2019-07-28
==========

Members Present: Geoffroy Montel, Iannis Zannos, Josh Parmenter, James Surgenor, Marcin Paczkowski, Nathan Ho, Patrick Dupuis, Tejaswi Prakash

Updates:
- Iannis submitted a pull request on NotificationCenter. Iannis is also interested in investigating an issue he's having with remote server.
- Patrick responded to James' code review on HelpBrowser.instance.
- James did some code review work and started looking at Marcin's Windows I/O device pull requests and added a denormal. He noticed a bunch of deprecation warnings with new Qt.
- Marcin responded to Brian's feedback for Windows I/O devices, dependency/dependancy documentation question.
- Geoffroy fixed cmd+Q issue on macOS.
- Josh dug into the macOS signing issue and has been sketching out ideas for multicore scsynth.
- Nathan reorganized the project docs and investigated a dangerous security configuration in scsynth.

We discussed the network security issue in scsynth and supernova (https://github.com/supercollider/supercollider/issues/4496). Despite the fact that fixing it properly involves the addition of a new feature and a minor breaking change, it is important enough that it should go in 3.10.3.

Josh discussed multicore scsynth.

We discussed the newly proposed backlog and release boards and how to keep the process of maintaining these boards efficient (using dev meetings) and inclusive (allowing people who aren't on dev meetings or slack).

Nathan demoed a fun delay UGen.

We discussed the QtWebEngine PR. James brought up QTextBrowser https://doc.qt.io/qt-5/qtextbrowser.html as an interesting alternative to QtWebEngine. 

2019-07-21
==========

Members Present: Geoffroy Montel, James Surgenor, Marcin Paczkowski, Nathan Ho, Patrick Dupuis, Tejaswi Prakash

Updates:

- Geoffroy is still working on the Cmd+Q bug on macOS.
- Patrick tested out the WebEngine PR on both his laptop and RPi, made a pull request #4488 (fixing an error in HelpBrowser.instance in sclang), and updated #4473 (Linux README).
- Marcin is working on the feedback that Brian gave him on the PortAudio device selection PR.
- James hasn't done anything but hopes to help with Marcin's work this week.
- Nathan worked on moving the project docs to the wiki.

We discussed the maintenance status of sc3-plugins.

Nathan suggested the idea of a "backlog board" containing a list of issues of interest, ordered by priority, which is regularly cleaned up.

2019-07-14
==========

Members Present: Patrick Dupuis, Nathan Ho, Geoffroy Montel, Marcin Pączkowski, James Surgenor

Geoffroy worked on fixing the Cmd+Q problem on macOS but has not yet been successful in debugging it (#4300).

Following last week's discussion, Marcin split his huge PR into a bunch of smaller PRs and will be responding to the code review Brian gave in #4475.

Patrick tested #4267 (SCIDE crash when opening up a second simultaneous instance, JavaScript errors when running HelpBrowser outside the IDE). He's been investigating HelpBrowser in command line sclang, but #4267 doesn't fix it. He also went through the guide on the wiki for building SC on Fedora and updated it.

James has been working on fuzzy array comparisons pull request.

3.10.3 drags on. The set of changes in the changelog is not particularly substantial, but code signing issues on macOS *are* potentially urgent enough for 3.10.3. We also discussed similar permissions-related issues on Windows, which Geoffroy has been looking into (https://github.com/supercollider/supercollider/issues/4368).

Nathan is halting the RFC proposal until 3.10.3 is out.

2019-07-07
==========

Members Present: Patrick Dupuis, Brian Heim, Nathan Ho, Marcin Pączkowski, Iannis Zannos

- Brian hasn't done much
- Nathan fixed bugs in the QtWebEngine PR and did some standard custodial work
- Marcin has been working on the Windows audio driver PR and has been dealing with a long string of issues.
- Patrick did some cherrypicks, redid a stalled PR, and tried out the WebSockets one

Marcin has been working with fixing Windows audio drivers on scsynth and supernova (https://github.com/supercollider/supercollider/pull/4009). Some concern was expressed about the overwhelmingly long comment thread, and scope creep happening in the pull request itself, and we agreed to break it down to separate pull requests to make things easier for reviewers and deferring some of the trickier changes to 3.11 rather than 3.10.3.

Iannis is interested in getting started with SuperCollider development and will be looking at the "good first issues" tag to file his first pull request. Iannis also noted some frustrations with remote servers and poor design of Synth class and Event.

Nathan expects to get a working version of the redesigned website in the next week.

Brian is interested in nailing down the project docs (at Mike McCrea's suggestion). We discussed moving them all to the SuperCollider wiki for better unification.

2019-06-30
==========

Members Present: Josh Parmenter, James Surgenor, Luke Nihlen, Nathan Ho, Patrick Dupuis, Marcin Paczkowski, Brian Heim, Tejaswi Prakash

We discussed a potential new RfC (request for comments) process [https://github.com/snappizz/rfcs]: when to introduce, how to introduce, requirements for RfC submitters, and how RfCs should be announced. 

We discussed some future organizational concerns: project permissions levels and fragmented discussion venues. There are many places we can discuss SC (sc-users, sc-dev, Discourse, Slack, Skype, GitHub, Facebook), and sometimes knowing where to discuss what is not easy.

Some felt a problem with the forum is that very few developers are using it. In that way, it made the fragmentation worse. We had general agreement that lack of searchability for the mailing lists has reduced their usefulness. General agreement that GitHub, sc-dev, and Slack combined seem to make a good combination of tools for developer collaboration.

Discussion then focused on how we use sc-dev vs. GitHub. General agreement that "goal-oriented" discussion should happen on GitHub. Some felt sc-dev should be seen as a forum for asking and answering development-related questions, reaching out to third-party clients, and announcing important activity. We discussed how to do that when the topics are more "meta" level. A few people remarked using the Core Team discussion area did not seem very inclusive; Luke suggested using GitHub issues, general agreement this was a good option.

After that, we discussed good places for user support discussions. General agreement that if something rises to the level of a bug report or feature request, it should be on GitHub.

Some expressed a desire to focus less on organizational discussions and more on development work for a while, until 3.10.3 is released.

2019-06-15
==========

Members present: Brian Heim, Calvin Yung, James Surgenor, Josh Parmenter, Luke Nihlen, Marcin Pączkowski, Tejaswi Prakash, Nathan Ho, Patrick Dupuis

Most number of people we've ever had on a call! Wow!

Top priority pull requests for 3.10.3:

- Separating input and output devices on Windows https://github.com/supercollider/supercollider/pull/4009
- Fixing WebChannel related errors https://github.com/supercollider/supercollider/pull/4267
- Making QtWebEngine optional https://github.com/supercollider/supercollider/pull/4328

On the topic of making QtWebEngine optional, we discussed how the ability to run code from the help browser is just a nicety, and has the development overhead of requiring two editors.

We discussed a few fun hypothetical UI/UX improvements to scide. These include:

- colors + text formatting in the post window
- Programmatic access to all UI elements in scide from the language.
- Toolbar buttons for running code and entire file.

Josh brought up multicore support for scsynth. The first step is to the waters by evaluating the feasibility of such support and running performance benchmarks on each server. We need to be careful that the reverence for supernova is based on hard data, and not a halo effect where we assume that supernova is good because multicore = faster.


Luke noted that a review of the academic literature on supernova demonstrates somewhat different goals from scsynth. scsynth is designed to minimize latency, supernova for thoroughput. In particular, memory locking is a nondeterministic process, which directly violates scsynth's design philosophy. The impact (to my understanding) is that supernova is really performant on a good laptop or desktop machine, but sacrifices reliability in environments such as RPi.

Optimization isn't just making something faster -- it's the progressive refinement of requirements.

Josh noted that multiple instances of scsynth running allows for a more stable approach to parallelism, which may be more in line with scsynth's design goals, so a possible area of focus would be providing good built-in support for that.

Brian noted that the project would also give us a good chance to clean up the scsynth code base and address some bugs. Ultimately the two servers can absorb each other's strengths.

The long term health of the project will benefit greatly by reducing the number of servers we're maintaining from two to one, and we'll start by assessing the best way to do that.

We discussed better timeboxing of the dev calls. Several of us are more than happy to talk for 2 hours or more, but we're going to keep it to 90 minutes from now on.

Brian has written up some documentation on PR review process so that newer contributors can participate. There are several procedures that Brian, Nathan, and Patrick have informally agreed on but were never written down, and this causes major problems when bringing new reviewers on board.

He brought up some concerns about how our project does not have any formal procedure for the delegation of write permissions.

Our idea is to stratify permissions as follows: 1. reviewers (can hit approve and request changes), 2. committers (can merge PRs). Historically we've been too eager to hand out committer privileges. This is problem not because we want to gatekeep, but because inexperienced Git users have a chance of making mistakes. Some on the call said that they would be more comfortable *not* having write access for fear of screwing up. Reviewer rights, however, should be handed out to many people.

Action items:

- Give write access to Marcin, who has been around for years.
- Write documentation for reviewers.
- Create two tiers of contributors: reviewers (handed out early and often), and committers (handed out after a period of months).

2019-06-02
==========

Members present: Brian, James S, Luke, Nathan, Patrick

The reformat is done! We're back in action!

Current task is to review our PR backlog and help people with the clang-format process. Rebasing is a bit tricky especially for git beginners, plus it has some minor bugs that we will need to help people work around. However, the number of PRs affected is finite.

This puts us on the road to 3.10.3. The most important PRs for this release are:

- Making qtwebengine optional: https://github.com/supercollider/supercollider/pull/4328
- WebChannel - fix crash opening a second IDE, fix JavaScript errors running without IDE: https://github.com/supercollider/supercollider/pull/4267
- HelpBrowser executes code twice: https://github.com/supercollider/supercollider/pull/4390

Patrick brought up the problem of inaccurate documentation in supercollider-quarks master repository, specifically the use of @ tags.

Luke investigated poor design of .asFloat and .asInteger: https://github.com/supercollider/supercollider/issues/4418 Their behavior is surprising and arbitrary: they return `0` when given incorrect syntax, they ignore characters at the end of the string (`"0fdsa".asFloat == 0.0`), and they don't support sclang literal features (`"0xfa".asInteger == 0`). However, unintended consequences of breaking backward compatibility is a real concern in the wake of Float:asString. Changing the failure behavior is particularly dangerous. Discussion on how to move forward remains inconclusive.

We did some early stage brainstorming of how the SC community can adopt an informal RFC process to finalize proposals in major project direction. In particular, we looked at the Rust RFC process: https://github.com/rust-lang/rfcs.

SC development is going to be a bit frenzied in the next two weeks while we catch up with the PR backlog and get in gear for 3.10.3. Once things are relatively stable, the timing is good to open a discussion about RFCs on sc-dev.

The process of proposing and adopting an RFC protocol is a bit chicken-and-egg, but it won't be an issue if the discussion is done in a way inclusive of all SC contributors whether or not they're on Slack or the dev meetings. We make a point of not finalizing any important/controversial decisions on these two platforms, since not everyone is comfortable using those and people are in different time zones. However, contributors who want a say in project decisions are expected to follow at least sc-dev and GitHub.

We had some discussion about upholding civility and ensuring psychological/emotional safety in the SC community.

2019-05-26
==========

Members present: Christof Ressi, Josh, James Surgenor, Luke, Nathan, Patrick

James Surgenor has a PR that fixes highlighted code execution in SCDoc #4390, later a Windows issue with the recordings directory #4420, and is struggling with a mysterious SCIDE issue #4413.

Christof Ressi has a pull request for the supernova architecture (#4379), we discussed some uncertainties with the future of supernova/scsynth. A good first step that would help that decision is implementing ParGroup support for scsynth.

The code reformatting is very close to done -- most of the remaining work is on tooling and documentation. Realistically it can be completed this week. We discussed the possibility of unfreezing the repository but the work on reformatting is so close to done that we agreed this is unnecessary.

Two related but separate issues should be discussed in the wake of what transpired in March: 1. the lack of a governance and leadership model in SC development, and 2. problems of tone/atmosphere in the SC community.

On the topic of governance, how do we establish important decisions that affect long-term health of the project? One approach that was discussed is a semi-formal RfC system. Nathan is interested in reviving his backburnered proposal to clip the audio output on macOS, using it as a guinea pig for a new RfC protocol.

Luke suggested using Code of Conduct enforcement as a way of dealing with tone in both the user and dev communities. SC's community is better than most other open source projects in this regard, but unfortunately the reality is that the user and dev lists still actively scare some people off. James noted the Csound community's approach to this -- a monthly "Administrivia" reminder sent by the list administrator.

Neither Luke or James had heard of the scsynth.org forums, so Nathan sent out a reminder of their existence. The forums and the Slack are linked in the SC README, but the website is still a mess and could do a better job of alerting the community to them.


2019-03-03
==========

Members present: Patrick, Brian, Nathan, Geoffrey M

Codebase reformatting:
- Brian wants to do this tonight/tomorrow
- Plan: merge Ableton Link PR before doing this (needs quick re-test of Brian's branch)

Date improvements PR (3259):
- discussed potential impact of changes
- decided to discuss on dev list

Patrick opened several PRs to improve sclang unit tests (4342-4346)

Float->String behavior:
- NaN gets printed as "nan" or "-nan" right now, this makes it hard to get a compile-string from it.
- discussed a few ways of fixing this ("Float.nan", "(0/0)")

Discussed post-survey thoughts and thoughts for next survey

Discussed Nathan's proposal about sc3-plugins

Nathan plans to contribute more effort to project tutorials/documentation

Patrick plans to contribute small bug fixes and updates to unit tests

2019-02-23
==========

Members present: Patrick, Brian, James H, Mark L, Nathan Ho

Ableton Link:
- James will make a PR (squashed) against develop of his new branch
- Additional testing? -> No, too much work
- Latency issues have been addressed
- Brian will try to review & merge before next weekend

Mark L:
- Looking into timing in ALSA MIDI implementation -- may be submitting fix sometime (next couple weeks)

PRs:
- 4324: let's document this way of keeping old things around

MIDI 2.0 & MPE:
- Could SC project ask for a copy of the spec?
- MPE might take some time to implement, no obvious way to do it

Survey:
- where to post results?
    - website
    - possibly a series of longer 'thoughts' post afterward

JITLib tests:
- Patrick is working on some basic tests for NodeProxy to add robustness in future changes

Testing:
- writing tests that wait is difficult
- Mark: think hard about how to make easy-to-use patterns in test framework
- marking requirements on tests

3.10.3:
- Nathan wants 2 PRs in before:
    - QtWebEngine PR
    - QtWebSocket

3.11:
- Could release as soon as Ableton Link PR merged

Documentation:
- Brainstormed ideas for how to tackle documentation/tutorials

2019-02-03
==========

Members Present:

Nathan, Brian, Patrick

Discussion Topics:
- 3.10.2
    - almost ready to release, just need to merge Brian's PR
    - plan: do rc ASAP, release 3.10.2 on Friday if no major issues
        - in the past, rcs have been useful, for example for 3.10.1 we got 3 issues in the first few days
- 3.10.3 release date set for 2 weeks after 3.10.2
- talked about organizing project documentation
    - how to balance things between wiki & CONTRIBUTING.md/DEVELOPING.md?
- Nathan: seems like SC doesn't use heavy vectorization for UGens with MSVC
    - because nova-simd doesn't make the correct check under MSVC
- survey: send out another reminder today, close survey in a week
    - publish a report & aggregated results at the same time (ideally, at most a week after close)
- git workflow: how to manage PRs where original author doesn't have much time to make changes
    - everyone is more or less in favor of helping each other out
- 25th-anniversary edition of SuperCollider should be released as a limited edition CD box set

2019-01-27
==========

Members present: Brian, Geoffroy, Patrick, Nathan

- Send out reminder for survey in one week, close in two weeks. Sent out a reminder email only to sc-dev, inviting SC educators to pass it on to students.
- Possible doc-a-thon for fleshing out Learn SC
- With the Menu memory leak in sclang, 3.10.2 needs to get out ASAP. Once MainMenu is fixed, release 3.10.2-rc1 TODAY, and 3.10.2 in a few days.
- Also sc3-plugins 3.10.1...
- Nathan has been working on automated tarball uploads
- Patrick brought up really bad CPU usage of PartConv even on moderate audio files (5 seconds), + poorly written API and missed opportunity for zero-latency partitioned convolution
- No current plans to merge VST plugin support into core -- current state as a 3rd party plugin seems pretty OK
- Ableton Link support is stalled and deprioritized for 3.11

2019-01-20
==========

Members present: Brian, Patrick, Nathan

- Nathan fixed the old editor themes issue
- Nathan has been tackling the WebSocket problems in SCIDE
- Brian has been working on whitespace formatting
- Brian documented how to use `git rebase` in CONTRIBUTING.md to help contributors' difficulties with it
- Brian fixed string/symbol lexing errors
- Nathan has been working on automated tarball uploads, optimized a new WIP compressor
- Patrick investigated Platform:helpDir
- Patrick fixed a bug in ServerOptions
- We released the user survey and spent like an hour watching the first 20 results roll in like we're watching ESPN

2019-01-13
==========

Members Present:

Nathan, Brian, Hanns, Geoffroy

Discussion Topics:

- Recent work on VST host support by Christof Ressi
- Limitations resampling quality in VDiskIn, PlayBuf
- Divergence between AudioClock and SystemClock: OSC bundles are not sample-accurate
- NRT mode with OSC socket
- SC on WebAssembly+WebAudio: the upcoming version of the WebAudio API will be much more stable in performance than the current one, so reliable real-time audio may be in reach
- Ability to query for the existence of a certain UGen via OSC messages
- Website redesign

2019-01-06
==========

Members Present:

Nathan, Brian, Patrick, Josh

Discussion Topics:

- 3.10.1:
    - decided to release after 4110, 4180, 4198, 4222, 4230
    - will do a release candidate so changes in 4180, 4191 (serial port related) can be tested on Linux & MacOS
    - will do a 3.10.1 release of sc3-plugins
    - planned release: Jan 13 (possibly earlier)
- recent PRs:
    - sc3plugins: new plugin PR (BFold)
- 3.10.2:
    - planned release: a month from 3.10.1 release
- 3.11:
    - no strong ideas yet, will talk after survey results come in
- user survey:
    - run it by the dev list for comments, then post it shortly afterward
- formatting:
    - Brian has been working on a formatting/linting branch, planning to run by the dev list for discussion

2018-12-01
==========

Members present: Brian, Edmond, Josh, Nathan, Patrick

At the current rate of development, 3.10.1 should be ready to go in a week or two.

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