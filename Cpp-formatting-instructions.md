I made a PR before the reformat and it has merge conflicts now! How do I fix it?
--------------------------------------------------------------------------------

First off, don't do anything brash. **You don't need to close your PR.** This following process will update a PR that you've already filed.

If you have a branch that contains work prior to the major C++ reformatting commit, just follow these steps.

### Install requirements

You will need clang v8.0.0 (exactly) and Python 2.7+ or 3.6+. Instructions on grabbing the dependencies are here: https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#requirements

### Update your repo

First, update the `3.10` and `develop` branches.

```
git checkout 3.10
git pull upstream 3.10
git checkout develop
git pull upstream develop
```

The next steps also rely on the existence of the tags `tag-clang-format-develop` and `tag-clang-format-3.10`. To grab these, run

```
git pull upstream --tags
```

### 3.10 or develop?

Figure out whether your PR was originally made from 3.10 or develop. If you forgot, look up the PR on GitHub and see what it was filed against. In this case, it's 3.10:

![Untitled](https://user-images.githubusercontent.com/1211064/58756835-d2f8a100-84b4-11e9-8979-e1812a91abb6.png)

### Rebase onto the commit before the reformat

If your branch was based on `develop`, run:

```
git rebase tag-clang-format-develop^  # DON'T FORGET THE ^ !!!!
```

For 3.10:

```
git rebase tag-clang-format-3.10^  # DON'T FORGET THE ^ !!!!
```

The ^, which you absolutely must not forget, indicates that you're rebasing onto the commit immediately before the relevant reformat commit. This gives you access to the `tools/clang-format.py` script.

Under normal conditions, this rebase won't create any conflicts. If there are conflicts, then first make sure that you've correctly chosen between develop and 3.10. If that was correct, it means a conflict started happening sometime between when you created the branch and the reformat, so this issue is unrelated to the reformat and should be addressed first.

### Reformat it!


If your branch was based on `develop`, run:

```
tools/clang-format.py rebase -b develop
```

For 3.10:

```
tools/clang-format.py rebase -b 3.10
```

This will switch you over to a new branch called `<branch-name>-reformatted`.

### Confirm

Inspect the changes -- do they all look good?

If so:

```
# rewrite the original branch to match the reformatted one
git branch -f <branch-name>

# Force push your changes to the branch in your fork of SC
git push -f origin <branch-name>
```

The PR will automatically update. **There is no need to close and re-open your PR.**

### Troubleshooting

We are using fairly tricky git features here, and I'm aware a lot of people are relatively new to git. **If something gets screwed up, don't panic** and **don't do reckless things like deleting your entire repository.** It will probably not fix your issue.

Instead, just ask for help! The fastest way to get help is [Slack](https://join.slack.com/t/scsynth/shared_invite/enQtMzk3OTY3MzE0MTAyLWY1ZGE1MTJjYmI5NTRkZjFmNjZmNmYxOWI0NDZkNjdkMzdkNjgxNTJhZGVlOTEwYjdjMDY5OWM0ZTA4NWFiOGY) (since Brian and I are on there), but not everyone is on that, so you can also leave a comment on the [official support thread](https://github.com/supercollider/supercollider/issues/4428) on GitHub. If you're having a problem, just leave a comment and someone more experienced with the process can help you out.

Linting and formatting
======================

This document has information about linting and formatting C++ code in the SuperCollider project.

To [**lint**](https://en.wikipedia.org/wiki/Lint_%28software%29) means to analyze code for problems.
Here, it specifically means to check code for stylistic errors and inform the user of any such
violations.

To **format** here means to modify code in-place so that it conforms to style rules.

For information about our code style guidelines, see [this
document](https://github.com/supercollider/supercollider/wiki/%5BWIP%5D-C---Code-Style-Guidelines).

SuperCollider uses [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) - part of the
[LLVM](http://llvm.org/) project - to format C++ and Objective-C/C++ code. This ensures that the
style of the codebase is largely consistent across time and among differing authors, and makes code
review and contributing smoother for new and experienced contributors.

Formatting is checked for every commit and PR by our CI (continuous integration) tools. This makes
it impossible to merge any change which violates our formatting standards.

If you are contributing to SuperCollider and plan on working on C++ code, it is strongly recommended
that you integrate ClangFormat into your development workflow.

Possible workflows and scripts
------------------------------

Integrating ClangFormat with your editor is relatively straightforward for many commonly used
C++ editors. Instructions can be found [here](https://clang.llvm.org/docs/ClangFormat.html).

As an alternative, or if your editor does not support integration, we also provide a Python script
(in `tools/clang-format.py`) for linting and formatting your code. Shortcuts for running this script
are available as CMake targets and as Python scripts in your build directory. Run
`tools/clang-format.py -h` for full information.

### CMake targets

The following targets are provided in the build system:

- `lint`: lints all uncommitted changes to the working tree. The output will be in the form of a
  diff between your changes and correctly formatted code. If there are no changes, this target will
  exit without printing anything.
- `format`: makes exactly the changes shown by `lint`. Does not commit any changes.
- `lintall`: lints *all* files in the repository. This takes a long time.
- `formatall`: formats *all* files in the repository. This also takes a long time.

How you run them depends on your CMake generator of choice. For example, if you choose the Makefiles
generator, you would run `make lint`.

### Build directory scripts

In your build directory (usually, `/path/to/supercollider/build`), after running CMake, you will
have two Python scripts named `lint.py` and `format.py`. These behave like the `lint` and `format`
targets, but they also take an optional single argument, the name of a commit to diff against. For
instance, if you have a branch `feature` which is 3 commits ahead of `develop`, you can run
`./lint.py develop` to lint the C++ changes introduced on your feature branch (and nothing else).

This is useful for quickly reformatting an entire branch of changes if you've neglected to format
each commit, and don't want to go back and redo each commit separately -- although, we'd prefer if
you never have to do this at all! Whatever your method, you should get in the habit of formatting
your code *before* each commit.

### Example workflow

If you are developing a C++ feature or bug fix, a typical workflow might look like this:

1. Write some code, build, test
2. Use your editor's integration or run `build/format.py` to format your code.
3. Commit your changes with Git

Requirements
------------

**ClangFormat v8.0.0**: it is *extremely* important that all contributors use the same version of
ClangFormat. Style options are added and modified between releases, so even if an older or newer
version accepts our style file, its behavior may differ from our accepted version's.

You can probably download a package including ClangFormat from the [LLVM releases
page](https://releases.llvm.org/download.html); alternatively, check your package manager of choice.
If you can't find a suitable version for your operating system, [let us
know](https://github.com/supercollider/supercollider/blob/develop/README.md#discuss) and we'll be
happy to help you!

**Python**: if you want to use the `tools/clang-format.py` script, you will need Python. The script
has been tested and confirmed to work with versions 2.7.15 and 3.6.5. Newer versions will probably
also work; use older versions at your own peril. If you don't have Python installed on your system,
you can download it [here](https://www.python.org/downloads/). Prefer to use Python 3. Issues in the
way Python 2 handles non-ASCII characters mean that you may encounter unsolvable errors if:
- the full path to your repository includes a non-ASCII character
- one of the files you are linting contains a non-ASCII character

**clang-format-diff.py**: if you want to use the `lint` or `format` CMake target, or `lint.py` or
`format.py` script, you will need `clang-format-diff.py`, a Python script provided by LLVM that
reads in a Git diff and either lints or formats your code to agree with our style. This script is
generally provided in LLVM releases. You may need to manually add it to your PATH, though. For
instance, if you use the LLVM-provided installer for Windows, this script is in
`<install-path>/share/clang`, but the installer only adds `<install-path>/bin` to your PATH.

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