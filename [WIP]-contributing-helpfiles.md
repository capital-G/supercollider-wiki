_Note: This document is still a draft_
## Contributing documentation changes
This document is aimed at helping new contributors, whose first contribution is perhaps a small change in SuperCollider's Help files. For a more involved workflow, aimed at more experienced contributors, see [below](#Previewing-your-changes).

Eli Fieldsteel made an excellent [video tutorial](https://www.youtube.com/watch?v=CbIwWsGl-zc), especially directed to beginners, that walks through the whole process of fixing a typo in a Help file, from installing git to submitting the changes.


Contributing documentation needs the same setup as any other change to the source code. However, for small documentation changes, i.e. everything that doesn't require you to see a preview (e.g. typos, punctuation, extra repetitions), building SuperCollider is not needed, and you don't need any extra developer tool apart from a text editor and git.

You'll need to setup your fork of SuperCollider, make your changes and open a Pull Request

### Setting up your development environment
First step is to get your own updated working copy of the source code, called a fork. If you don't have one already, please see [Setting Up Your Development Environment]() for instructions to create your fork and to keep it updated.

### Making a documentation change
Once you have your fork cloned on your local machine, it's a recommended practice to create a new branch for every contribution you make. It makes it easier to organize your changes, and later publish them as Pull Requests, ensuring every contribution is isolated and thus easier to review, discuss and merge.
For this example, we are going to pretend to fix a typo in SinOsc's help file, so we create a new branch and we decide to name it `topic/help-sinosc-typo`:

    $ git checkout -b topic/help-sinosc-typo

Now it's time to find the .schelp file you want to modify. All .schelp files live in a folder called `Help Source`, inside the base folder of your fork, where you can search or browse with your operating system tools.
Alternatively, when you look at an Help file in the Help Browser (or online), you'll find a line at the bottom starting with `helpfile source:`, which will give you the path to its relative .schelp file. You are interested only in the part after "/HelpSource". For example, for SinOsc, you'll see something like:

    helpfile source: /usr/local/share/SuperCollider/HelpSource/Classes/SinOsc.schelp

And then you know that the source for SinOsc is in Classes/SinOsc.schelp, inside the HelpSource folder in your fork.

Once you've found it, open the .schelp file in a text editor and make the changes you want. When you are satisfied, you can proceed to publish your changes. Previewing them requires a few more steps, including building SuperCollider, see [below](#Previewing-your-changes) if you're interested, but feel free to skip it if your changes are small and you don't want to go through additional setup.

### Publishing your changes
Now that you have modified one or more files, the command `git status` will show a red entry for every modified files, calling them "Changes not staged for commit". To publish your changes you first need to stage them, which means to add them to your next commit:

    git add .

This command stages all modified files in any subdirectory of your current location. If you run `git status` now, you will see your modified files as green entries. Staged files will constitute your publishable change, called a commit. Create a commit with a meaningful, short message:

    git commit -m "help: SinOsc: fix typos [skip ci]"

And then push your branch to the remote server:

    git push --set-upstream origin topic/help-sinosc-typo

_For more about Pull Requests, branch naming conventions and [skip ci], see [Creating Pull Requests](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests)_

Now your branch contains a commit, which is constituted by your changes! The next part is to create a Pull Request, so that other developers will be able to see, discuss and approve your changes. GitHub offers a quick way to do this, if you go to (supercollider/supercollider)[https://github.com/supercollider/supercollider] shortly after making a change, it will prompt you to "Compare & Pull Request" your newly modified branch. Follow the instructions to add a description to your Pull Request, mark it as a documentation change, check all the checkboxes (since doc changes requires no testing, you can mark that "Code is tested" and "All tests are passing"), and finally "Create Pull Request".

### Your Pull Request, after you've published it
Congratulations on your Pull Requests, and thanks for taking the time to contribute to SuperCollider! After a Pull Request is published, it will be reviewed by at least one other developer and, if necessary, changes will be requested before it can be approved. You will receive notifications from GitHub whenever the discussion about your Pull Requests is updated (comments, requests for changes, approval).
Finally, the Pull Request will be accepted and your changes included in SuperCollider. Thanks!


### Previewing your changes

To see your changes in ScIDE's Help Browser, or any web browser, .schelp files need to be converted to HTML. Sclang, which does this conversion, needs to check with the class library, and all other help files, for broken links and undocumented methods.

It is recommended to build sclang from source, to ensure it can compile the class library that comes with that source. Skipping this step is possible, but it could lead to sclang being unable to start, in case your sclang version is incompatible with the class library from your source.
For instructions to build SuperCollider from source, please refer the specific README for your platform.

Next you have mainly two options:
- If you install and run the SuperCollider version you built from source, follow these instructions to [create and use a developer config file](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment#For-schelp-and-SuperCollider-contributions).
- If you just want to render html Help Files to a folder, you can use a special build target. During configuration, pass `-DSC_DOC_RENDER=ON` to CMake. This provides a target called `doc` which can be built to render all schelp documents:

    cmake .. -DSC_DOC_RENDER=ON # <other options>
    cmake --build . --target doc

Help files will be rendered in `YOUR/BUILD/FOLDER/RenderedHelp`
