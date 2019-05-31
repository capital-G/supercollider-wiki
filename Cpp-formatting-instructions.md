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

Rebasing a pre-reformat branch
------------------------------

If you have a branch that contains work prior to the major C++ reformatting commit, you can rebase
it easily with the `tools/clang-format.py` script in this repository. Run `tools/clang-format.py -h`
for more information.

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