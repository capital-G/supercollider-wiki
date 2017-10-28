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