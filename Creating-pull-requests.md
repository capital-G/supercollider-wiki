### Before making changes
See [Setting Up Your Development Environment](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment), to make sure you have a working and updated fork of SuperCollider's source code.
Then you can create a fresh new branch for your contribution:

### Create a topic branch
- Create a topic branch from where you want to base your work.
	- Your topic branch should be based on `develop`, unless it is a trivial bug fix or documentation change, in which case it should be based on the latest release (`3.x`) branch.
	- Our branch naming convention is `topic/branch-description`: for example, `topic/fix-sinosc` or `topic/document-object`.
	- To quickly create a topic branch based on develop: `git checkout -b topic/my-fix develop`.
	- Please do not work off of the `master` branch, which is stable and only includes releases.
- As time passes, make sure to keep your fork updated - see [Updating your fork](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment#2-Keep-your-fork-updated).

### Making changes

- Make commits of logical units.
- Please refer to [Code Style Guide](https://github.com/supercollider/supercollider/wiki/Code-style-guidelines). Note that code style, such as whitespace conventions, depend on the language (`C++` vs `SuperCollider` vs `SCDoc Markup`)
- Make sure your commit messages are descriptive and in the proper format.
	- Commit messages follow the schema "category: content", e.g. `docs: Make the example in CONTRIBUTING imperative and concrete`, or `help: Update RunningSum2 help file`, or `class library: do this and that`, or `plugins: add missing function definition`.
	- A more complete example:

	        docs: Make the example in CONTRIBUTING imperative and concrete

	        Without this patch applied the example commit message in the CONTRIBUTING
	        document is not a concrete example. This is a problem because the
	        contributor is left to imagine what the commit message should look like
	        based on a description rather than an example. This patch fixes the
	        problem by making the example concrete and imperative.

	        The first line is a real life imperative statement which optionally identifies
	        the component being changed. The body describes the behavior without the patch,
	        why this is a problem, and how the patch fixes the problem when applied.

- Make sure you have added the necessary tests for your changes. All changes to code should include a test which checks for correct functionality, including regression tests for bug fixes. Info on best practice for Unit tests is available at https://github.com/supercollider/supercollider/wiki/Unit-Testing-Guide
- Make sure you have documented your changes, if necessary.

### Submitting changes as Pull Requests

- Push your changes to a topic branch in your fork of the SuperCollider repository. If you are working locally, do this with `git push -u origin topic/branch-description`. `origin` should be the remote of your fork; check with `git remote -v`.
- Submit a pull request to the SuperCollider repository.
- The core team looks at pull requests on a regular basis in a public meeting that is held on a weekly basis. The meeting times are announced on the sc-dev mailing list.
- You may receive feedback and requests for changes. We expect changes to be made in a timely manner. We may close pull requests if they aren't showing any activity.

### Notes on rebasing and merge conflicts

It is almost never a good idea to resolve merge conflicts via the GitHub interface or by merging the main branch in locally. This creates noise in commit history and makes it more difficult to perform other operations on branches later. In the SuperCollider project, the preferred way to resolve merge conflicts in a pull request is by rebasing.

See `git help rebase` for `rebase` usage examples that include graphical representations.

Rebasing (`git help rebase`) is a very useful command for four scenarios in particular:

1. If you'd like to incorporate new commits on the base branch that contain relevant fixes or
   features into your topic branch.
2. If you'd like to resolve merge conflicts.
3. If you'd like to change the branch your topic branch is based on. This may happen if, for instance, a maintainer requests that you make your bug fix merge request against a release branch (e.g. 3.9, 3.10) instead of develop. You will then need to rebase your topic branch onto the appropriate release branch.
4. If you'd like to rewrite your commit history by combining or reordering some commits (not recommended for those newer to git).

Rebase has an interactive mode (`git rebase -i`) which will show exactly which commits will be applied to the new base, and the order in which they will be applied. This can be very helpful when you're not completely sure what the result of a rebase will be.

For scenarios (1) and (2), suppose that the current branch is `topic/foo`, which is based on an old commit from the `develop` branch. To rebase, you can execute `git rebase -i develop`. You can examine the change list to make sure it's correct before continuing. Git will stop if it encounters a merge conflict, and give instructions on how to resolve it and continue the rebase.

For scenario (3), suppose that there are three branches: `develop`, the release branch `3.10`, and the topic branch `topic/foo` which is based on `develop`. Suppose that `topic/foo` is currently checked out.  You would like it to be based on `3.10` instead of `develop`. An easy way to do this is with `git rebase -i --onto 3.10 develop topic/foo`. Beware that you may need to resolve merge conflicts during this rebase.

After rebasing, you may find it helpful to display the pretty-printed commit log with `git log --oneline --graph --decorate` to make sure all is well.

In any case, after rebasing your local branch will now be out of sync with your remote branch. You will have to resolve this by force pushing: `git push --force origin topic/foo`. If you realize later that you made a mistake with your rebase, it's always possible to go back to your previous local state using `git reflog`.

For scenario (4), `git help rebase`'s section "Interactive mode" has extensive documentation on how to reorder and recombine commits. Also refer to the section on `--autosquash` for ideas on how to combine these features into a streamlined rebase-oriented workflow.

## Additional resources

More information can be found on the [git workflow wiki page](https://github.com/supercollider/supercollider/wiki/git-workflow-and-guidelines).

You can also refer to Github's guide to [forking a repository](https://help.github.com/articles/fork-a-repo/) and to [syncing a fork](https://help.github.com/articles/syncing-a-fork/).

Instructions on adding translation files for the IDE can be found in the [Developer Reference](https://github.com/supercollider/supercollider/wiki/Developer-reference) (soon to be moved, please update that link when it does move...).
