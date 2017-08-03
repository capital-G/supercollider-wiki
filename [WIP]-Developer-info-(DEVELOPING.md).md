Purpose
=======

Record location & usage of various tools for developers and maintainers.

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

Download UnitTesting quark separately. Add the test suite folder to your SuperCollider compile paths. Recompile. UnitTest.runAll (<- check that)