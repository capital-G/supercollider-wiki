Style Guidelines
================

This is a living document reflecting the conventional style used for SuperCollider and C++ source code in this project. Each guideline here is presented with a brief discussion including examples, rationale, and importance.

SuperCollider
=============

The following guidelines apply to all SuperCollider code in the repository, including the SuperCollider class library and examples in documentation.

Whitespace
----------

Don't have additional whitespace at the beginning or end of a file. In class library files, there should be exactly one newline at the end in order to appease Git.

Avoid trailing whitespace at the end of lines. It's a good idea to set your editor to automatically remove it.

Binary operators, including key binary operators, should have one space before and after.

There should be no spaces inside parentheses `( )` and brackets `[ ]`. Curly braces `{ }` are "heavier" since they denote functions, so they should have exactly one space after the opening brace and one space before the closing brace.

C++
===

The following guidelines apply to C++ code for all four major components in the repository (sclang, scsynth, supernova, and scide).