<!-- TOC start (generated with https://derlin.github.io/bitdowntoc/) -->
#### Table of contents

- [Release Cycle](#release-cycle)
   * [Version branches](#version-branches)
      + [`beta` release](#beta-release)
      + [`main` Release](#main-release)
      + [`patch` Releases](#patch-releases)
   * [Turnaround time](#turnaround-time)
      + [Merging PRs](#merging-prs)
      + [Incrementing versions](#incrementing-versions)
- [Release checklist](#release-checklist)
   * [Writing changelogs](#writing-changelogs)
   * [A note about `sc3-plugins`](#a-note-about-sc3-plugins)

<!-- TOC end -->

# Release Cycle

## Version branches

A month or so before the beta release, the release manager branches off `develop` to create a new branch named after the release, say `3.13`. Uncontroversial bug fixes are merged into the `3.13` branch for further testing as a release candidate. This ensures that those changes already slated for the `3.13` release are sandboxed and given a grace period to ensure stability of those features. As issues are discovered in this period, patches need to be made.

This causes the `3.13` and `develop` branches to diverge, so any fixes added to the `3.13` branch are periodically be merged back into `develop` to keep `develop` up to date. **Note:** prereleases are not merged back into `main`! `main` is stable!

After a release branch is created, any new PRs reviewed and merged into the `develop` branch. They will be assigned milestone tags that designate which future release they are slated for.


### `beta` release

- In the `3.13` branch, the version is bumped from 3.13dev to 3.13.0-beta1 (or from 3.13.0-beta1 to 3.13.0-beta2, etc.), and the release is tagged accordingly.
- The changelog is updated, along with the "New in 3.13" help file.
- A release is created on the GitHub release page with builds for macOS, Linux, and Windows.
- The same is done for `sc3-plugins`.
- Announcements go out to the mailing list, Facebook, etc.


### `main` Release

- In the `3.13` branch, bump up the version in `SCVersion.txt` to 3.13.0.
- Copy the changelog again and convert it to schelp if there were any new changes.
- Update the release history in `README.md`.
- `3.13` is merged into `main`.
- The release is tagged in git as "Version-3.13.0". *Unlike the pre-releases, the branch is* `main`*.*
- `main` I merged into `develop`.
- A release is created on the GitHub release page with builds for macOS, Linux, and Windows.
- The same is done for `sc3-plugins`, even if `sc3-plugins` is unchanged, to indicate parity between compatible version numbers of two projects through their version numbers.
- Updates are made to the website download page, the [Wikipedia page](https://en.wikipedia.org/wiki/SuperCollider).
- Announcements are made everywhere: SCSynth Forum, Slack, Discord, etc.

### `patch` Releases

- The process is the same as the release proper. We keep the `3.13` branch for all the `3.13.x` releases.


## Turnaround time

### Merging PRs

The turnaround time is variable depending on a number of issues: the size and complexity of the proposed change, Reviewer availability, responsiveness of the author, to name a few. We recognize that everyone's time is valuable and we make best efforts to move the project forward!

There are also guidelines for Reviewers to assist in keeping review moving forward. For example, if a Reviewer becomes unavailable to follow through with your PR, another may be assigned to it to see it through.


### Incrementing versions

Ideally we aim for **3-4 months** though it can extend to **6+ months**. The timing of `3.x` release is dependent on the amount of work that gets done -- at least one big new feature per  release. If the releases are too quick then it's overwhelming for users, if they're too slow then we lose development momentum.


# Release checklist

- [ ]  When you're done with patch releases, bump up `SCVersion.txt` in `develop` to `3.Xdev`.
- [ ]  On release, post the changelog to the following announcement channels:
    - Post a full version with all pull request links to:
        - [ ]  *[CHANGELOG.md](http://changelog.md/)*
        - [ ]  "News in 3.x" helpfile
    - Post an abbreviated version:
        - [ ]  GitHub release page
        - [ ]  GitHub website
        - [ ]  [scsynth.org](http://scsynth.org/)
        - [ ]  Discord
        - [ ]  Facebook group
        - [ ]  Reddit (/r/supercollider)


## Writing changelogs

The [changelog](https://github.com/supercollider/supercollider/wiki/Changelog) documents the publicly visible changes since the most recent SuperCollider release. A change is worth putting in the log if it affects users, such as breaking changes (of course), new features, and bug fixes. Significant refactors should also be logged to identify areas that should be tested, and to help locate the culprit in case of breakage. Documentation edits generally shouldn't be on this list, but major overhauls and expansions may be appropriate.

The website [Keep a CHANGELOG](http://keepa[changelog](https://github.com/supercollider/supercollider/wiki/Changelog).com/en/0.3.0/) is a major inspiration for the organization of the changelog. Changes to each component of SuperCollider are subdivided into Added, Changed, Deprecated, Removed, Fixed, and Security, in that order.

Please provide the link to the PR with every entry in the changelog for easy navigation.

Try to exercise common sense in keeping the log readable and useful to users. Use complete sentences and, to a reasonable extent, err on the side of clarity. In case of doubt, prefer inclusion over exclusion.

link/description to semantic versioning

## A note about `sc3-plugins`

*New additions to the `sc3-plugins` project is currently suspended, pending a revision of third-party plugin distribution to ease maintenance efforts.*

The **merge process** described above is slightly different for the [sc3-plugins project](https://github.com/supercollider/sc3-plugins). There is no `develop` branch, `main` serves the role of a development branch. That is to say that versions are branched off of `main` for releases. For example, at some point we go into release mode for `3.13` by creating a `3.13` branch off `main`, so that branch will automatically have any previously merged PRs embedded in it, so no cherry-picking is necessary.

The plugin **release cycle** of `3.x` versions is strictly simultaneous with that of core SuperCollider versions. The reasons are not because of any development cycle of `sc3-plugins`, but because it's confusing for users if they're out of sync! So we can simply declare that 3.14 supercollider works with 3.14 plugins, and so forth.