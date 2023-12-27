#### Table of contents
<!-- TOC start (generated with https://derlin.github.io/bitdowntoc/) -->

- [At-a-glance PR checklist](#at-a-glance-pr-checklist)
- [Before making changes](#before-making-changes)
- [Branching model](#branching-model)
- [Creating a topic branch](#creating-a-topic-branch)
- [Making changes, managing commits](#making-changes-managing-commits)
- [Git commit message format](#git-commit-message-format)
- [Skipping CI](#skipping-ci)
- [Submitting your Pull Request](#submitting-your-pull-request)
- [Merge conflicts and rebasing](#merge-conflicts-and-rebasing)
- [How a PR moves from `develop` to release `3.x.x`](#how-a-pr-moves-from-develop-to-release-3xx)
- [How your PR fits into the release cycle](#how-your-pr-fits-into-the-release-cycle)
  - [Milestone tags](#milestone-tags)
  - [Turnaround time](#turnaround-time)
- [Additional resources](#additional-resources)
- [A note about `sc3-plugins`](#a-note-about-sc3-plugins)

<!-- TOC end -->

## At-a-glance PR checklist

The review of PRs is sped up tremendously by concise and well-structured PRs.

- [ ]  **Make a clean commit history.** The scope of your changes should be legible in your commit history.
- [ ]  **A good title and description.** Even if your PR builds on prior discussions, you should recap for people who haven't been following along.
- [ ]  **Documentation.** New features and behavior changes should be accompanied with thorough documentation.
- [ ]  **Unit tests.** Our future selves will thank you**.**

**Other tips**

**Open PRs when they are truly ready for review.** The list of open PRs is intended to be the SC "workspace," the list of patches that are currently being worked on and discussed. Cluttering it with incomplete work makes the pull requests page overwhelming to assess for Reviewers and authors!

**Break a large project into bite-sized chunks.** Several small PRs will get merged much faster than one big one.


## Before making changes

- If the changes are multifaceted or potentially contentious, consider whether it’s appropriate to first submit a [Request for Comments (RFC)](https://github.com/supercollider/rfcs) to discuss different approaches, side effects, or the implementation details.
- See [Setting Up Your Development Environment](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment), to make sure you have a working and updated fork of SuperCollider's source code. Then you can create a fresh new branch for your contribution.
- Familiarize yourself with the Review Process so you know what to expect after submitting your PR.


## Branching model

SuperCollider uses the [git-flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model. We use the `develop` branch for new features, deprecations, and breaking changes, and we use the current version's *\<major\>.\<minor\>* branch (e.g. `3.12`) for bug fixes for the next patch release (e.g. `3.12.x`) that have no chance of breaking anything. 

Documentation changes might go into either branch, depending on the timing in the release cycle and which documents are being changed. If in doubt, use the `develop` branch.


## Creating a topic branch

1. **Choose the branch** you will use as the starting point for your changes. The simple answer is to **use `develop`**.

<details>
  <summary>For a more detailed answer, click here</summary>
    Sometimes you can make your branch directly against the latest release branch (`3.9`, `3.10`, etc.). We prefer this when possible. First, check if the latest release branch is active. "Active" means that the next [milestone](https://github.com/supercollider/supercollider/milestones) is a patch version for that release. For example, if the next milestone is 3.15.0 but the latest release branch is `3.14`, use `develop`. If the next milestone is 3.15.2 and the latest release branch is `3.15`, use `3.15`. *If in doubt, just base your branch on `develop`. This is always a safe thing to do.*
</details>
    
2. **Choose your new branch name.** Our naming convention is `topic/` followed by a **_brief_** description of what your branch is about. For example, `topic/fix-sinosc` or `topic/document-object`.
3. **Create your branch.** To quickly create and move to a topic branch based on `develop`: `git checkout -b topic/my-branch develop`.

As time passes, make sure to keep your fork updated - see [updating your fork](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment#2-Keep-your-fork-updated).

[^Top](#table-of-contents)


## Making changes, managing commits

- Make commits of logical units.
- Please refer to the code Style Guides. Note that code style, such as whitespace conventions, depend on the language.
- [Commit message format](https://github.com/supercollider/supercollider/wiki/Commit-message-format): make sure your commit messages are descriptive and in the proper format, following the schema <br>
"component: sub-component: short description of changes".
See the following [subsection](#Git-commit-message-format).
- Make sure you have added the necessary _**tests**_ for your changes. All changes to code should include a test which checks for correct functionality, including regression tests for bug fixes. See the [Unit Testing Guide](https://github.com/supercollider/supercollider/wiki/Unit-Testing-Guide) for guidance and best practices.
- Make sure you have updated any documentation that is affected by your change, adding documents if necessary.


## Git commit message format

Git commit messages should consists of a one-line title, followed by an empty line, followed by the message body:

```
title

first line of body
second line of body
third line of body
```

This makes the message most expressive and comprehensible, and supports many git functions and graphical clients that treat the first line differently than the rest of the message. 

### Title

Message titles should have the following form:

`component: sub-component: short description of changes`

Great titles are short (70 characters or less), so as to fit in one line in most constrained circumstances.

The short description of changes should clearly and concisely state what the commit does, rather than describing the previous state or new functionality. E.g. “fix bug in X” instead of “there is a bug in X, and add X to settings dialog instead of settings dialog can do X”.

For example:

- `class library: ClassBrowser: fix search with empty query string`
- `docs: RunningSum2: update help file`
- `plugins: LFSaw: add missing function definition`

Look at previous commits in the repository for inspiration.

[_**TODO:**_ add a list of component tags]

### Body

The message body should describe the changes in detail and explain motivations behind them. The body is not always needed if the changes are few, and the title explains them enough.

The body should have *manual* line breaks at around 70 character.

A full example:

```
docs: Make the example in CONTRIBUTING imperative and concrete

Without this patch applied the example commit message in the CONTRIBUTING
document is not a concrete example. This is a problem because the
contributor is left to imagine what the commit message should look like
based on a description rather than an example. This patch fixes the
problem by making the example concrete and imperative.

The first line is a real life imperative statement which optionally identifies
the component being changed. The body describes the behavior without the patch, why this is a problem, and how the patch fixes the problem when applied.

```

[^Top](#table-of-contents)


## Skipping CI

We have continuous integration (CI) provided by AppVeyor (Windows) and Travis (Linux, macOS). If a commit changes *only* non-schelp documentation, *without* renaming, adding, or removing files, you may want to consider adding `[skip ci]` to the commit message so it does not waste CI resources. See https://github.com/supercollider/supercollider/wiki/Continuous-Integration---Travis-&-Appveyor#skip-ci.


## Submitting your Pull Request

- Push your changes to a topic branch in your fork of the SuperCollider repository. If you are working locally, do this with `git push -u origin topic/branch-description`. `origin` should be the remote of your fork; check with `git remote -v`.
- Submit a pull request to the SuperCollider repository.
- The core team looks at pull requests on a regular basis in a public meeting. The meeting times are announced on the [scsynth forum](https://scsynth.org/t/dev-meetings-schedule/250?u=mike) and on Slack.
- You may receive feedback and requests for changes. We expect changes to be made in a timely manner. We may close pull requests if they aren't showing any activity.


## Merge conflicts and rebasing

<!-- Note: This introduction is mirrored from the introductory statement of Rebasing a PR page, update both if changing* -->

In the SuperCollider project, the accepted way to resolve merge conflicts in a pull request is by first *rebasing* onto the target branch, resolving any merge conflicts that arise during that rebase process, before merging of your PR into the target branch. 

To avoid merge conflicts between your work branch and any new changes added to the upstream `develop` since you began work on your branch, you should update your local `develop` branch to reflect the new upstream changes, then ******rebase****** your work branch ****onto**** `develop` so that your changes are added (”replayed”) *****after***** the latest upstream changes to `develop`.

Details on rebasing, including reordering, combining, or removing commits, are found in the [[Rebasing a PR]] wiki.


## How a PR moves from `develop` to release `3.x.x`

Your PR will be cherry-picked (or, more commonly, rebased) from `develop` onto a release branch, `3.x.x`, according to the nature of the changes introduced and where we are in the release cycle.

As someone who contributes pull requests, you don't necessarily need to do the cherrypicking. The release manager or other Trusted Reviewer will often step up to do this. If you think something should be cherrypicked but hasn't, you're free to ping them. If you have familiarized yourself with the process, it's also OK for you to do it yourself.


## How your PR fits into the release cycle

See [[Releasing]] for detailed information on how SC milestones and versions branches are managed.


#### Milestone tags

The Reviewer will assign a release milestone to your PR, which determines where in the release cycle your changes will be merged into the main distribution.

Milestones help to prioritize your PR as well as identify where it fits most appropriately in the release cycle, given the scope of the change and how it relates other changes already positioned in the release cycle.


#### Turnaround time

The PR process varies depending on a number of issues: the size and complexity of the proposed change, Reviewer availability, responsiveness of the Author, to name a few. Everyone's time is valuable and we make best efforts to move the project forward.

**You're an active part of the process!** If you find that your PR has been sitting in waiting for a long time, your PR hasn't been intentionally ignored. Feel free to ping the PR Conversation to draw attention back to your PR.   Reviewers' availability fluctuates. There are also guidelines for Reviewers to assist in keeping review moving forward. For example, if a Reviewer becomes unavailable to follow through with your PR, another may be assigned to it to see it through.


## Additional resources

More information can be found on the [git workflow wiki page](https://github.com/supercollider/supercollider/wiki/git-workflow-and-guidelines).

You can also refer to Github's guide to [forking a repository](https://help.github.com/articles/fork-a-repo/) and to [syncing a fork](https://help.github.com/articles/syncing-a-fork/).

Instructions on adding translation files for the IDE can be found in the [Developer Reference](https://github.com/supercollider/supercollider/wiki/Developer-reference) (soon to be moved, please update that link when it does move...).


## A note about `sc3-plugins`

*New additions to the `sc3-plugins` project are currently suspended, pending a revision of third-party plugin distribution.*

The **merge process** described above is slightly different for the [sc3-plugins project](https://github.com/supercollider/sc3-plugins).

See [Releasing: A note about `sc3-plugins`](https://github.com/supercollider/supercollider/wiki/Releasing-Cycle-and-Process#a-note-about-sc3-plugins) for details.

[^Top](#table-of-contents)