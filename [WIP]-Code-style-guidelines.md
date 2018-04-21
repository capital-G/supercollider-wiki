Style Guidelines
================

This is a living document reflecting the conventional style used for SuperCollider and C++ source code in this project. Each guideline here is presented with a brief discussion including examples, rationale, and importance.

How to read this document
-------------------------

There are two categories of guidelines: *Rules* should be followed strictly; *Recommendations* are looser preferences. Existing code should conform to all *Rules*, but *Recommendations* are suggestions for new and existing contributors who may be interested in the discussion surrounding the topic.

Rules marked with "[needs discussion]" are potentially controversial and have not yet been agreed upon.

General
=======

TODOs
-----

When a bug or feature is critical or hard to solve, it's OK to sometimes fix the problem in a way that's less than ideal. If you do, make sure to include a note about why the fix exists, along with the text `TODO` and/or `FIXME` so that it can be easily found by developers later. You never know who might come along and have the proper knowledge to solve the problem correctly!

SuperCollider
=============

The following guidelines apply to all SuperCollider code in the repository, including the SuperCollider class library and examples in documentation.

Whitespace
----------

### End-of-file newline

#### *Rule:* Use exactly one newline at the end of a file.

Git considers a file without a terminating newline to be malformed, and will complain when you commit a change without one! You can set your editor to fix this behavior.

### Trailing whitespace

#### *Rule:* Don't end lines with whitespace characters.

This keeps diffs clean as it prevents accidental whitespace from being committed. Other users whose editors automatically strip trailing whitespace will be forced to either redo your mistake or commit unnecessary changes. If your editor supports automatically removing trailing whitespace, consider turning that behavior on.

### Spaces in expressions and statements

#### [needs discussion] *Rule:* Use spaces around binary operators

Binary operators, including key binary operators, should have one space before and after.

#### [needs discussion] *Rule:* Add spaces after commas.

Commas should have one space after, but not before.

#### *Rule:* Don't use spaces before semicolons.

Semicolons should immediately follow the end of the statement, with no additional space.

```supercollider
x = 3 + 5 ; // incorrect
x = 3 + 5;  // correct
```

#### [needs discussion] *Rule:* Add spaces within curly brackets, but not parentheses or square brackets.

When written on a single line, there should be no spaces inside parentheses `( )` or square brackets `[ ]`. Curly braces `{ }` delimit functions, and should have exactly one space after the opening brace and one space before the closing brace.

```supercollider
// correct:
a = f.value(10);
b = [1, 2, 3];
c = b.collect({ |x| x + 3 });

// incorrect:
a = f.value( 10 );
b = [ 1, 2, 3 ];
c = b.collect({|x| x + 3});
```

### Indentation

#### *Rule:* use tabs for indentation.

The SuperCollider class library uses tabs for indentation.

#### *Rule:* Use K&R style for multi-line blocks

