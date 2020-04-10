"Continuous integration" (CI) is a practice where an application is continuously tested in a reproducible, fixed environment, and is useful to quickly detect bugs and regressions and the changes that introduce them. We have CI services for SuperCollider and sc3-plugins provided by AppVeyor (Windows) and Travis (Linux, macOS). This document is intended to provide information about those systems and how we use them for people maintaining our CI integrations or interested in maintaining them.

Several things are checked in our CI builds:
- various dependencies can be installed reliably
- the project can be configured correctly by CMake
- the project builds successfully
- tests all pass

CI is also responsible for pushing release artifacts to GitHub (the "assets" shown in [the releases page](github.com/supercollider/supercollider/releases)) and for pushing builds to our S3 AWS cloud storage.

## Branch vs PR builds

Both Appveyor and Travis build commits in 2 cases:
1. "PR": builds the result of merging a PR, to check whether the merge is acceptable. Triggered on every update to a PR branch
2. "branch": builds a commit in its current state. Triggered on every update to any branch in the main repository.

A single push can trigger both a PR and branch build if the branch is in the main repo and also open as PR.

Important: "PR" builds don't have access to encrypted environment variables which we use for things like access keys and IDs. Of course, it would be a major security risk otherwise.

## Access to CI

People need to have membership within the SuperCollider organization to do actions within Travis and AppVeyor. Anyone with Reviewer, Trusted reviewer, or Core Team status can restart builds and modify some settings in AppVeyor. Admin privileges belong to Brian Heim. For Travis CI, Core Team membership gives you access over most settings.

## Storage and deployment of build artifacts

Builds produce "artifacts", in our case zip files and Windows installers. These are stored in 3 places:
- Appveyor's own public storage (see Appveyor section below for details)
- An AWS S3 instance
- GitHub releases pages

Brian Heim and Scott Carver have access to the S3 instance we use for storage. For info on where the S3 builds live, see [here](https://github.com/supercollider/supercollider/wiki/Miscellaneous-project-information-(CI,-maintenance-scripts,-etc.)#s3-build-hosting).

For SC and sc3-plugins:
- on every build of an internal branch, a ZIP macOS archive and ZIP Windows archives are deployed to S3, and (normally) the Windows archives are stored on AppVeyor too
- on every build of a tag, a ZIP macOS archive and Windows installers (SC) or ZIP Windows archives (sc3-plugins) are deployed to the GitHub release

## [skip ci]

If you have `[skip ci]` in your commit message then neither Appveyor nor Travis will build it. You can also use `[skip appveyor]`. `[skip travis]` doesn't work but we should make it possible.

## Restarting builds

If a build fails for a spurious reason and you think it will work on the next run, restart it. (TODO how to do this)

## CI config files

`.travis.yml` and `.appveyor.yml` are YAML files that control configuration of each service. They have similar structures:
- a listing of general project information
- configurations of individual build jobs, such as which OS each job runs on and the values of environment variables. This stuff is set up before each job starts
- a series of commands organized into "build phases" like before_install, script, before_deploy, and so on. Each job will run through these commands in order and fail if any of them fails
- a listing of deployment configurations (we use S3 and GitHub)

## Travis-specific notes

The file that controls travis config is `.travis.yml` which in turn uses several scripts in the `.travis` directory. Those scripts do complex things and are separated by OS and build step.

We have 3 jobs right now for SC:
1. Ubuntu build with Qt components (IDE, sclang Qt extensions)
2. Ubuntu build without Qt components, which lints the codebase
3. macOS build with Qt components

(2) is very important, as it is the only place the whole project is linted. If only this build fails on a C++ change, it is probably because it failed linting! The log will also print out the linting diff, which you can share with a PR author.

For sc3-plugins, we just have Ubuntu and macOS builds.

## Appveyor-specific notes

For SC and sc3-plugins we have two builds each -- Windows 64-bit and Windows 32-bit.

These ones build slower than Travis because we only have 1 parallel build with Appveyor between both SC and sc3-plugins. Plus, the individual jobs take 15-30 min because there's no caching. This is why PR builds will sometimes get stalled for a long time waiting for AppVeyor.

The 32-bit build for SC uses an old version of Qt (5.9) because that's the last version for which 32-bit WebEngine components were released.

Appveyor has a very strange policy where artefacts are always uploaded to their cloud and retained for 6 months, no exceptions or configurability. So sometimes we hit an arbitrary storage limit imposed by them.

**NOTE**: Unfortunately right now we are waiting for this limit to be raised, so **temporarily we are not creating "artifacts", just pushing to S3 manually the same artifact we would normally deploy via configuration**. This is also important because **no artifact will be deployed to github currently**. That needs to be reversed before SC is released because for Windows SC builds we need to deploy an installer and not the ZIP that is pushed to S3.

## Build steps

Each of our SC builds does the same thing:
- install dependencies and set up the environment
- install qpm (for GUI build)
- configure the project
- build the project
- install the project to a directory below the build directory
- run tests with qpm (for GUI build)

qpm is our python test runner (github.com/supercollider/qpm), see the repo for more info.

## Troubleshooting, tips and tricks

The most important thing when troubleshooting a CI issue is to check the log carefully. Sometimes, errors early on don't manifest until much later in the build.

---

If you see a failing build and can interpret the reason for the failure, do so, especially for newer contributors and when the reason for the build failing is not obvious.

---

Try to encourage people to use [skip ci] as much as possible in their commit messages.

---

Sometimes Github and the CI server just won't communicate right and a PR will refuse to build. In that case, a last resort is to push the same set of commits under a different branch name, and then make a new PR for that. For example if your branch `topic/example` is the problem:

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