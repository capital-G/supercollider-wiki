SuperCollider uses an unstable master branch. Stable releases are marked using tags, along with GitHub's "releases" page.

All contributions to the project should be done in topic branches in contributor forks of the repository. **Contributors with push access should never, ever push directly to the master or release branches.** A topic branch name starts with `topic/` and then a very brief description of what the branch is doing, e.g. `topic/fix-sinosc-help`. We aren't strict about the naming conventions for topic branches — it's mostly for your own good.

When you file a pull request, GitHub gives you the option to allow contributors with write access to the main repository to push to the branch on your fork. This is a very good idea, and you should enable it on every PR you file. We used to create topic branches in the main repository, but now that GitHub has added this feature, this is discouraged.

## Guidelines for pull request authors ##

*this section is kind of in a proposal state, so it's not necessarily enforced*

**Documentation.** New features and behavior changes should be accompanied with documentation.

**Unit tests.**

**Clean commit history.**

**A good title and description in GitHub.**

## Releasing ##

A month or so before the beta release, the release manager creates a new branch named after the release (say 3.9). Uncontroversial bug fixes should be merged into the 3.9 branch, and everything else should go into the master branch. This causes the 3.9 and master branches to diverge, so the fixes in the 3.9 branch should periodically be merged into master to keep master up to date.

The first thing to do in release mode is to remove the `SCClassLibrary/deprecated/3.8` directory and document these removals in the changelog. Corresponding UGen and primitive code should also be removed. Be careful when deprecating UGens and be considerate of alternate clients!

For each beta release:

- In the 3.9 branch, bump up the version in the top-level file `SCVersion.txt` from 3.9dev to 3.9.0-beta1 (or from 3.9.0-beta1 to 3.9.0-beta2, etc).
- Copy the changelog to a new "News in 3.9" helpfile. This is best done as late as possible before the beta release to avoid having to update the changelog continuously.
- Tag the beta release in git as (say) "Version-3.9.0-beta1." Release on GitHub.
- Announce to mailing list, Facebook, etc.
- Merge 3.9 into master. This will temporarily mess up `SCVersion.txt` in master, but who cares, it's master.

For the release proper:

- In the 3.9 branch, bump up the version in `SCVersion.txt` to 3.9.0.
- Copy the changelog again if there were any new changes.
- Tag the beta release in git as "Version-3.9.0." Release on GitHub.
- Announce to mailing list, Facebook, etc. Celebrate, bake a cake, etc.
- Merge 3.9 into master.

For patch releases, the process is the same.

When you're done with patch releases, bump up `SCVersion.txt` in master to 3.10dev.