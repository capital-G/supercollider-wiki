(github-actions-migration-notes)=
# GitHub actions and migration notes

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

Moved to [Continuous Integration - GitHub Actions](https://github.com/supercollider/supercollider/wiki/Continuous-Integration---GitHub-Actions#test-suite).
