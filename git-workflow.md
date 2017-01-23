SuperCollider uses an unstable master branch. Stable releases are marked using tags, along with GitHub's "releases" page.

**Contributors with push access should never, ever push directly to the master branch.** Instead, create a topic branch (on your own repository or in the core repository) and file a pull request.

## Release mode ##

When it's time for a release, we enter "release mode." In release mode, the release manager creates a new branch (say 3.9) named after the version of the upcoming release. Uncontroversial bug fixes should be merged into the 3.9 branch, and everything else should go into the master branch. This causes the 3.9 and master branches to diverge, so the fixes in the 3.9 branch should periodically be merged into master to keep master up to date.