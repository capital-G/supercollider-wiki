Purpose
=======

Document tools and practices for developers and maintainers of SuperCollider.

Practices
=========

Git Workflow
------------

GitFlow (TODO: incorporate, or link, to other document about this topic)

Milestones
----------

We use four tags to keep track of issues:

- Next patch (example: "3.9.1")
- Some patch (example: "3.9.x")
- Next minor (example: "3.10")
- Some minor (example: "3.x")

Patch-milestoned issues are those that will require bug fixes, while minor-milestoned issues are things like
new features and major changes that are better left for a minor release. The "Next patch"/"Next minor"
milestones mark those issues that we've decided _must_ be addressed before the next respective release. They're
either the most painful bugs or most requested features.

When, in the example milestones above, 3.10 is released, we would move all 3.9.x-milestoned issues to 3.10.x,
and then collectively decide which issues ought to move from 3.x to 3.11 and from 3.10.x to 3.10.1.

Standards
=========

New UGens
---------

New UGens should meet the following standards:

- **General software quality concerns:**
  - UGens in core should never break backward compatibility.
  - UGens should be fully documented, with a clear explanation of what it does and an appropriate collection of examples. Be sure to document which UGen inputs are modulatable at which rates.
  - UGens should be efficient. SuperCollider takes pride in being easy on the CPU, and UGens should help support that reputation.
  - The UGen should be deemed useful enough to the general SC user base.
  - Each UGen should be in a separate C++ source file (or multiple source files if it's really that long).
  - Don't leave any unnecessary print statements lying around.
- **Safety:**
  - Check input rates in the sclang class.
  - Any calls to `RTAlloc` should be protected from `RTAlloc` returning a null pointer. This usually happens when there isn't enough real-time memory left, and results in a **server crash** if unprotected.
  - The Ctor sample should be initialized. If this is not done, very nasty bugs can occur.
  - Zap dangerous values (subnormals, infinities, nans) in feedback loops to 0. SC provides a `zapgremlins` function that does this for you.
- **Utility:**
  - UGens should have both `.ar` and `.kr` methods if applicable.
  - Sample rate and block size independence should be maintained if applicable. For example, audio UGens shouldn't sound radically different if the sample rate is increased.
  - For audio UGens, control-rate inputs should be interpolated if applicable.
  - Don't arbitrarily make certain inputs nonmodulatable just for programming convenience -- carefully anticipate what's worth modulating. Either way, don't forget to document it.
- **Modernization and deprecated features:**
  - When writing a new UGen from scratch, it is recommended to use the modern C++ style seen in `SC_PlugIn.hpp`.
  - Don't use `mul` and `add` arguments. These were originally introduced for efficiency, but now `Foo.ar * 2 + 1` gets optimized into a `MulAdd`.
  - Don't use a `doneAction` argument. Set the done flag instead.

Tools
=====

Boost Update Script
-------------------

Location: `external_libraries/extract_boost.sh`, `external_libraries/boost_sc_changes.patch`

### Purpose

Update Boost libraries packaged with SuperCollider, and apply the SuperCollider organization's patches for Boost.

### Usage

Should be run as soon as possible after a new release of Boost. See instructions in `external_libraries/README_BOOST.md` for more information.

sclang Lexer, Parser, & Compiler Regression Test Suite
------------------------------------------------------

### Purpose

TODO

### Usage

TODO

QtGUI Debug Capability
----------------------

### Purpose

Print verbose debug messages while diagnosing issues with the Qt GUI features.

### Usage

Only enabled on a debug build.

```sclang
QtGUI.debugLevel_(0) // 0 = no output, 3 = verbose
```

Test Suite
----------

### Purpose

Unit testing suite for SuperCollider language core library

### Usage

If developing on a version older than 3.9.0, download `UnitTesting` quark separately. Add the test suite folder to your SuperCollider compile paths. Recompile. Run `UnitTest.runAll`, or run tests from the GUI via `UnitTest.gui`.

### Continuous automatic red/green testing via guard-sclang

Rather than manually running appropriate tests after editing a library class or a `UnitTest` class, you can use [aspiers/guard-sclang](https://github.com/aspiers/guard-sclang) which will watch for file changes and automatically run tests in reaction to them.  The steps to set this up are as follows:

- Make sure you have Ruby installed.
- Make sure you have [Bundler](http://bundler.io/) installed (usually this is as simple as running `gem install bundler`).
- Make sure `sclang` is somewhere on your `$PATH`.
- `cd $supercollider_source/tools/guard`
- `bundle install` 

Now you should be ready to launch Guard via:

    bundle exec guard

Then start hacking on SuperCollider classes, and enjoy the immediate feedback! 

The mapping between implementation classes and test classes is defined in `tools/guard/Guardfile`.  This is currently by far from perfect, because it naively assumes a 1:1 mapping between class `Foo` and test class `TestFoo`.  However it should be easy to make it more intelligent, even if you don't know Ruby; please feel free to contribute improvements!

Changelog-to-schelp script
--------------------------

Location: https://gist.github.com/brianlheim/443ae188dee8f7a85e7f34c04cc66d2b

### Purpose

Converts a changelog in markdown format into schelp format. A little extra work required but saves a lot of tedium. See script for usage.

Specific Contribution Workflows
===============================

Updating translation files
--------------------------

To update translation files for the IDE, you'll first need to make sure Qt's `lupdate` program is in your path, then build the `update_ide_translations` CMake target. This will overwrite the `.ts` files in `editors/sc-ide/translations` to reflect the most recent source code.

Adding IDE translations
-----------------------

Use [Qt Linguist](http://doc.qt.io/qt-5/qtlinguist-index.html) to update the `.ts` files in `editors/sc-ide/translations`. Qt Linguist can be included when you install Qt Creator or a general Qt distribution.

### Adding a new translation language

If you can't find the language you want to add translations for, first make sure you have `lupdate` and Qt Linguist, then:

1. Determine its two-letter [language code](https://www.loc.gov/standards/iso639-2/php/code_list.php).
2. Add a new filename for it in `editors/sc-ide/CMakeLists.txt`, in the section marked `# Translation files`.
3. Re-run the CMake generation phase (in your `build` directory, execute `cmake ..`)
4. Build the `update_ide_translations` CMake target to generate a `.ts` file
5. Add translations using Qt Linguist.

Adding to QtCollider widgets
----------------------------

These instructions detail how to add functionality to existing QtCollider widgets (such as TreeView and Knob). Each widget typically corresponds to a single Qt class, and the simplest way to add functionality is by providing access to an existing C++ function of the Qt widget.

1. Locate the C++ source for the widget in `/QtCollider/widgets/`.
2. Add the signature for the function in the header file.
3. Add the implementation for the function in the implementation file.
4. Locate the SC source for the widget in `/SCClassLibrary/Common/GUI/Base/`.
5. Add a suitably named new method in the class file that calls down to the QtCollider widget using `invokeMethod`.
6. Document the method in the corresponding schelp file in `/HelpSource/Classes/`.

Technical note: not all types can be transcoded between SuperCollider and QtCollider widgets. However, all primitive types, some collection types, and a few class types are supported. The code which controls this can be found in `QtCollider::MetaType::find( PyrSlot * )`.

### Example

[PR #3560](https://github.com/supercollider/supercollider/pull/3560) demonstrates how to do this by adding `setColumnWidth` to `TreeView`:

1. The C++ files are `/QtCollider/widgets/QcTreeWidget.{cpp,h}`
2. The function signature is:

```cpp
Q_INVOKABLE void setColumnWidth( int column, int width );
```

3. The implementation simply calls up to `QTreeView`:

```cpp
void QcTreeWidget::setColumnWidth( int column, int width )
{
  QTreeWidget::setColumnWidth( column, width );
}
```

4. The SC file is `/SCClassLibrary/Common/GUI/Base/QTreeView.sc`
5. The new method simply forwards arguments to `invokeMethod`:

```supercollider
setColumnWidth { arg column, width;
	this.invokeMethod( \setColumnWidth, [column, width] )
}
```

6. The documentation is added to `/HelpSource/Classes/TreeView.schelp`:

```
METHOD:: setColumnWidth

ARGUMENT:: column
	The integer index of the column to modify
ARGUMENT:: width
	Integer width in pixels
```