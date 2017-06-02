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

Commas should have one space after, but not before. No space should go before semicolons.

The three kinds of brackets, `( ) [ ] { }`, may be used either inline or multiline. In inline form, there should be no spaces inside parentheses `( )` and square brackets `[ ]`. Curly braces `{ }` are "heavier" since they denote functions, so they should have exactly one space after the opening brace and one space before the closing brace.

```supercollider
// good:
a = [1, 2, 3].collect({ |x| x + (x * 3) });

// bad:
a = [ 1, 2, 3 ].collect( {|x| x + ( x * 3 )} );
```

Multiline form for all three bracket types is uses the K&R style of indentation:

```supercollider
x = {
    y = y + 1;
    3.rand;
};
```

Specific details on `{ }` and `[ ]` whitespacing are discussed in later sections.

Method calls
------------

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

Methods should always be multiline.

Use `|pipes|`, not `arg`, with a comma between each argument and no spaces inside the pipes. In multiline form, put the argument list on the same line as the opening brace of the function or method.

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

Arrays
------

In multi-line form, each element should be on a separate line:

```supercollider
x = [
    "foo",
    "bar",
    "baz"
];
```

The abbreviated symbol syntax `[foo: "bar"]` should only be used in contexts that accept alternating symbols and other values. It's a good idea to use it in, e.g., `Pbind` and `Pmono`.

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