### Table of Contents

* [Get the latest sources](#get-the-latest-sources)
* [Working with submodules](#working-with-submodules)
* [Update local repository](#update-local-repository)
* [Commit \+ Push](#commit--push)
* [Branches](#branches)
* [A common git workflow for development work on SuperCollider](#a-common-git-workflow-for-development-work-on-supercollider)
* [Common git commands](#common-git-commands)
* [Problems with submodule state update](#problems-with-submodule-state-update)
* [Testing mailing list patches](#testing-mailing-list-patches)
* [Resources](#resources)

Created by [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go)

## Get the latest sources ##

To work with SuperCollider's source code, you first need to create your own local clone of the online *repository*. There are two options:

* If you are going to push changes back to the GitHub repository do:

    ``git clone --recursive git@github.com:supercollider/supercollider.git``

* If you don’t have a GitHub account or you don’t intend to push changes (so will instead be contributing via patches or pull-requests), then use read-only access:

    ``git clone --recursive git://github.com/supercollider/supercollider.git``

The `--recursive` flag is required to also download all the *submodules* used by the repository.

## Working with submodules ##

This project uses [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) to manage third-party dependencies (Ableton Link, yaml-cpp, etc.) and subprojects. By default, when you switch branches or commits, git does not update the state of submodules, which may cause build failures and nuisances such as directories containing submodules showing up as untracked or modified in `git status`. You can resolve this by running `git submodule update --init --recursive`. However, there are ways of making things simpler.

### Auto-update of submodules using git config

The following command will turn on automatically updating submodules when performing `checkout`, `fetch` and `pull`:

```
git config --local submodule.recurse true
```

You can use `--global` instead of `--local` to make this the default behavior across all git repositories on your computer.

You can also turn automatic submodule updates on or off for `fetch` by setting:

```
git config --local fetch.recurseSubmodules true # or false
```

Note that this can make these commands take much longer to complete.

### Auto-update of submodules using command line flags

You can use the `--recurse-submodules` option with `fetch`, `pull`, and `checkout` to update submodules: `git checkout --recurse-submodules develop`. If you find yourself using this flag (or any command) regularly, you can alias it using a [git alias](https://git-scm.com/book/en/v2/Git-Basics-Git-Aliases). An example would be:

```
git config --global alias.chrs 'checkout --recurse-submodules' # chrs = 'checkout, recursing submodules'
# now you can use it like:
git chrs develop
```


[^top](#table-of-contents)

## Update local repository ##

You can update the branches on your local repository to those of a remote repository with:

    git pull
    git submodule update --init --recursive 

Many reported build problems are due to out-of-date submodules, so make sure to not skip the last step.

If you are going to do any development work, keep reading for more details...


### Updating and rebasing

The `git pull` command downloads *commits* from the online to the local repository. If you are doing any development work, it is best to always use it with the `--rebase` flag:

    git pull --rebase

The `--rebase` flag tells git to first put your new commits off the commit stack, and then stack them up on top of the just-downloaded commits. If the downloaded commits were stacked on top of yours, the history of your repository would not be a linear continuation of the history of the online repository anymore, which would prevent you from being able to push your commits online.

You could define a git command *alias* to help you with this - a short custom command that will substitute the longer command:

    git config alias.up pull --rebase

This will make `git up` equivalent to `git pull --rebase`.


### Updating submodules

Submodules are git repositories within other git repositories; the main SuperCollider repository uses several submodules. Submodules are not automatically updated within your local copy when you `git pull`, so now and then you need to update them manually using:

    git submodule update --init --recursive

How to know precisely when submodules need to be updated? Your local copy of submodules is out of sync when:
* the `git status` command shows directories that correspond to submodules as modified
* the `git diff` command will show changes related to these directories, in the form:
    `Subproject commit <commit ID>`

When you see any of these signs, it's time to update submodules. This may happen even whenever changing [branches](#branches), as different branches may use different versions of submodules.

Submodules are referenced in their hosting module by their URL. At some point the URL itself may be changed, and you will have to update it with:

    git submodule sync --recursive

In case you get a submodule stuck in a state you don't understand, it's handy to know that you can always delete the submodules and re-fetch them, for example:

    rm -rf external_libraries/nova-tt
    git submodule update --init --recursive


### Pulling from different sources

With git, it's also possible to pull changes from different clones of the same repository. For instance, you might have two or three computers that you use at different times. You can synchronize those clones over a local network without touching github!

The easy way:

    git pull https://example.com/repo.git their-branchname # get their changes

check that everything is okay

    git pull --rebase # update main from github
    git push

The hard way:

    git checkout -b merge-their-changes
    git pull https://example.com/repo.git their-branchname # get their changes

check that everything is okay, then push changes back to github.

    git checkout main
    git pull --rebase # update main from github
    git rebase main merge-their-changes # put their’s changes on top of latest changes from github
    git checkout main
    git merge merge-their-changes
    git push

taken from [here](http://people.gnome.org/~federico/misc/git-cheat-sheet.txt)


[^top](#table-of-contents)

## Commit + Push ##

Unlike in SVN, publishing changes is a two-step process in git:

- `Commit` the changes. The changes are now "permanent" in your local clone of the repository.
- `Push` the new commits into the public repository.

This has the advantage over SVN that you can manipulate the changes after committing but before pushing. If you made a mistake with some commits, you can `git reset` them, erasing them from your local repository. Then you can recommit before pushing.

Highly recommended: Set your global git configuration so that `git push` with no arguments will push only the current branch. Otherwise, if you forget to say `git push origin [branch]`, git will helpfully push all commits from all branches, including ones that you forgot about and didn't intend to make public. Once changes are pushed to the public repository, they can't be erased -- only reverted. Doing this will help to avoid headache-inducing mistakes.

    git config --global push.default upstream

If you're using an older version of git, substitute "tracking" for "upstream."

    git config --global push.default tracking


[^top](#table-of-contents)

## Branches ##
Another really helpful way to save you from yourself is to work in a local branch that doesn't exist in the public repository. If you are new to git, you `will` make mistakes. If you make mistakes in a published branch, such as "main," and you accidentally push those mistakes, it may take some effort to clean up. But if you work in a branch that exists only on your local machine, you can do anything you want with it, and then selectively move specific commits into a public branch.

With a local-only branch, the worst case (completely messing up the branch) is that you delete the local branch and re-create it, with no impact on the origin.

The "-b" option to `git checkout` creates a new branch from an existing one.

    git checkout main -b my_main # now you have your own disconnected branch of main

... work work work, commit stuff, blah blah...

    git log # take note of the commit IDs, which are 32 digit hexadecimal strings

    git checkout main # switch back to the real main branch
    git cherry-pick [ID] # repeat for each ID
    git cherry -v # doublecheck what will actually be pushed
    git push origin main

    git checkout my_main # safe again

`git cherry-pick` is a bit inconvenient for large numbers of commits. In that case, it would be better to use a "topic branch." See below, "Using a separate branch for work on a feature."


[^top](#table-of-contents)

## A common git workflow for development work on SuperCollider ##

Make sure you've done the "git clone" stuff above, then...


### Simple work on your main branch ###

Hack on existing files, create new files...

Display and check uncommitted changes:

    git diff main

Stage changed and new files (mark them for inclusion in the next commit):

    git add file1 file2 file3

Check which changed files are staged and which not:

    git status

Commit the staged changes and additions:

    git commit -m "This commit does this and that..."

Repeat the above procedure for as many separate commits as you want.

Update your local repository with latest commits in the public repository:

    git pull --rebase
    git submodule update --init --recursive

Check what you will be pushing:

    git log origin/main..

Push it:

    git push


### Using a separate branch for work on a feature ###

Sometimes you want to work on several unrelated features during the same period of time and you want to be able to switch between your work on one or another. You can do this by using several branches within your local repository. Each branch allows you to store your work on a feature in form of commits on top of the commit history at the time the branch was created. By default, each repository contains one branch named main, but you can create new ones (and even rename any of them later, including main).

Create a new branch named "my_new_feature" containing all the commits in the current branch:

	git checkout -b my_new_feature

By the way `git checkout branch_name` switches between branches. 'git status' will tell you which branch you are currently on.

Now start coding your changes, and commit them into your feature branch with 'git add' and 'git commit' as explained in the previous section.

While you are coding your new feature you might need to update the branch with latest changes from the remote (public) repository, to keep up with other developments. The safest way to do this is to update your main branch and then rebase commits introduced by your feature branch on top of the main. Be sure to have all local changes committed before doing this:

	git checkout main
	git pull --rebase
	git rebase main my_new_feature

When you are ready to push the work on the feature to the public repository, first do the above three steps to synchronize your local repository with the public one, then check what you are going to push with 'git log origin/main..' and do the following:

    git checkout main
    git merge my_new_feature
    git push

This will merge the additional commits of your feature branch into the main and push them public. For additional details about rebase, see (4).


[^top](#table-of-contents)

## Common git commands ##

upstream - the GitHub repository.

fetch and merge changes from upstream:

    git pull

commit all local changes:

    git commit -a -m “message”

commit changes in specific files:

    git add <files…>

    git commit -m “message”

get patch files for last N commits

    git format-patch -N

get patch files for all commits that are in your current branch but not in upstream:

    git format-patch origin/main

undo (delete) all current non-commited changes (Watch out !):

    git reset --hard HEAD

undo last commit, but leave the changes in the working tree

    git reset --soft HEAD^1

undo (delete) all commits since last time one was pulled from upstream (Watch out !). This should be done while in the main branch:

    git reset --hard origin/main

undo all commits since the last time one was pulled from upstream but leave the changes in the working tree. This should be done while in the main branch:

    git reset --soft origin/main

show uncommited local changes:

    git diff [file]

discard local changes instead of commiting them:

    git checkout — <file>

add interactively

    git add -i

To revert local commits, revert will create another commit that undoes the commit provided. Unlike reset the history is not erased.

    git revert <commit ID>

show changes compared to upstream:

    git diff origin/main    # only diff

    git show origin/main..  # log and diff

    git log origin/main..   # only log

show latest log in upstream:

    git log origin/main

see status of changes:

    git status
    

[^top](#table-of-contents)

## Problems with submodule state update ##

When switching branches and doing a submodule update (in SC: nova-simd and nova-tt"), git sometimes messes up the submodule status without you having touched it. 

It will post something like:

    On branch main
    Changes not staged for commit:
      (use "git add <file>..." to update what will be committed)
      (use "git checkout -- <file>..." to discard changes in working directory)
      (commit or discard the untracked or modified content in submodules)
    modified:   external_libraries/nova-tt (untracked content)


This can be remedied by deleting the file and updatind the submodules again (given you haven't consciously made any changes, of course, which you'd lose!):
    
    rm -r external_libraries/nova-tt
    git submodule update --init --recursive
    

[^top](#table-of-contents)

## Testing mailing list patches ##

To try out emailed patches (created with git send-mail) copy all the content of the original mail message in a file, e.g. patch.mbox, and remove all the empty/white-spaces lines from the beginning of that file. If the patch is a series of mails copy all in order in the same file (the subject has an order tag `[PATCH 0/N]`, `[PATCH 1/N]`, ..., `[PATCH N/N]`).

Note: in gmail go to the option "show original" and copy the plain text message.

Create a branch to try the patch

    git checkout -b solve_problem_patch

Apply and merge the patch with am (apply mailbox)

    git am -3 patch.mbox

After testing it the branch can be erased (be careful any change will be lost)

    git branch -D solve_problem_patch

Note: this workflow is useful just to try a patch and discard changes for other solutions check the Resources.


[^top](#table-of-contents)

## Resources ##

- [Git Book](http://book.git-scm.com/)
- [Pro Git Book](http://progit.org/book/)
- [Visual Git Tutorial](http://www.ralfebert.de/blog/tools/visual_git_tutorial_1/)
- [Rebasing](http://jbowes.wordpress.com/2007/01/26/git-rebase-keeping-your-branches-current/)
- [My Git Workflow](http://osteele.com/archives/2008/05/my-git-workflow)


contributed by:  Miguel Negrão, Jakob Leben, Jonatan Liljedahl, James Harkins, Till Bovermann
