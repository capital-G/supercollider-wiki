Style Guidelines
================

This is a living document reflecting the conventional style used for SuperCollider and C++ source code in this project. Each guideline here is presented with a brief discussion including examples, rationale, and importance.

SuperCollider
=============

The following guidelines apply to all SuperCollider code in the repository, including the SuperCollider class library and examples in documentation.

Whitespace
----------

### General guidelines

#### Avoid using additional whitespace at the beginning or end of a file.

Use exactly one newline at the end of a file. Git considers a file without a terminating newline to be malformed, and will complain when you commit a change without one!

#### Avoid trailing whitespace at the end of lines.

This keeps diffs clean as it prevents accidental whitespace from being committed. Other users whose editors automatically strip trailing whitespace will be forced to either redo your mistake or commit unnecessary changes. If your editor supports automatically removing trailing whitespace, consider turning that behavior on.

### Spaces in expressions

#### *[needs discussion]* Binary operators

Binary operators, including key binary operators, should have one space before and after.

#### *[needs discussion]* Commas

Commas should have one space after, but not before. 

#### Semicolons

No space should go before semicolons.

```supercollider
x = 3 + 5 ; // questionable
x = 3 + 5;  // better
```

#### *[needs discussion]* Brackets and parentheses

The three kinds of brackets, `( ) [ ] { }`, may be used either inline or multiline:

```supercollider
// inline:
foo.do { |bar| bar.postln };

// multiline:
foo.do { |bar|
    var baz = bar * 3;
    baz = baz.mod(10);
    postln(baz - 3);
};
```

In inline form, there should be no spaces inside parentheses `( )` or square brackets `[ ]`. Curly braces `{ }` delimit functions, and should have exactly one space after the opening brace and one space before the closing brace.

```supercollider
// good:
a = [1, 2, 3].collect({ |x| x + (x * 3) });

// bad:
a = [ 1, 2, 3 ].collect( {|x| x + ( x * 3 )} );
```

### Indentation

#### Spaces and tabs

The SuperCollider class library uses tabs for indentation.

#### *[needs discussion]* Multi-line blocks

For all three bracket types, use the K&R style of indentation. The open brace comes at the end of the first line, rather than on a separate line.

```supercollider
x = {
    y = y + 1;
    3.rand
};

// rather than

x = 
{
    y = y + 1;
    3.rand
};
```

### Method calls

#### *[needs discussion]* Method calls

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

Functions
---------

#### Argument lists

Use `|pipes|`, not `arg`. Use a comma between each argument. In multiline form, put the argument list on the same line as the opening brace of the function or method.

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

x = { |foo = 3 bar = 4|
    foo + bar;
};
```

Arrays and Collections
----------------------

#### *[needs discussion]* Multiline form

Each element should be on a separate line:

```supercollider
x = [
    "foo",
    "bar",
    "baz"
];
```

The abbreviated symbol syntax `[foo: "bar"]` should only be used in contexts that accept alternating symbols and other values. It's a good idea to use it in, e.g., `Pbind` and `Pmono`.

#### *[Needs discussion]* Abbreviated symbol syntax

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