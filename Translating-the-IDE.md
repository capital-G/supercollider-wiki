Updating translation files
--------------------------

To update translation files for the IDE, you'll first need to make sure Qt's `lupdate` program is in your path, then
build the `update_ide_translations` CMake target. This will overwrite the `.ts` files in `editors/sc-ide/translations`
to reflect the most recent source code.

Adding IDE translations
-----------------------

Use [Qt Linguist](http://doc.qt.io/qt-5/qtlinguist-index.html) to update the `.ts` files in
`editors/sc-ide/translations`. Qt Linguist can be included when you install Qt Creator or a general Qt distribution.

### Adding a new translation language

If you can't find the language you want to add translations for, first make sure you have `lupdate` and Qt Linguist, then:

1. Determine its two-letter [language code](https://www.loc.gov/standards/iso639-2/php/code_list.php).
2. Add a new filename for it in `editors/sc-ide/CMakeLists.txt`, in the section marked `# Translation files`.
3. Re-run the CMake generation phase (in your `build` directory, execute `cmake ..`)
4. Build the `update_ide_translations` CMake target to generate a `.ts` file
5. Add translations using Qt Linguist.