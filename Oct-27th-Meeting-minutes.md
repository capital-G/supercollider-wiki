Oct 27

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



