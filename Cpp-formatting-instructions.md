### Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Getting started](#getting-started)
- [Working with clang-format](#working-with-clang-format)
  - [Reformatting as you work (normal usage)](#reformatting-as-you-work-normal-usage)
  - [Reformatting your last commit](#reformatting-your-last-commit)
  - [Reformatting an entire PR](#reformatting-an-entire-pr)
  - [CMake targets](#cmake-targets)
  - [Build directory scripts](#build-directory-scripts)
- [Working without clang-format](#working-without-clang-format)
- [What files are actually linted/formatted?](#what-files-are-actually-lintedformatted)
- [I made a PR before the reformat (June 2019) and it has merge conflicts now! How do I fix it?](#i-made-a-pr-before-the-reformat-june-2019-and-it-has-merge-conflicts-now-how-do-i-fix-it)
  - [Troubleshooting](#troubleshooting)
  - [Specific issues](#specific-issues)
    - ["'ascii' codec can't encode character"](#ascii-codec-cant-encode-character)
    - ["Your working tree has pending changes."](#your-working-tree-has-pending-changes)

###### *generated with [DocToc](https://github.com/thlorenz/doctoc)*

Overview
--------

In this context of this document, "linting" means checking that code is formatted correctly, without modifying code;
"formatting" means actually changing the code.

For information about our code style guidelines, which includes things like naming conventions, see [this
document](https://github.com/supercollider/supercollider/wiki/%5BWIP%5D-C---Code-Style-Guidelines).

SuperCollider uses [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html). This helps to make sure that the style
of the codebase is consistent across time and authors, and makes contributing and code review smoother.

Formatting is checked on each PR (pull request) by our CI (continuous integration) tools. This makes it impossible to
merge any change which violates our formatting standards.

If you are contributing to SuperCollider and plan on working on C++ code, it is strongly recommended that you
integrate ClangFormat into your development workflow.

Requirements
------------

**Python >= 3.6**: any version past 3.6 should work. To find out what version you have run `python --version`.

**ClangFormat v8.x.y**: either [8.0.1](https://releases.llvm.org/download.html#8.0.1) or
[8.0.0](https://releases.llvm.org/download.html#8.0.0) will work. In the long term, we would like to not require an
out-of-date version of clang-format. To find out if it's already installed, run `clang-format --version`.  Even if it
is installed, you may still need to do some setup (see below).

The LLVM official releases support at least: FreeBSD, Windows, Ubuntu, RHEL/Fedora, and macOS (8.0.0 only). Other
platforms might also be supported; it's unclear to the person writing this.

On **Arch Linux**, there is no good package for clang8; https://aur.archlinux.org/packages/clang8 conflicts with
clang, and the clang-8 source code release does not compile with the latest clang or gcc version. This script will
install it for you in a way that it peacefully coexists with other installations of clang:
https://gist.github.com/brianlheim/2f80768eb2429b285902f8898182ae2d.

If you can't find a suitable release artifact for your system on LLVM's website, check your package manager of choice.
If that doesn't work either, [let us
know](https://github.com/supercollider/supercollider/blob/develop/README.md#discuss) and we'll be happy to help you!

Getting started
---------------

1. Download and install Python and LLVM 8;  See
[requirements](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#requirements) above for
more info.
2. Open a terminal and execute `clang-format --version` and `clang-format-diff.py -h`. You should see something like
   this:

```
clang-format version 8.0.0 (tags/RELEASE_800/final)

usage: clang-format-diff.py [-h] [-i] [-p NUM] [-regex PATTERN]
                            [-iregex PATTERN] [-sort-includes] [-v]
                            [-style STYLE] [-binary BINARY]

Reformat changed lines in diff. Without -i option just output the diff that
would be introduced.

optional arguments:
  -h, --help       show this help message and exit
  -i               apply edits to files instead of displaying a diff
  -p NUM           strip the smallest prefix containing P slashes
  -regex PATTERN   custom pattern selecting file paths to reformat (case
                   sensitive, overrides -iregex)
  -iregex PATTERN  custom pattern selecting file paths to reformat (case
                   insensitive, overridden by -regex)
  -sort-includes   let clang-format sort include blocks
  -v, --verbose    be more verbose, ineffective without -i
  -style STYLE     formatting style to apply (LLVM, Google, Chromium, Mozilla,
                   WebKit)
  -binary BINARY   location of binary to use for clang-format
```

If you see this, and the clang-format verison matches the version you installed, and *you can skip the remaining steps.*

3. Otherwise, find where you installed LLVM, and within that directory you should see `your-llvm-root/bin/clang-format` and `your-llvm-root/share/clang/clang-format-diff.py`.
Find their full paths, and then add the following variables to your environment:

```
SC_CLANG_FORMAT=/full/path/to/clang-format
SC_CLANG_FORMAT_DIFF=/full/path/to/clang-format-diff.py
```

On macOS and Linux, you can add the following lines to `~/.bash_profile` (or the profile script for whatever shell you
prefer):

```
export SC_CLANG_FORMAT=/full/path/to/clang-format
export SC_CLANG_FORMAT_DIFF=/full/path/to/clang-format-diff.py
```

On Windows, this is done by setting environment variables through user settings; there are many articles online that
explain how.

4. Alternatively, you can add both the directories containing clang-format and clang-format-diff.py to your `PATH`.
   Instructions to do this can be found online. This may lead to issues if you have another version of LLVM or
   clang installed on your system. You can open a new terminal window and run `clang-format --version` and
   `clang-format-diff.py -h` like before to confirmed that you did it correctly.

Working with clang-format
-------------------------

There are four basic commands that we use for formatting: `lint`, `format`, `lintall`, `formatall`. The first two **only
apply to the code that changed between commits**, while the last two will run on the entire codebase.

It's very important to remember that by default, linting and formatting only apply to changes that
haven't been committed. **The intended way of using this tool is to format code before it's committed**. If you want to
lint or format code you've already committed, you need to also specify what you want to use as a "reference point". This
is the commit hash, branch name, or other commit specification (like `HEAD^`) you will give to the formatting script.
For example, if you realize you forgot to format code you just committed, you would only want to pass `HEAD^` (in git
this means the commit directly before your current one); if you want to lint or format an entire feature branch based
off `develop`, you would pass `develop`.

There are a couple ways you can use clang-format in SuperCollider:

1. Many IDEs and editors integrate directly with clang-format (more information
   [here](https://clang.llvm.org/docs/ClangFormat.html)). This is a great workflow as all your code will be formatted
   correctly by your editor without you having to think about it. You may need to tell your editor to use the version of
   clang-format that you installed rather than the one it came with.
2. You can run the `tools/clang-format.py` script directly; run `tools/clang-format.py -h` for more information.
3. You can run the `build/lint.py` and `build/format.py` scripts that are generated in your build folder. Both scripts
   accept a commit "reference point" as an optional first argument.
4. You can "build" some commands as build targets, see below.

### Reformatting as you work (normal usage)

If you are developing a C++ feature or bug fix, a typical workflow might look like this:

1. Write some code, build, test
2. Use your editor's integration or run `./format.py` in your build directory to format your code
3. Commit your changes with git

### Reformatting your last commit

If you just made a commit without formatting and want to reformat it:

1. Make sure your working directory is completely clean. The output of `git status` shouldn't show any files waiting
   to be committed, or any submodule changes. `git submodule update --recursive` will set your submodules to the
   correct commits.
1. Run `./format.py HEAD^` in your build directory or `tools/clang-format.py HEAD^` from anywhere. **Remember to
   include the `^`!**
2. If you haven't pushed your work yet, run `git commit -a --amend --no-edit` to update your last commit.
3. If you have already pushed your work, run `git commit -am "Format with clang-format"` to make a new commit.

### Reformatting an entire PR

If you've made a PR and now need to reformat the whole thing:

1. Make sure your working directory is completely clean. The output of `git status` shouldn't show any files waiting
   to be committed, or any submodule changes. `git submodule update --recursive` will set your submodules to the
   correct commits.
1. Run `./format.py develop` in your build directory or `tools/clang-format.py develop` from anywhere.
3. Run `git commit -am "Format with clang-format"` to make a new commit.

### CMake targets

The following targets are provided in the build system:

- `lint`: lints all uncommitted changes to the working tree. The output will be in the form of a
  diff between your changes and correctly formatted code. If there are no changes, this target will
  exit without printing anything.
- `format`: makes exactly the changes shown by `lint`. Does not commit any changes.
- `lintall`: lints *all* files in the repository. This takes a long time.
- `formatall`: formats *all* files in the repository. This also takes a long time.

To make use of them, either build the target in your IDE, or run them on the command line in your build directory like
this: `cmake --build . --target lint`.

This method should not be your main method of formatting, because there's no way to specify a reference commit to format
against.

### Build directory scripts

In your build directory (usually, `/path/to/supercollider/build`), after running CMake, you will
have two Python scripts named `lint.py` and `format.py`. These behave like the `lint` and `format`
targets, but they also take an optional single argument, the name of a commit to diff against. For
instance, if you have a branch `feature` which is 3 commits ahead of `develop`, you can run
`./lint.py develop` to lint the C++ changes introduced on your feature branch (and nothing else).

This is useful for quickly reformatting an entire branch of changes if you've neglected to format
each commit, and don't want to go back and redo each commit separately.

Working without clang-format
----------------------------

Sometimes you just want to update your PR (pull request) so it passes linting, without installing clang-format. It
will be painful but you can follow these steps as a last resort:

1. Look toward the bottom of the PR for the section that has "Some checks were not successful", then next to the
   check called "continuous-integration/travis-ci/pr" click "Details".

<img width="600" alt="Screen Shot 2020-11-22 at 11 18 34 AM" src="https://user-images.githubusercontent.com/15369640/99910685-fcaf1480-2cb4-11eb-8c4d-0723f89fd306.png">

2. This will take you to Travis's build job view. You will see a listing of build jobs each labeled N.1, N.2, N.3,
   where N is some number. Select build job 11, which also has "with linting" in its JOB_NAME. It should be the one
   with a red exclamation point next to the name instead of a green check mark. (Depending on the PR there may be other
   jobs with red marks)

<img width="600" alt="Screen Shot 2020-11-22 at 11 19 00 AM" src="https://user-images.githubusercontent.com/15369640/99910684-fc167e00-2cb4-11eb-8fa7-e457bbb85fa8.png">

3. Scroll down through the log, or open the raw log, until you get to "Running tools/clang-format.py lintall".
   Everything from here until "The command $TRAVIS_BUILD_DIR/.travis/before-install-$TRAVIS ..." is what clang-format
   disagreed with. If you don't want to use clang-format, you will have to manually make these changes in your local
   repo. For some diffs, it may look like nothing has changed; make sure you check locally for things like trailing
   whitespace, mixed spaces and tabs, and tabs instead of spaces.

<img width="600" alt="Screen Shot 2020-11-22 at 11 19 47 AM" src="https://user-images.githubusercontent.com/15369640/99910682-fb7de780-2cb4-11eb-90b8-e6ef1aff4462.png">

What files are actually linted/formatted?
-----------------------------------------

Any file with an extension of `c`, `h`, `cpp`, `hpp`, `m`, or `mm` is linted or formatted, with the
exception of files that we don't have direct control over. That set of files consists of code from
third parties or other projects (files under `external_libraries`), and files generated by code
generation tools. These auto-generated files are:

- `SCDoc/SCDoc.tab.cpp`
- `SCDoc/SCDoc.tab.hpp`
- `SCDoc/lex.scdoc.cpp`
- `lang/LangSource/Bison/lang11d_tab.cpp`
- `lang/LangSource/Bison/lang11d_tab.h`

I made a PR before the reformat (June 2019) and it has merge conflicts now! How do I fix it?
--------------------------------------------------------------------------------------------

If you have a branch that contains work prior to the major C++ reformatting commit (tag `tag-clang-format-develop`, which happened around June 2019), just follow these steps.

1. Follow the "Getting Started" steps above if you haven't already.
2. Run the following commands to update your local repo. This assumes that `upstream` points to the main SuperCollider
   repository; you can use `git remote -v` to check.

```
git checkout develop
git pull upstream develop
git pull upstream --tags
```

3. Rebase your branch to the commit before the reformat:

```
git checkout my-branch
git rebase tag-clang-format-develop^  # DON'T FORGET THE ^ !!!!
```

The ^, which you absolutely must not forget, indicates that you're rebasing onto the commit immediately before the relevant reformat commit. This gives you access to the `tools/clang-format.py` script.

Under normal conditions, this rebase won't create any conflicts. If there are conflicts, you can try to resolve them
yourself, or ask for help.

4. Checkout and commit the latest version of the clang-format.py script. Since it was written, there have been a few
   bugs fixed in the clang-format.py script. In order to get the best rebase experience, you should check the latest
   version out from the develop branch and commit that separately **on the branch you want to rebase**.

```
git checkout my-branch
git checkout develop -- tools/clang-format.py # only modifies the one file
git add tools/clang-format.py
git commit -m "Update clang-format.py to latest develop prior to rebase"
```

The script may later complain about an empty commit due to this, but don't worry.

5. Rebase it!

```
tools/clang-format.py rebase -b develop
```

This will switch you over to a new branch called `<branch-name>-reformatted`, and explain how to undo what you just did
if you think you made a mistake.

6. Update your remote branch. Inspect the changes -- do they all look good? If so:

```
# rewrite the original branch to match the reformatted one
git branch -f <branch-name>

# Force push your changes to the branch in your fork of SC
git push -f origin <branch-name>
```

Any PR you have open will automatically update. **There is no need to close and re-open your PR.**

### Troubleshooting

We are using fairly tricky git features here. **If something gets screwed up, don't panic** and **don't do reckless things like deleting your entire repository**. It will probably not fix your issue.

Instead, just ask for help in [one of our communities](https://github.com/supercollider/supercollider/wiki#joining-the-community).

### Specific issues

#### "'ascii' codec can't encode character"

If the script fails with something like this error message:

`*** ERROR: 'ascii' codec can't encode character u'\u2026' in position 629: ordinal not in range(128)`

You may need to use Python 3 to run the script (see below in Requirements). First, reset your repository state, then try rerunning the script with Python 3:

```
git reset --hard <branch-to-rebase>
python3 tools/clang-format.py rebase -b develop # or current release version
```

#### "Your working tree has pending changes."

If the script fails with this error message:

`*** ERROR: Your working tree has pending changes. You must have a clean working tree before proceeding.`

You need to make sure that any changed files shown by `git status` are reset back to their clean state. You can do that with the following commands. **Be certain you are not losing any unsaved work before you start running these!**

```
git reset --hard # resets all files in your working tree
git submodule git submodule foreach --recursive git reset --hard # resets all files in the working trees of your submodules
git submodule update --recursive --force # resets all submodules according to the currently checked out commit
```
