## git-flow

SuperCollider takes inspiration from git-flow for its branching mode. You can read about this frequently used git methodology [here](http://nvie.com/posts/a-successful-git-branching-model/). The most important thing to know:

- Bug fixes and minor changes are merged into the current release branch (like `3.9`), and are incorporated into the next patch (3.x.y) release.
- New features and breaking changes are merged into the `develop` branch and incorporated into the next minor (3.x) release.
- Periodically (roughly every week), the release branch is merged into `develop` so that `develop` always has both the latest bug fixes and features.
- `main`, which is stable and only includes releases. Pre-releases such as alphas and betas are not included.

A "feature" is, generally speaking, anything that adds new functionality. Examples include a new class, a new public method, and a new parameter on a public method. Private methods (those beginning with `pr`) are not features.

A "bug fix" or "patch" is anything that improves an existing feature without adding new features. Examples include adding documentation, updating translations, and improvements to class or method implementations. The terms "bug fix" and "patch" are frequently interchangeable, except when referring 3.x.y releases, which are always called patch releases.

PRs to the release branch may contain a new feature if the feature is minor, and if implementing the patch without this feature would be inconvenient or impossible.

There is a set of [command-line extensions](https://github.com/nvie/gitflow) for git-flow; you may want to consider installing them if you contribute frequently. There is also a helpful [cheat-sheet](https://danielkummer.github.io/git-flow-cheatsheet/) by Daniel Kummer. Also consider installing GitHub's extensions for git, [hub](https://hub.github.com/).

Stable releases are marked using annotated tags on GitHub's "releases" page.

Contributions to the project may be done in topic branches either on the main repository or a contributor fork. Contributors with push access should never push directly to `develop`, `main`, or the release branches -- especially not `main`, which is the stable branch! We have put protections in place so that this is impossible to do accidentally. A feature branch name starts with `topic/` and then a very brief description of the branch's topic, e.g. `topic/sinosc-help`. We aren't strict about the naming conventions for topic branches, but consistency is appreciated.

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

The current release managers are Marcin Pączkowski (@dyfer) and Josh Parmenter (@joshpar).

When it is time to prepare a release, run the script in `tools/release/make_release.py`.

We generally follow this sequence of pre-releases prior to the official release. `N` is a sequentially increasing natural number (1, 2, 3...) which starts over at 1 for each step:
- `X.Y.Z-alphaN`, for minor releases, only if a lot has changed quickly and we know there are likely bugs we aren't aware of
- `X.Y.Z-betaN`, for minor releases, to find any new bugs we missed and catch any regressions
- `X.Y.Z-rcN` (release candidate), for minor and patch releases, to catch any regressions and ensure that the official release itself will go smoothly

### Tagging

Creating a release involves adding a tag on the tip of the main branch. We follow the convention of using `Version-` prefix for the tags intended for official releases, e.g. `Version-3.11.0`. Our CI uses the tag in the filenames of the release artifacts, but removes the `Version-` prefix. Please note that creating a tag without the prefix will also trigger deployment of release artifacts, which is useful for testing. In the regular workflow, tags are used almost solely for creating releases. One notable exception from this was adding tags before reformatting the codebase with `clang-format`.

### Versioning

The current version of SuperCollider is defined in the `SCVersion.txt` file. This is the only place where version number should be updated before the release etc.

Starting with [PR #5566](https://github.com/supercollider/supercollider/pull/5566), we are using a different version number on the current release branch and the `develop` branch. The minor version number on the `develop` branch should be one above the current release version and should include the `-dev` suffix. For example: if the current version on the `3.12` branch is `3.12.2`, the version on the develop branch should be `3.13.0-dev`. 

The version on the `develop` branch should be updated right after a new release branch is created. For example: after the `3.13` branch is created, the version on the develop branch should be changed to `3.14.0-dev`. The version on the `3.13` branch can stay as `3.13.0-dev` until the time of release, when it will be changed to e.g. `3.13.0-rc1`. 

Please note: this will cause a merge conflict _on the first merge_ from the given release branch (e.g. `3.13`) to `develop`. This conflict needs to be resolved before that first merge. Subsequent merges from the given release branch to `develop` should not trigger the merge conflict anymore.

### Emergency support releases

Rarely, we may need to do an "emergency release" for extra support. As of February 2021, this has only happened once since the project moved to its current git-flow branching model. The reason for doing so was to support macOS 11 Big Sur between the release of 3.11.2 -- which did not support Big Sur at all yet -- and 3.12.0. In a conversation [here](https://github.com/supercollider/supercollider/issues/5168#issuecomment-778898320), this was the particular process arrived at:

1. Assume the release to be patched is `x.y.z`, which, according to our branching model, has been developed on the release branch called `x.y`. Also assume that `x.y` has been merged into `main` at commit `A`, tagged `Version-x.y.z`, and that the parent commit of `A` on the `x.y` branch is `B`. In other words, `B` is the last commit on the `x.y` branch before merging into `main`.
2. From `B`, create a new branch called `x.y.z-Comment`, where `Comment` is a brief camel-case descriptor for the motivation for the emergency support release. In the case of the `3.11.2` emergency release for Big Sur, this branch was called `3.11.2-BigSur`. Push the new branch to the repository, still pointing to commit `B`.
3. Merge any necessary patches into `x.y.z-Comment` using the typical GitHub PR merge process. Let's refer to the merge commit created from this merge as commit `C`.
4. Create any necessary release artifacts from commit `C`. *Do not* make a permanent tag for this release, as such a tag could interfere with downstream packaging processes.
5. Name the artifact with this scheme: `x.y.z+Comment.SHA` (note the `+`!). `SHA` should be the first 7 digits of the hex SHA for commit `C`. We use a `+` here instead of `-` to conform to [SemVer's](https://semver.org/) requirements for labelling releases with build metadata. A secondary goal of adding these extra labels is to transparently show that the release artifact corresponds to a commit different than commit `A`, which was given the actual release tag.
5. Publish these artifacts on GitHub releases and the website download page, and announce the newly available artifact across all venues where the original release announcement was made. All announcements should clearly state that the artifact is a modified version of the official release patched for additional support, and should also transparently indicate the testing done prior to release.

## Conflicts between release branches and develop ##

Occasionally it may happen that a release branch cannot be cleanly merged into `develop`. In that case, the correct procedure is:

1. Create a new branch off `develop` with a name like `topic/merge-forward-3.x`
2. Merge the release branch into this new branch, resolving merge conflicts and creating a merge commit.
3. Create a pull request from the new branch against `develop`.

This allows the merge conflict resolution to be reviewed and treated like any other pull request.
