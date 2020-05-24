If you'd like to start contributing to SC, there are a few things you will need to do to prepare your environment.

First, you will need everything you normally need to build SuperCollider on your system. Check the platform-specific README for instructions. Try to build SuperCollider at least once first before modifying any code, so you know this part of your environment is set up correctly, and the issues are due to anything you touched.

### For C++ contributions

To contribute C++ code, you will need to install the tools necessary to run our automatic linting and formatting scripts. You can find more information about requirements [here](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#requirements), and how to use these scripts [here](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions#possible-workflows-and-scripts).

### For schelp and SuperCollider contributions

In order to contribute code in the SuperCollider language and documentation in schelp, the easiest thing to do is to point sclang toward the files in SCClassLibrary and testsuite, and nothing else. This removes any possibility of interference from extensions and startup files, and will also ensure that the help browser and documentation renderer use the schelp files you are editing.

We would like to have a better workflow for this, but for now, here is a simple way to get set up:

1. Run this SuperCollider code to create a 'developer' sclang config file:

```supercollider
// edit this to the appropriate path!
~scGitPath = "/path/to/your/supercollider";

// add paths from your clone
LanguageConfig.addIncludePath(~scGitPath +/+ "SCClassLibrary");
LanguageConfig.addIncludePath(~scGitPath +/+ "testsuite");

// disable startup files
LanguageConfig.addIncludePath(~scGitPath +/+ "plaform/disable_startup_files");

// disable default search paths
LanguageConfig.addExcludePath(Platform.systemExtensionDir);
LanguageConfig.addExcludePath(Platform.userExtensionDir);
LanguageConfig.addExcludePath(Platform.resourceDir +/+ "SCClassLibrary");

// enable developer-oriented warning
LanguageConfig.postInlineWarnings = true;

~scConfPath = Platform.userConfigDir +/+ "sclang_dev_config.yml";
LanguageConfig.store(~scConfPath);
postln("Language config stored to" + ~scConfPath);
```

2. In your IDE preferences, set this to be the sclang config file, and reboot sclang. In SCIDE, you can do this in the Preferences dialog. If you are using sclang by itself on the command line, run it with `-l path/to/sclang_dev_config.yml`.