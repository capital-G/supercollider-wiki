Linting and formatting
======================

Here, "linting" specifically means checking that code is formatted correctly, without modifying code; "formatting" means
actually changing the code.

For information about our code style guidelines, which includes things like naming conventions, see [this
document](https://github.com/supercollider/supercollider/wiki/%5BWIP%5D-C---Code-Style-Guidelines).

SuperCollider uses [ClangFormat](https://clang.llvm.org/docs/ClangFormat.html) - part of the
[LLVM](http://llvm.org/) project - to format C++ and Objective-C/C++ code. This helps to make sure that the
style of the codebase is consistent across time and authors, and makes contributing and code
review smoother.

Formatting is checked for every commit and PR (pull request) by our CI (continuous integration) tools. This makes it
impossible to merge any change which violates our formatting standards. Only one CI job on Travis checks the linting
target; if your commit fails to build due to linting, you can check the build log to see why.

If you are contributing to SuperCollider and plan on working on C++ code, it is strongly recommended
that you integrate ClangFormat into your development workflow.

Getting started
---------------

You will need clang v8.x.y and Python 2.7+ or 3.6+. Instructions on grabbing the dependencies are here: 
1. Download and install Python and LLVM 8; either [8.0.1](https://releases.llvm.org/download.html#8.0.1) or
[8.0.0](https://releases.llvm.org/download.html#8.0.0) will work. See
[requirements](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#requirements) below for
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

On Windows, this is done through user settings; there are many articles online that explain how.

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
   clang-format that you installed.
2. You can run the `tools/clang-format.py` script directly; run `tools/clang-format.py -h` for more information.
3. You can run the `build/lint.py` and `build/format.py` scripts that are generated in your build folder. Both scripts
   accept a commit "reference point" as an optional first argument.
4. You can "build" some commands as build targets, see below.

### Example workflow

If you are developing a C++ feature or bug fix, a typical workflow might look like this:

1. Write some code, build, test
2. Use your editor's integration or run `./format.py` in your build directory to format your code
3. Commit your changes with git

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

Requirements
------------

**ClangFormat v8.x.y**: it is very important that all contributors use the same major version of
ClangFormat. Style options are added and modified between releases, and other small things may change between versions.
Any version that starts with 8 is acceptable.

On Arch Linux, there is no good package for clang8 (https://aur.archlinux.org/packages/clang8 conflicts with clang), and the clang-8 source code release does not compile with the latest clang or gcc version. This script will install it for you in a way that it peacefully coexists with other installations of clang: https://gist.github.com/brianlheim/2f80768eb2429b285902f8898182ae2d

You can probably download a package including ClangFormat from the [LLVM releases
page](https://releases.llvm.org/download.html); alternatively, check your package manager of choice.
If you can't find a suitable version for your operating system, [let us
know](https://github.com/supercollider/supercollider/blob/develop/README.md#discuss) and we'll be
happy to help you!

In the long term, we would like to not require a single and out-of-date version of clang-format.

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

I made a PR before the reformat and it has merge conflicts now! How do I fix it?
--------------------------------------------------------------------------------

If you have a branch that contains work prior to the major C++ reformatting commit, just follow these steps.

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
