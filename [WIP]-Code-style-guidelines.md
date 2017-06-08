Style Guidelines
================

This is a living document reflecting the conventional style used for SuperCollider and C++ source code in this project. Each guideline here is presented with a brief discussion including examples, rationale, and importance.

How to read this document
-------------------------

There are two categories of guidelines: *Rules* should be followed strictly; *Recommendations* are looser preferences. Existing code should conform to all *Rules*, but *Recommendations* are suggestions for new and existing contributors who may be interested in the discussion surrounding the topic.

Rules marked with "[needs discussion]" are potentially controversial and have not yet been agreed upon.

SuperCollider
=============

The following guidelines apply to all SuperCollider code in the repository, including the SuperCollider class library and examples in documentation.

Whitespace
----------

### End-of-file newline

#### *Rule:* Use exactly one newline at the end of a file.

Git considers a file without a terminating newline to be malformed, and will complain when you commit a change without one!

### Trailing whitespace

#### *Rule:* Don't end lines with whitespace characters.

This keeps diffs clean as it prevents accidental whitespace from being committed. Other users whose editors automatically strip trailing whitespace will be forced to either redo your mistake or commit unnecessary changes. If your editor supports automatically removing trailing whitespace, consider turning that behavior on.

### Spaces in expressions and statements

#### [needs discussion] *Rule:* Use spaces around binary operators

Binary operators, including key binary operators, should have one space before and after.

#### [needs discussion] *Rule:* Add spaces after commas.

Commas should have one space after, but not before. 

#### *Rule:* Use spaces before semicolons.

Semicolons should immediately follow the end of the statement, with no additional space.

```supercollider
x = 3 + 5 ; // questionable
x = 3 + 5;  // better
```

#### [needs discussion] *Rule:* Add spaces within curly brackets, but not parentheses or square brackets.

In inline form, there should be no spaces inside parentheses `( )` or square brackets `[ ]`. Curly braces `{ }` delimit functions, and should have exactly one space after the opening brace and one space before the closing brace.

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

#### [needs discussion] *Rule:* Use K&R style for multi-line blocks

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

#### [needs discussion] *Rule:* keep method calls compact

In the most common method call syntaxes, don't put whitespace around the period, and don't put whitespace between the method name and the parentheses:

```supercollider
// good:
foo.value(bar)
value(foo, bar)

// bad:
foo . value(bar)
foo.value (bar)
value (foo, bar)
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

C++
===

The following guidelines apply to C++ code for all four major components in the repository (sclang, scsynth, supernova, and scide).