This is a work-in-progress document started by Marcin with some notes about implementing our automated build system (CI/CD) using GitHub Actions (GHA). For reasons and background information on migrating to GHA see [#5252](https://github.com/supercollider/supercollider/issues/5252) and [#5261](https://github.com/supercollider/supercollider/issues/5261).

## General Information
GitHub Actions is configured using a `yaml` file located in `.github/workflows/<name>.yml`

## Workflows, Jobs, Steps, Actions
...also Events and Runners

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

