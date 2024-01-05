
(development-environment-setup)=
# Setting up your development environment

If you'd like to start contributing to SuperCollider, there are a few things you will need to do to prepare your environment.

First, you will need everything you normally need to build SuperCollider on your system. Check the platform-specific README for instructions. Try to build SuperCollider at least once first before modifying any code, so you know this part of your environment is set up correctly, and the issues are due to anything you touched.

Checklist:

- GitHub account
- `git` installed on your computer
- Personal fork of SuperCollider's code
- Fork setup for updates
- Additional tooling, depending on the kind of contributions you're interested in making (e.g. C++, sclang and/or documentation)

## 1. Setup your fork

To contribute to SuperCollider, you'll need to get your personal working copy of its source code, called a fork. From there you'll be able to make your changes and submit them to the community through Pull Requests.
If you have created your fork before, bring it up-to-date with the SuperCollider repository. See ["Keep your fork updated"](#keep-your-fork-updated) below for details.

SuperCollider's source code is hosted on GitHub, using `git` as a version control system. If you are new to Git and GitHub, notice that they are two different things: `git` is free version control software, and GitHub is a web platform to facilitate sharing of git projects. You'll need to create a GitHub account and setup `git` on your computer. For more informations about installing and configuring git, you can referer for example to [this guide from GitHub](https://docs.github.com/en/github/getting-started-with-github/set-up-git).

1. [Create a fork](https://github.com/supercollider/supercollider/fork) of the SuperCollider repository. This procedure will prompt you to create a GitHub account, if you don't have one already.
2. Clone the repo and its submodules locally. This command creates a new folder called "supercollider" in your current directory:

```shell
git clone --recursive https://github.com/your-name/supercollider.git
```

(keep-your-fork-updated)=
## 2. Keep your fork updated

In order to keep your fork up-to-date, you need to point it to the main SuperCollider repository. This is done by adding the main repository as a remote, usually called `upstream`. **Please note:** naming the main repository `upstream` is just a convention, not a requirement. If you already have a differently named remote pointing to the main SuperCollider repository, you can use that name instead.

- If you haven't yet added the `upstream` remote, you can add it by doing the following:
	- Check the list of remotes: `git remote -v`. The output should look like this:

			origin	https://github.com/your-name/supercollider.git (fetch)
			origin	https://github.com/your-name/supercollider.git (push)

	- Add a new remote called `upstream`, pointing to the SuperCollider repository:

			git remote add upstream https://github.com/supercollider/supercollider.git

	- Check the list of remotes again: `git remote -v`. Now the output should look like this:

			origin	https://github.com/your-name/supercollider.git (fetch)
			origin	https://github.com/your-name/supercollider.git (push)
			upstream	https://github.com/supercollider/supercollider.git (fetch)
			upstream	https://github.com/supercollider/supercollider.git (push)

	- You can now proceed to update your fork.
- If you've already added the `upstream` remote, you can update your fork by doing the following:
	- Be sure to have all local changes committed before proceeding with the update
	- Fetch changes made to the `upstream` repository: `git fetch upstream`
	- Checkout the `develop` branch: `git checkout develop`
	- Pull changes into the `develop` branch: `git pull upstream develop`. Your `develop` branch is now up-to-date.
	- If you've already created your topic branch, you can update it with the changes in `develop` by either rebasing or pulling - see [rebasing and merge conflicts](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests#rebasing-and-merge-conflicts).
	- If you haven't yet created your topic branch, proceed to creating it as described in [Creating Pull Requests](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests#Create-a-topic-branch).

## 3. Tooling and contribution-type based setup

### For C++ contributions

To contribute C++ code, you will need to install the tools necessary to run our automatic linting and formatting scripts. You can find more information about requirements [here](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#requirements), and how to use these scripts [here](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#possible-workflows-and-scripts).

### For schelp and SuperCollider contributions

In order to contribute code in the SuperCollider language and documentation in schelp, the easiest thing to do is to point sclang toward the files in SCClassLibrary and testsuite, and nothing else. This removes any possibility of interference from extensions and startup files, and will also ensure that the help browser and documentation renderer use the schelp files you are editing.

We would like to have a better workflow for this, but for now, here is a simple way to get set up:

1. Run this SuperCollider code to create a 'developer' sclang config file:

   ```text
   // edit this to the appropriate path!
   ~scGitPath = // "/path/to/your/supercollider";
   
   // disable every currently included search path (defaults, extensions, manually-added ...)
   LanguageConfig.includePaths.do(LanguageConfig.removeIncludePath(_));
   // disable startup files
   LanguageConfig.addIncludePath(~scGitPath +/+ "platform/disable_startup_files");
   
   // exclude default paths (important! otherwise you'll get "duplicate Class found" errors and the interpreter won't start)
   LanguageConfig.excludeDefaultPaths = true;
   
   // add paths from your clone
   LanguageConfig.addIncludePath(~scGitPath +\/+ "SCClassLibrary");
   LanguageConfig.addIncludePath(~scGitPath +\/+ "testsuite");
   
   // enable developer-oriented warning
   LanguageConfig.postInlineWarnings = true;
   
   ~scConfPath = Platform.userConfigDir +\/+ "sclang_conf_development.yaml";
   LanguageConfig.store(~scConfPath);
   postln("Language config stored to" + ~scConfPath);
   ```
  
2. In your IDE preferences, set this to be the sclang config file, and reboot sclang. In SCIDE, you can do this in the Preferences dialog. If you are using sclang by itself on the command line, run it with `-l path/to/sclang_conf_development.yml`.
3. When you want to switch back to using sclang for your own enjoyment, simply swap the config file to what it was previously.

### C++ changes, sclang, and SCIDE

The IDE runs sclang using PATH on Windows and Linux, and assumes an App Bundle directory structure on macOS. This presents a difficulty if you want to use SCIDE to test C++ changes to sclang, because it may accidentally use your system installation of sclang.

The way to manage this is different on each platform:

- MacOS: always use the app bundle from the `install` or `SuperCollider` targets to run the IDE.
- Linux: run the IDE with `PATH="/directory/with/sclang:$PATH" /path/to/scide` (don't include `sclang` in the path, just its containing directory).
- Windows: since sclang is not usually in PATH by default, and "." is, always run the IDE from the `install` target.
