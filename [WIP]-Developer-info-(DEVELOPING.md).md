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

- UGens in core should never break backward compatibility.
- The UGen should be deemed useful enough to the general SC user base.
- The Ctor sample should be initialized. If this is not done, very nasty bugs can occur.
- Any calls to `RTAlloc` should be protected from `RTAlloc` returning a null pointer. This usually happens when there isn't enough real-time memory left, and results in a server crash if unprotected.
- Zap dangerous values (subnormals, infinities, nans) in feedback loops to 0. SC provides a `zapgremlins` function that does this for you.
- Don't leave any unnecessary print statements lying around.
- Sample rate and block size independence should be maintained if applicable. For example, audio UGens shouldn't sound radically different if the sample rate is increased.
- For audio UGens, control-rate inputs should be interpolated if applicable.
- Don't use `mul` and `add` arguments. These were originally introduced for efficiency, but now `Foo.ar * 2 + 1` gets optimized into a `MulAdd`.
- UGens should have both `.ar` and `.kr` methods if applicable.
- Don't use a `doneAction` argument. Set the done flag instead.
- UGens should be efficient. SuperCollider takes pride in being easy on the CPU, and UGens should help support that reputation.

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

If developing on a version older than 3.9.0, download `UnitTesting` quark separately. Add the test suite folder to your SuperCollider compile paths. Recompile. UnitTest.runAll (<- check that)

Changelog-to-schelp script
--------------------------

Location: https://gist.github.com/brianlheim/443ae188dee8f7a85e7f34c04cc66d2b

### Purpose

Converts a changelog in markdown format into schelp format. A little extra work required but saves a lot of tedium. See script for usage.

