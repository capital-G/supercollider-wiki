*Sorry about the disorderliness of this article. Project docs are undergoing some major restructuring right now. -NH 2019-07-26*

## git-flow

SuperCollider takes inspiration from git-flow for its branching mode. You can read about this frequently used git methodology [here](http://nvie.com/posts/a-successful-git-branching-model/). The most important thing to know:

- Bug fixes and minor changes are merged into the current release branch (like `3.9`), and are incorporated into the next patch (3.x.y) release.
- New features and breaking changes are merged into the `develop` branch and incorporated into the next minor (3.x) release.
- Periodically (roughly every week), the release branch is merged into `develop` so that `develop` always has both the latest bug fixes and features.
- `master`, which is stable and only includes releases. Pre-releases such as alphas and betas are not included.

A "feature" is, generally speaking, anything that adds new functionality. Examples include a new class, a new public method, and a new parameter on a public method. Private methods (those beginning with `pr`) are not features.

A "bug fix" or "patch" is anything that improves an existing feature without adding new features. Examples include adding documentation, updating translations, and improvements to class or method implementations. The terms "bug fix" and "patch" are frequently interchangeable, except when referring 3.x.y releases, which are always called patch releases.

PRs to the release branch may contain a new feature if the feature is minor, and if implementing the patch without this feature would be inconvenient or impossible.

There is a set of [command-line extensions](https://github.com/nvie/gitflow) for git-flow; you may want to consider installing them if you contribute frequently. There is also a helpful [cheat-sheet](https://danielkummer.github.io/git-flow-cheatsheet/) by Daniel Kummer. Also consider installing GitHub's extensions for git, [hub](https://hub.github.com/).

Stable releases are marked using annotated tags on GitHub's "releases" page.

Contributions to the project may be done in topic branches either on the main repository or a contributor fork. Contributors with push access should never push directly to `develop`, `master`, or the release branches -- especially not `master`, which is the stable branch! We have put protections in place so that this is impossible to do accidentally. A feature branch name starts with `topic/` and then a very brief description of the branch's topic, e.g. `topic/sinosc-help`. We aren't strict about the naming conventions for topic branches, but consistency is appreciated.

When you file a pull request, GitHub gives you the option to allow contributors with write access to the main repository to push to the branch on your fork. This is a very good idea, and you should enable it on every PR you file provided you are comfortable with other maintainers pushing to your branch.

If you have push access, creating the branch on the main SuperCollider repository has a few benefits:
- SuperCollider's CI integrations apply to pushes to the branch
- binaries of the branch for Windows and macOS will be available via our S3 hosting
- the branch is protected from potentially being lost if a contributor deletes their fork

## Deprecation

SuperCollider class library deprecations are currently made on a case-by-case basis using the `Object:-deprecated`
method. When a method or class is deprecated, it is moved to `SCClassLibrary/deprecated`. Deprecations are removed on a case-by-case basis with each minor (3.x) release.

## Milestones

We use four tags to keep track of issues:

- Next patch (example: "3.9.1")
- Some patch (example: "3.9.x")
- Next minor (example: "3.10")
- Some minor (example: "3.x")

Patch-milestoned issues are those that will require bug fixes, while minor-milestoned issues are things like new
features and major changes that are better left for a minor release. The "Next patch"/"Next minor" milestones mark those
issues that we've decided _must_ be addressed before the next respective release. They're either the most painful bugs
or most requested features.

When, in the example milestones above, 3.10 is released, we would move all 3.9.x-milestoned issues to 3.10.x,
and then collectively decide which issues ought to move from 3.x to 3.11 and from 3.10.x to 3.10.1.

## Guidelines for pull request authors ##

**A good title and description in GitHub.** Code review is a drag. If you want your work reviewed and discussed in a timely manner, it's really important that you make things as painless and clear as possible for anyone who reviews your work. Even if your PR builds on prior discussions, you should recap for people who haven't been following along.

**Clean commit history.**

**Documentation (as necessary).** New features and behavior changes should be accompanied with documentation.

**Unit tests (as necessary).**

### Other tips ###

**Open PRs when they are truly ready for review.** The list of open PRs is intended to be the SC "workspace," the list of patches that are currently being worked on and discussed. Cluttering it with incomplete work makes the pull requests page overwhelming to look at.

**Break a large project into bite-sized chunks.** Several small PRs will get merged much faster than one big one.

## Writing changelogs ##

The [changelog](https://github.com/supercollider/supercollider/wiki/Changelog) documents the publicly visible changes since the most recent SuperCollider release. A change is worth putting in the log if it affects users, such as breaking changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

The website [Keep a CHANGELOG](http://keepachangelog.com/en/0.3.0/) is a major inspiration for the organization of the changelog. Changes to each component of SuperCollider are subdivided into Added, Changed, Deprecated, Removed, Fixed, and Security, in that order.

Please provide the link to the PR with every entry in the changelog for easy navigation.

Try to exercise common sense in keeping the log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. In case of doubt, prefer inclusion over exclusion.

## Releasing ##

A month or so before the beta release, the release manager branches off `develop` to create a new branch named after the release -- say `3.9`. Uncontroversial bug fixes should be merged into the `3.9` branch, and everything else should go into the `develop` branch. This causes the `3.9` and `develop` branches to diverge, so the fixes in the `3.9` branch should periodically be merged into `develop` to keep `develop` up to date.

The first thing to do in release mode is to remove the `SCClassLibrary/deprecated/3.8` directory and document these removals in the changelog. Corresponding UGen and primitive code should also be removed. Be careful when deprecating UGens and be considerate of alternate clients!

For each beta release:

- In the `3.9` branch, bump up the version in the top-level file `SCVersion.txt` from 3.9dev to 3.9.0-beta1 (or from 3.9.0-beta1 to 3.9.0-beta2, etc).
- Make sure the changelog is up to date.
- Run the [changelog to schelp converter script](https://github.com/supercollider/supercollider/blob/develop/package/changelog_to_schelp.sh) to get the "News in 3.9" help file up to date.
- Tag the beta release in git as (say) "Version-3.9.0-beta1." **Double check the branch -- you should be tagging the commit on the 3.9 branch.**
- Seriously Nathan, you gotta check that branch. Don't goof it up!
- Run `./package/create_source_tarball.sh -v <version>` (where `version` is the version tag) to create a source tarball (including submodules). Optionally run the script with `-s <email-or-keyid>` (where `email-or-keyid` is a valid PGP key id of the release manager) to also create a detached PGP signature for the source tarball.
- Create a release on the GitHub release page. Upload source tarball (and optionally detached PGP signature) and builds for macOS, Linux, and Windows.
- Do the same for sc3-plugins!
- Announce to mailing list, Facebook, etc.
- Merge `3.9` into `develop`. This will temporarily mess up `SCVersion.txt` in `develop`, but who cares, it's `develop`. **Do not merge prereleases into `master`! `master` is stable!**

For the release proper:

- In the `3.9` branch, bump up the version in `SCVersion.txt` to 3.9.0.
- Copy the changelog again and convert it to schelp if there were any new changes.
- Update the release history in `README.md`.
- Merge `3.9` into `master`, preferably with `git merge --no-ff`.
- Tag the release in git as "Version-3.9.0." **Unlike the pre-releases, the branch should be `master`.** Release on GitHub.
- No really man, double check that branch.
- Run `./package/create_source_tarball.sh -v <version>` (where `version` is the version tag) to create a source tarball (including submodules). Optionally run the script with `-s <email-or-keyid>` (where `email-or-keyid` is a valid PGP key id of the release manager) to also create a detached PGP signature for the source tarball.
- Create a release on the GitHub release page. Upload source tarball (and optionally detached PGP signature) and builds for macOS, Linux, and Windows.
- Update the website download page.
- Do the same for sc3-plugins!
- Update [the Wikipedia page](https://en.wikipedia.org/wiki/SuperCollider)
- Announce everywhere - sc-users, sc-dev, Slack, Discourse, Facebook. (Reddit?) Celebrate, bake a cake.
- Merge `master` into `develop`.

For patch releases, the process is the same. You can just keep around the `3.9` branch for all the `3.9.x` releases.

When you're done with patch releases, bump up `SCVersion.txt` in `develop` to 3.10dev.

On release, post the changelog to the following announcement channels:

- CHANGELOG.md: post full version with all pull request links
- GitHub release page: post an abbreviated version
- "News in 3.x" helpfile: post full version without pull request links
- GitHub website: post an abbreviated version
- sc-users mailing list: post an abbreviated version
- Facebook group: post an abbreviated version
- Reddit (/r/supercollider): post an abbreviated version

## Conflicts between release branches and develop ##

Occasionally it may happen that a release branch cannot be cleanly merged into `develop`. In that case, the correct procedure is:

1. Create a new branch off `develop` with a name like `topic/merge-forward-3.x`
2. Merge the release branch into this new branch, resolving merge conflicts and creating a merge commit.
3. Create a pull request from the new branch against `develop`.

This allows the merge conflict resolution to be reviewed and treated like any other pull request.