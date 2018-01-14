SuperCollider takes inspiration from git-flow for its branching mode. You can read about this frequently used git methodology [here](http://nvie.com/posts/a-successful-git-branching-model/). We use three major branches:

- `develop`, for bleeding-edge commits that will be incorporated into the next 3.x release
- The current release branch (like `3.9`), to which only bug fixes can be merged. (Features will occasionally be merged into release branches if they are considered critical for that release.)
- `master`, which is stable and only includes releases. Pre-releases such as alphas and betas are not included. (note: at the time of this writing [2017-09-12], master is not yet stable, but it will be when 3.9 is released)

There is a set of [command-line extensions](https://github.com/nvie/gitflow) for git-flow; you may want to consider installing them if you contribute frequently. There is also a helpful [cheat-sheet](https://danielkummer.github.io/git-flow-cheatsheet/) by Daniel Kummer.

Stable releases are marked using annotated tags on GitHub's "releases" page.

Most contributions to the project should be done in topic branches in contributor forks of the repository. **Contributors with push access should never push directly to `develop`, `master`, or the release branches -- especially not `master`, which is the stable branch!** We have put protections in place so that this is impossible to do accidentally. A feature branch name starts with `topic/` and then a very brief description of the branch's topic, e.g. `topic/sinosc-help`. We aren't strict about the naming conventions for topic branches, but consistency is appreciated.

When you file a pull request, GitHub gives you the option to allow contributors with write access to the main repository to push to the branch on your fork. This is a very good idea, and you should enable it on every PR you file provided you are comfortable with other maintainers pushing to your branch.

If desired, a feature branch can be made on the main organization repository instead of your personal fork. Typically, this is done when the branch contains a significant change of organizational interest, such as a fix for a major bug, an upgrade of a bundled library, a change to the CI or packaging system, a feature that solves a longstanding problem, and so on. Creating the branch here has a few benefits:
- the branch is easy to find and build
- SuperCollider's CI integrations apply to pushes to the branch
- the branch is protected from potentially being lost if a contributor deletes their fork

## Guidelines for pull request authors ##

**A good title and description in GitHub.** Code review is a drag. If you want your work reviewed and discussed in a timely manner, it's really important that you make things as painless and clear as possible for anyone who reviews your work. Even if your PR builds on prior discussions, you should recap for people who haven't been following along.

**Clean commit history.**

**Documentation (as necessary).** New features and behavior changes should be accompanied with documentation.

**Unit tests (as necessary).**

### Other tips ###

**Open PRs when they are truly ready for review.** The list of open PRs is intended to be the SC "workspace," the list of patches that are currently being worked on and discussed. Cluttering it with incomplete work makes the pull requests page overwhelming to look at.

**Break a large project into bite-sized chunks.** Several small PRs will get merged much faster than one big one.

## Releasing ##

A month or so before the beta release, the release manager branches off `develop` to create a new branch named after the release -- say `3.9`. Uncontroversial bug fixes should be merged into the `3.9` branch, and everything else should go into the `develop` branch. This causes the `3.9` and `develop` branches to diverge, so the fixes in the `3.9` branch should periodically be merged into `develop` to keep `develop` up to date.

The first thing to do in release mode is to remove the `SCClassLibrary/deprecated/3.8` directory and document these removals in the changelog. Corresponding UGen and primitive code should also be removed. Be careful when deprecating UGens and be considerate of alternate clients!

For each beta release:

- In the `3.9` branch, bump up the version in the top-level file `SCVersion.txt` from 3.9dev to 3.9.0-beta1 (or from 3.9.0-beta1 to 3.9.0-beta2, etc).
- Make sure the changelog is up to date.
- Run the [changelog to schelp converter script](https://github.com/supercollider/supercollider/blob/develop/package/changelog_to_schelp.sh) to get the "News in 3.9" help file up to date.
- Tag the beta release in git as (say) "Version-3.9.0-beta1."
- Create a release on the GitHub release page. Upload builds for macOS, Linux, and Windows.
- Do the same for sc3-plugins!
- Announce to mailing list, Facebook, etc.
- Merge `3.9` into `develop`. This will temporarily mess up `SCVersion.txt` in `develop`, but who cares, it's `develop`. **Do not merge prereleases into `master`! `master` is stable!**

For the release proper:

- In the `3.9` branch, bump up the version in `SCVersion.txt` to 3.9.0.
- Copy the changelog again and convert it to schelp if there were any new changes.
- Update the release history in `README.md`.
- Merge `3.9` into `master`, preferably with `git merge --no-ff`.
- Tag the release in git as "Version-3.9.0." Release on GitHub.
- Update the website download page.
- Announce to mailing list, Facebook, etc. Celebrate, bake a cake.
- Merge `master` into `develop`.

For patch releases, the process is the same. You can just keep around the `3.9` branch for all the `3.9.x` releases.

When you're done with patch releases, bump up `SCVersion.txt` in `develop` to 3.10dev.