For all three bracket types, use [K&R indent style](https://en.wikipedia.org/wiki/Indent_style#K.26R). The open brace comes at the end of the first line, rather than on a separate line.

```supercollider
// correct
x = {
    y = y + 1;
    3.rand
};

// Allman style: avoid
x = 
{
    y = y + 1;
    3.rand
};
```

### Method calls

#### *Rule:* don't space around `.`

`.` may be used either inline or multiline. Inline, don't put any space around it.

```supercollider
// good:
foo.value(bar)

// bad:
foo . value(bar)
```

In long chains of method calls on the same object, it may be beneficial to split the method call across two lines. The dot should be on the second line, not the first, and it should be indented one level. Don't put whitespace between the dot and the method name.

```supercollider
Button()
    .states_([["blorp", nil, nil]])
    .action_({
        "hey hey hey".postln
    });
```

Methods and functions
---------------------

### Parameter lists

#### *Rule:* Use pipes instead of the `arg` keyword to express parameter lists.

The pipe-enclosed parameter list is used in most modern code, and mimics parameter lists in Smalltalk. Programmers coming from languages other than Smalltalk may also find that it appears closer to C-family function signature notation.

Although the SuperCollider compiler will allow commas to be omitted in parameter lists, adding them makes for clearer code, especially when default arguments are provided.

```supercollider
// good:
x = { |foo = 3, bar = 4| /* ... */ };

// bad, unclear:
x = { |foo = 3 bar = 4| /* ... */ };
// bad, outdated notation:
x = { arg foo = 3, bar = 4; /* ... */ };
```

This rule was discussed [here](https://github.com/supercollider/supercollider/issues/2913).

#### *Rule:* Place the parameter list on the same line as the opening curly bracket of a function or method.

As explained in the previous rule, this is closer to conventional Smalltalk style and reads like a parameter list in C-family languages.

```supercollider
// good:
x = { |foo = 3, bar = 4|
    foo + bar;
};

// bad:
x = {
    |foo = 3, bar = 4|
    foo + bar;
};
```

This rule was discussed [here](https://github.com/supercollider/supercollider/issues/2913).

### Return statements

#### *Recommendation:* don't place a semicolon after the final statement of a method or function.

Expressions that are followed by a semicolon suggest that another expression follows. A function return value isn't followed by any other statement. In this way, omitting the optional semicolon after the final statement of a method or function can serve to indicate an intentional return value.

When code within a method or function changes frequently, missing semicolons may trip up the programmer as statements are reordered. A similar risk appears in methods where the last return statement is likely to be amended with further return cases. In those situations, it may make more sense to retain the final semicolon.

```supercollider
ExampleClass {
    exampleMethod { |a, b|
        var c = a + b;
        ^c.asString
    }
}
```

```supercollider
f = { |a, b|
    var c = a + b;
    c.asString // semicolon omitted here marks this as the intended return value
}
```

This rule was discussed [here](https://github.com/supercollider/supercollider/issues/2914).

Arrays and Collections
----------------------

### Multi-line arrays

#### [needs discussion] *Rule:* Place each element of a multi-line array on its own line.

Each element should be on a separate line:

```supercollider
x = [
    "foo",
    "bar",
    "baz"
];
```

### Abbreviated symbol syntax

#### [needs discussion] *Rule:* Only use abbreviated symbol syntax in appropriate contexts.

The abbreviated symbol syntax `[foo: "bar"]` should only be used in contexts that accept alternating symbols and other values. It's a good idea to use it in, e.g., `Pbind` and `Pmono`.

#### [needs discussion] *Rule:* Don't mix abbreviated symbol and basic array syntaxes.

If an array uses the abbreviated symbol syntax, it should use only the abbreviated symbol syntax and not mix it with bare items:

```supercollider
// good:
Pmono(\lead, *[
    degree: Pseq([0, 1, 2, 3])
]);

// bad:
Pmono(*[
    \lead,
    degree: Pseq([0, 1, 2, 3])
]);
```

SCDoc (.schelp)
===============

The following guidelines apply to schelp files in `/HelpSource`.

### Tag capitalization

Prefer using the lowercase forms of tags (`code:: ::`, `method::`), unless this would break with convention in the context being edited.

### Indentation

Use tabs for indentation, both for schelp-formatted text and code examples.

### Private methods

Hide all of a class's private methods using `private::`.

### Method documentation

Prefer using `argument::` and `returns::` instead of the method description body to document parameters and return values.

Either all of the parameters and/or return value should be documented, or none should be.

When documenting a parameter or return value, make sure to include the expected type.

C++
===

The following guidelines apply to C++ code throughout the project.

### Indentation

A mix of indentation styles is used in the C++ source code. In the near future, [all C++ code will be converted to use 4-space indentation](https://github.com/supercollider/supercollider/issues/2819). New files and new large sections within existing files should conform to 4-space indentation. In all other cases, please follow the pre-existing convention in the surrounding code.

### Whitespace

#### `if`, `for`, `while`, `switch`

Use one space after `if`, `for`, `while`, and `switch`, before the open paren. If the statement includes an open bracket, and the code is in K&R brace style (the open bracket is on the same line), use one space between the close paren and open bracket.

```cpp
// correct
if (condition)

// incorrect
if(condition)

// correct
while (condition) {
    /* ... */
}

// incorrect
while (condition){
    /* ... */
}
```

### Statements

#### One statement per line

Have at most one statement per line. This makes it easier to set breakpoints while debugging, and is generally clearer.

```cpp
// correct
if (condition)
    return 3;

// incorrect
if (condition) return 3;

// correct
a++;
b++;

// acceptable
a++, b++;

// incorrect
a++; b++;
```

Other files
===========

These rules apply to source files in all other formats (CMake, Python, Bash, Batch, etc.), unless otherwise specified.

### Indentation

Prefer 4-space indentation for new code.