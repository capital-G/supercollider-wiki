## Before making changes
See [Setting Up Your Development Environment](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment), to make sure you have a working and updated fork of SuperCollider's source code.
Then you can create a fresh new branch for your contribution:

## Create a topic branch
- Create a topic branch from where you want to base your work.
	- Your topic branch should be based on `develop`, unless it is a trivial bug fix or documentation change, in which case it should be based on the latest release (`3.x`) branch.
	- Our branch naming convention is `topic/branch-description`: for example, `topic/fix-sinosc` or `topic/document-object`.
	- To quickly create a topic branch based on develop: `git checkout -b topic/my-fix develop`.
	- Please do not work off of the `master` branch, which is stable and only includes releases.
- As time passes, make sure to keep your fork updated - see [Updating your fork](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment#2-Keep-your-fork-updated).

## Making changes

- Make commits of logical units.
- Please refer to [Code Style Guide](https://github.com/supercollider/supercollider/wiki/Code-style-guidelines). Note that code style, such as whitespace conventions, depend on the language (`C++` vs `SuperCollider` vs `SCDoc Markup`)
- [Commit message format](https://github.com/supercollider/supercollider/wiki/Commit-message-format): make sure your commit messages are descriptive and in the proper format, following the schema "category: content", e.g. `docs: Make the example in CONTRIBUTING imperative and concrete`, or `help: Update RunningSum2 help file`, or `class library: do this and that`, or `plugins: add missing function definition`.

- Make sure you have added the necessary tests for your changes. All changes to code should include a test which checks for correct functionality, including regression tests for bug fixes. Info on best practice for Unit tests is available at https://github.com/supercollider/supercollider/wiki/Unit-Testing-Guide
- Make sure you have documented your changes, if necessary.

## Submitting changes as Pull Requests

- Push your changes to a topic branch in your fork of the SuperCollider repository. If you are working locally, do this with `git push -u origin topic/branch-description`. `origin` should be the remote of your fork; check with `git remote -v`.
- Submit a pull request to the SuperCollider repository.
- The core team looks at pull requests on a regular basis in a public meeting that is held on a weekly basis. The meeting times are announced on the sc-dev mailing list.
- You may receive feedback and requests for changes. We expect changes to be made in a timely manner. We may close pull requests if they aren't showing any activity.

## Skipping CI

We have CI provided by AppVeyor (Windows) and Travis (Linux, macOS). If a commit changes _only_
non-schelp documentation, _without_ renaming, adding, or removing files, you may want to consider
adding `[skip ci]` to the commit message so it does not waste CI resources. See https://github.com/supercollider/supercollider/wiki/Continuous-Integration---Travis-&-Appveyor#skip-ci.

## Rebasing and merge conflicts

### Introduction

Do not resolve merge conflicts via the GitHub interface or by merging the main branch in locally. This creates noise in commit history and makes it more difficult to perform other operations on branches later. In the SuperCollider project, the accepted way to resolve merge conflicts in a pull request is by rebasing.

See `git help rebase` for `rebase` usage examples that include helpful graphical representations.

Rebase has an interactive mode (`git rebase -i`) which will show exactly which commits will be applied to the new base, and the order in which they will be applied. This can be very helpful when you're not completely sure what the result of a rebase will be.

### Rebasing to resolve merge conflicts in a PR

Suppose your current PR branch is `topic/foo`, which is based on an old commit from the `develop` branch. `topic/foo`
is the branch you want to rebase, and `develop` is the branch you want to rebase onto.

    # first pull any new changes from develop on the upstream project
    git checkout develop
    git pull upstream develop
    # rebase interactively (-i). this will also leave `topic/foo` checked out when done
    git rebase -i develop topic/foo

Now see [Completing a rebase](#completing-a-rebase) below.

### Rebasing to change the base branch of a PR branch

Suppose your current PR branch is `topic/foo`, which is based on `develop`, but you would like to rebase it on `3.12`
instead. In other words, you want to take the commits unique to your feature branch and replay them on the `3.12`
branch. This scenario can arise when you want to change a PR so that it targets a release branch instead of `develop`.

    # first pull any new changes from the release branch
    git checkout 3.12
    git pull upstream 3.12
    # rebase interactively (-i). this will also leave `topic/foo` checked out when done
    git rebase -i --onto 3.12 develop topic/foo

Now see [Completing a rebase](#completing-a-rebase) below.

### Completing a rebase

Before beginning to rebase, git will show you a change list which you can examine to make sure it's correct before
continuing. Git will stop if it encounters a merge conflict, and give instructions on how to resolve it and continue
the rebase.

After rebasing, you may find it helpful to display the pretty-printed commit log with `git log --oneline --graph --decorate` to make sure all is well.

When done, your local branch will be out of sync with your remote branch. You will have to resolve this by force pushing: `git push --force origin topic/foo`. You can add the `-n/--dry-run` switch to see what this command will do without actually making any changes. If you realize later that you made a mistake with your rebase, it's always possible to go back to your previous local state using `git reflog`.

### Rebasing to rearrange and edit commits

This is not recommended for those newer to git. `git help rebase`'s section "Interactive mode" has extensive documentation on how to reorder and recombine commits. Also refer to the section on `--autosquash` for ideas on how to combine these features into a streamlined rebase-oriented workflow.

## Additional resources

More information can be found on the [git workflow wiki page](https://github.com/supercollider/supercollider/wiki/git-workflow-and-guidelines).

You can also refer to Github's guide to [forking a repository](https://help.github.com/articles/fork-a-repo/) and to [syncing a fork](https://help.github.com/articles/syncing-a-fork/).

Instructions on adding translation files for the IDE can be found in the [Developer Reference](https://github.com/supercollider/supercollider/wiki/Developer-reference) (soon to be moved, please update that link when it does move...).
