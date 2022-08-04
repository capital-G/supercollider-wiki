As of March 2021, [we have fully moved](https://github.com/supercollider/supercollider/wiki/GitHub-Actions-migration-notes) our CI from Travis and AppVeyor to GitHub Actions for the main SuperCollider repository.

As of March 2021, sc3-plugins CI has not been moved to GitHub Actions.

"Continuous integration" (CI) is a practice where an application is continuously tested in a reproducible, fixed environment, and is useful to quickly detect bugs and regressions and the changes that introduce them. We have CI services for SuperCollider and sc3-plugins provided by GitHub Actions (GHA). This document is intended to provide information about this system and how we use them for people maintaining our CI integrations or interested in maintaining them.

Several things are checked in our CI builds:
- various dependencies can be installed reliably
- the project can be configured correctly by CMake
- the project builds successfully
- tests all pass

CI is also responsible for pushing release artifacts to GitHub (the "assets" shown in [the releases page](github.com/supercollider/supercollider/releases)) and for pushing builds to our S3 AWS cloud storage. Builds are also accessible for a limited time directly in the Actions page.

## Branch vs PR builds

Currently GitHub Actions builds are triggered for following events:
1. "PR": builds the result of merging a PR, to check whether the merge is acceptable. Triggered on every update to a PR branch
2. "branch": builds a commit in its current state. Triggered on every update to any branch in the main repository.

A single push can trigger both a PR and branch build if the branch is in the main repo and also open as PR.

Important: "PR" builds don't have access to encrypted environment variables which we use for things like access keys and IDs. Of course, it would be a major security risk otherwise. Upload to S3 is disabled for those builds.

## Access to CI

Anyone can see the status of the GitHub Action after selecting "Actions" tab in the SuperCollider repository. Anyone with Reviewer, Trusted reviewer, or Core Team status can restart builds and modify some settings in GitHub Actions. 

## Access to S3

Our S3 storage is owned by Scott Carver. Brian Heim also has limited access.

## Encrypted information

Sensitive information is stored in SuperCollider's "Repository secrets". We use this functionality for storing S3 access keys.

## Storage and deployment of build artifacts

Builds produce "artifacts", in our case dmg files, zip files and Windows installers. These are stored in 3 places:
- GitHub Action's own storage (available for a limited time and only for authenticated GitHub users)
- An AWS S3 instance
- GitHub releases pages

Brian Heim and Scott Carver have access to the S3 instance we use for storage. For info on where the S3 builds live, see [here](https://github.com/supercollider/supercollider/wiki/Miscellaneous-project-information-(CI,-maintenance-scripts,-etc.)#s3-build-hosting).

For SC and sc3-plugins:
- on every build of an internal branch, a DMG/ZIP macOS archive and ZIP Windows archives are deployed to S3
- on every build of a tag, a DMG/ZIP macOS archive, Windows installers (SC) and ZIP Windows archives are deployed to the GitHub release

## [skip ci]

In GHA, we automatiacally skip building if the changes are made only to help files, `*.md` files, examples, and sounds. See [paths-ignore section in the workflow file](https://github.com/supercollider/supercollider/blob/develop/.github/workflows/actions.yml#L10).

Additionally, if you have `[skip ci]` in the first line of your commit message then GHA won't build it. Please **only** use this functionality when a commit only changes comments, documentation files, or other text files. Do not use it when adding, deleting, or renaming files.

## Restarting builds

If a build fails for a spurious reason and you think it will work on the next run, restart it. To to the Actions tab, open the Workflow that's failing, and press "Re-run jobs" in the top-right section of the screen.

## CI config files

`.github/workflows/actions.yml` is the YAML file that control configuration of GHA.

## Linting

In first job that's run in GHA the whole project is linted. All other builds depend on that one, so if linting fails, no actual compilation occurs. The log will print out the linting diff, which you can share with a PR author.

## Build steps

(to be added)

qpm is our python test runner (github.com/supercollider/qpm), see the repo for more info.

## Test suite

Our test suite is run using qpm, see [#5332](https://github.com/supercollider/supercollider/pull/5332) for more details.
### Which tests are being run
We use the test suite from https://github.com/supercollider/supercollider/tree/develop/testsuite/classlibrary. We run _all the tests_, _except_ the ones excluded in https://github.com/supercollider/supercollider/blob/develop/testsuite/scripts/gha_test_run_proto.json.
### Adding new tests to the test suite
In order to add tests to the test suite, just add them to https://github.com/supercollider/supercollider/tree/develop/testsuite/classlibrary. Once the changes are pushed to the repository, they will be run in GHA.
### Removing tests from the test suite
- If the test has issues and needs to be disabled temporarily, please add an [entry](https://github.com/supercollider/supercollider/blob/develop/testsuite/scripts/gha_test_run_proto.json#L7) with `"skip":true` parameter to https://github.com/supercollider/supercollider/blob/develop/testsuite/scripts/gha_test_run_proto.json
- If the test is invalid for whatever reason, it should probably be removed from https://github.com/supercollider/supercollider/tree/develop/testsuite/classlibrary

### Additional notes
- Running scsynth in GH runners is possible. On Linux one can use jack1 with dummy driver; on macOS, while audio hardware is not present, the runners have SoundFlower installed and SC server boots fine using it.

## Notes on migrating from Travis/AppVeyor to GitHub Actions

See [GitHub Actions migration notes](GitHub-Actions-migration-notes).

## Troubleshooting, tips and tricks

The most important thing when troubleshooting a CI issue is to check the log carefully. Sometimes, errors early on don't manifest until much later in the build.

---

If you see a failing build and can interpret the reason for the failure, do so, especially for newer contributors and when the reason for the build failing is not obvious.

---

Sometimes the CI might be temporarily unavailable and not build a commit. Usually manually restarting the workflow should fix this. If not, a last resort is to push the same set of commits under a different branch name, and then make a new PR for that. For example if your branch `topic/example` is the problem:

```
git checkout topic/example
git checkout -b topic/example-retry
git push -u origin topic/example-retry
```

You could also push an empty or otherwise bogus commit.

---

If you have the time and patience, when you see a build failure try to see if there is a way it could have been made clearer and contribute it. There is lots of room for improvement.

---

If you make a change to one of sc3-plugins or SC's CI files, double check whether the same change should apply to the other.