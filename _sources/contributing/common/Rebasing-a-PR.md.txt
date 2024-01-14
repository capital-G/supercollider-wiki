(rebasing-a-pr)=
# Rebasing a PR

## Introduction

In the SuperCollider project, the accepted way to resolve merge conflicts in a pull request is by first *rebasing* onto the target branch, resolving any merge conflicts that arise during that rebase process, before merging of your PR into the target branch. Do not resolve merge conflicts via the GitHub interface or by merging the `main` branch into your local branch. This creates noise in commit history and makes it more difficult to perform other operations on branches later.

- Tip: See `git help rebase` for usage examples that include helpful graphical representations.
- Tip: Rebase has an interactive mode (`git rebase -i`) which will show exactly which commits will be applied to the new base, and the order in which they will be applied. This can be very helpful when you're not completely sure what the result of a rebase will be.

## Rebasing: making a clean merge

Suppose your work branch `topic/foo` was based on the `develop` branch (as is standard practice), and you’re ready to submit a PR. But suppose that since you started your work, the remote upstream`develop` branch has had new commits added to it, leaving your local `develop` (on which `topic/foo` is based) out of date. 

To avoid merge conflicts between your changes and the new changes added to the upstream `develop`, you should update your local `develop` branch to reflect the new changes, then _rebase_ your work branch _onto_ `develop` so that your changes are added (”replayed”) _after_ the latest changes to `develop`.

1. First, checkout and pull the latest version of `develop` from the upstream (remote) project to your local repo:

```shell
git checkout develop       # switch to your local develop branch
git pull upstream develop  # pull in upstream changes from the remote
```

2. Then, rebase. This will also checkout your `topic/foo` branch when you’re done.

```shell
git rebase develop topic/foo
```

You may choose to rebase interactively (`-i`) to see which commits will be applied to the new base, and the order in which they will be applied.

[Add a section at the end explaining more about interactive rebase?]

Now skip to [Completing a rebase](#completing-a-rebase) below.

## Rebasing with a branch other than `develop`

A may reviewer may ask you to rebase your PR onto a main version branch to, for example, expedite your PR getting into a release branch.

If your PR branch `topic/foo` is based on `develop`, you can take the commits unique to your branch and replay them *onto* the version (e.g. `3.13`) branch instead.

1. First checkout and pull the latest version branch from the upstream (remote) project to your local copy:

```shell
git checkout 3.13
git pull upstream 3.13
```

2. Then, rebase. This will also your `topic/foo` branch checked out when you’re done.

```shell
git rebase --onto 3.12 develop topic/foo
```

You may choose to rebase interactively (`-i`) to see which commits will be applied to the new base, and the order in which they will be applied.

[Add a section at the end explaining more about interactive rebase?]

Now see [Completing a rebase](#Completing-a-rebase) below.

## Merge conflicts

Before rebasing, git will show you a change list which you can examine to make sure it's correct before continuing. Git will stop if it encounters a merge conflict, and give instructions on how to resolve it and continue the rebase. You can read more about how to handle this situation [here](https://docs.github.com/en/github/using-git/resolving-merge-conflicts-after-a-git-rebase).

(completing-a-rebase)=
## Completing a rebase

After rebasing, you may find it helpful to display the pretty-printed commit log with `git log --oneline --graph --decorate` to make sure all is well.

When done, your local branch will be out of sync with your remote branch. You will have to resolve this by force pushing: 

```shell
git push --force origin topic/foo
```

- Tip: You can add the `-n/--dry-run` switch to see what this command will do without actually making any changes.
- Tip: If you realize later that you made a mistake with your rebase, it's always possible to go back to your previous local state using `git reflog`. [ADD EXPLANATORY LINK]

## Rearranging, combining commits or editing commit messages with `rebase`

This is not recommended for new git users. 

In `git help rebase` you’ll find a section, "Interactive mode", with extensive documentation on how to reorder and recombine commits. 

Also refer to the section on `--autosquash` for ideas on how to combine these features into a streamlined rebase-oriented workflow.

## Removing commits with `rebase`

**Note: this is an advanced procedure and might result in a messy git state, including lost changes. Consider making a backup copy of the branch before proceeding**. 

The general idea is to enter "interactive rebase" mode in git, remove commits that are not desired, resolve conflicts that occur in the process, then *force push* the local branch to the origin.

**Note:  `--force` pushing rewrites the commit history, so this should not be done with branches on which multiple people are collaborating.** (I.e. It’s ok if you’re the only one working on your branch).

1. Make sure you don't have any uncommitted changes. 
2. (Optional) Safety measure: make a copy of the current branch (e.g. `topic/foo`):

```shell
git checkout topic/foo         # your branch
git checkout -b topic/foo-copy # (optional) backup copy
git checkout topic/foo         # go back to your branch
```

1. We’ll want to view all of the commits that we want to edit/remove, *plus at least one before that*. To do that, we're going to look at a list of recent commits. For example, let's list the last 12 commits:

```shell
git log --oneline -n 12 --reverse
```

Make note which commit is *one before* the commits to be edited.

1. Rebase interactively starting from that commit before the ones to be edited. Here we rebase onto the *eleventh* commit from the `HEAD` (this assumes we want to make changes to some of the last 10 commits):

```shell
git rebase -i HEAD~11
```

Note, you can also rebase onto an older commit, just be careful not to change any of the commits that are not yours in the subsequent steps. 

This will open a text editor where you can edit the commit history (`vi` editor by default, here’s a [cheat sheet for vi](https://www.atmos.albany.edu/daes/atmclasses/atm350/vi_cheat_sheet.pdf). You’ll initially be in "command mode". Pressing `i` enters "input mode". `Esc` returns to command mode.

- Lines starting with `p` or `pick` will keep those commits.
    - This should be the case for all the commits before the ones you are editing (note that you need to have at least one on top that's unchanged, before you start removing desired commits).
- To remove the commits, either delete the line with the commit information altogether.
    - In command mode, navigate to that line using arrows and press `D` (capital), or enter insert mode (`i`) and change `pick` to `drop` or `d`. Do this for all of the commits you want to remove. Leaving empty lines is OK, they’re ignored.

The example result will look like this (with different commit SHAs/names):

```text
pick ecbd988dab supernova: use the `/error` messages to turn on / off the console printing (#5820)
# <possibly empty, deleted lines>
pick 62c95d7bd6 docs: fix SimpleNumber typo
pick a9d9979056 add additional info about recSampleFormat method options
```

If this looks correct, i.e. if we have at least one unchanged commit at the top and we have properly edited the commit history…

1. Save the changes in `vi` and exit it, which will trigger the rebase. 
    1. Press `Esc` to make sure you're in the command mode, then enter `:wq` (write quit) and press enter.

Git now performs the rebase. 

If some of the removed commits operated on the same file as following commits, there might be conflicts that need to be resolved. 

1. Check the history again:

```shell
git log --oneline -n 3 --reverse
```

The new history should look like this (for this example):

```text
0b51f02ce9 supernova: use the `/error` messages to turn on / off the console printing (#5820)
e6e9a6e5d2 docs: fix SimpleNumber typo
920a3d50df (HEAD -> topic/foo) add additional info about recSampleFormat method options
```

1. `--force` push the changes to your local branch to the remote branch on GitHub.

First, double check we are on the right branch:

```shell
git status
```

Which should print, among other things, `On branch topic/foo`.  Then force push:

```shell
git push -f
```

If all went well, the history of your remote branch on GitHub should now reflect your local revised commit history.
