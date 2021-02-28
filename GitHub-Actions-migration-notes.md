This is a work-in-progress document started by Marcin with some notes about implementing our automated build system (CI/CD) using GitHub Actions (GHA). For reasons and background information on migrating to GHA see [#5252](https://github.com/supercollider/supercollider/issues/5252) and [#5261](https://github.com/supercollider/supercollider/issues/5261).

## General Information
GitHub Actions is configured using a `yaml` file located in `.github/workflows/<name>.yml`

### GHA structure
Workflows >> Jobs >> Steps, which use Actions

Events: what triggers a Workflow (e.g. push, a PR, possibly the REST API/manual trigger)

Runners: virtual machines with preconfigured OS images that run Jobs

### Implementation notes
- All actions for the CI are specified directly in a .yaml file; no separate scripts are used, which was the case with our Travis implementation
- Currently we have a single .yaml file with linting, building, testing, and deployment
- There are very minimal "dependencies" between Jobs/Steps
  - We create a "version string" in the linting step
    - all subsequent Jobs depend on the linting Job
    - the version string is either: 
      - git tag, without the `Version-` prefix, or
      - commit SHA
    - that string is used in other Jobs/Steps, referred to as `needs.lint.outputs.sc-version`, where `lint` is the set name of the linting job, and `sc-version` is the `id` of the step that creates the string
- Test suite jobs run separately from build jobs
  - they download artifacts uploaded to GHA by the building step
  - for this reason, artifact name format needs to be kept consistent for all Jobs
    - if it is changed in the future, all Jobs need to be adjusted to use it (particularly testing jobs need to be updated to match the building jobs)
    - at the time of writing, the artifact name is `SuperCollider-<sc-version>-<artifact-suffix>.zip`, where `sc-version` is either tag or commit SHA, and artifact suffix is manually specified for each Job, e.g. `macOS` or `linux-bionic-gcc10`
    - **testing and deployment actions need to match the artifact name from the building step**
  - at the time of writing this, it is not possible to use matrix entries in the `depends on` field for Jobs, thus all tests wait for both Linux and macOS builds to finish; if possible in the future, it would be better for Linux tests to wait only on Linux builds, and macOS tests wait only on macOS builds


## Qt

Qt is not preinstalled on GitHub-provided runners. On Linux and macOS it can be installed using package managers (`apt` and `homebrew`, respectively). It can also be installed on all platforms using `install-qt-action`:
```yaml
- name: install qt using aqtinstall
  uses: jurplel/install-qt-action@v2
  with:
    modules: 'qtwebengine'
```
Note: on macOS I am currently getting [issues with library paths](https://github.com/supercollider/supercollider/issues/5294) when using this method of Qt installation

## Debugging
One of the ways to debug problems with GHA is to log in via SSH to the runner while it's running our job. This can be done using a following action:
```yaml
- name: debug with tmate
  uses: mxschmitt/action-tmate@v3
```
This action will allow SSH access to the runner, allowing interactive evaluation of scripts etc. Once the job reaches this step, it will post an address for SSH access (either through a browser or through a terminal). Subsequent steps are _not_ being run while this action is running. 

To continue with following steps, create an empty file with the name `continue` either in the root directory or in the project directory by running `touch continue` or `sudo touch continue`.


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