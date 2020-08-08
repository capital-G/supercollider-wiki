Adding translations for the IDE is very helpful and makes SC easier to use for people whose first language is not English. To contribute translations, you will need the following:

- A local clone of the repository. See ["Setting up your development environment"](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment) for more instructions. You don't need to build SC to contribute translations, you only need to clone the repository.
- QtLinguist, part of the Qt project. You can download the installer from [Qt's website](https://www.qt.io/).

Updating translation files
--------------------------

Before starting to make translations, you can optionally make sure the translation file you'll be working on is up to date with the source code. This is a good thing to do if you have the time.

To update translation files for the IDE, you'll first need to find Qt Linguist's `lupdate` program where it was installed, and then execute the following command from the root of the repo:

    /path/to/lupdate editors/sc-ide -ts editors/sc-ide/translations/<file>

where `<file>` is the translation file you want to update. All the translation files are in `editors/sc-ide/translations`.

You can also update all translation files at once by having `lupdate` in your PATH and building the `update_ide_translations` build target.

Adding IDE translations
-----------------------

Use [Qt Linguist](http://doc.qt.io/qt-5/qtlinguist-index.html) to update the `.ts` files in `editors/sc-ide/translations`. Complete instructions for using Qt Linguist can be found [on Qt's website](https://doc.qt.io/qt-5/linguist-translators.html).

### Adding a new translation language

If you can't find the language you want to add translations for, first make sure you have `lupdate` and Qt Linguist, then:

1. Determine its two-letter [language code](https://www.loc.gov/standards/iso639-2/php/code_list.php).
2. Add a new filename for it in `editors/sc-ide/CMakeLists.txt`, in the section marked `# Translation files`.
3. Re-run the CMake generation phase (in your `build` directory, execute `cmake ..`)
4. Build the `update_ide_translations` CMake target to generate a `.ts` file
5. Add translations using Qt Linguist.

Testing translations
--------------------

TODO

Submitting translations
-----------------------

When you're ready to contribute your translations back to the project, follow the instructions for [creating a pull request](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests). Thanks!!