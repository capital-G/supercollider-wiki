C++ Code Style Guidelines
=========================

The following guidelines apply to C++ code throughout the SuperCollider project.

SuperCollider uses [clang-format](https://clang.llvm.org/docs/ClangFormat.html), an open source C and C++ source code formatting tool, to ensure consistent code style across our code base. So while the following discussion describes the style used in the code, along with some things that can't be easily automated such as variable naming, for issues of code formatting the output of the clang-format tool should be considered canonical style. For more information about using clang-format on SuperCollider C++ code see [here](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions).

In general SuperCollider follows the [WebKit Code Style Guidelines](https://webkit.org/code-style-guidelines/), with a few notable exceptions and additions.

### Naming

New code, either in new files or substantial additions to existing files, should follow [WebKit](https://webkit.org/code-style-guidelines/#names) guidelines around naming, which has some similarity to SuperCollider language style guidelines. Generally, name things using full words and CamelCase, classes have capitalized first letters, variables and functions do not. Prefix member variables with "m_" and static data members with "s_".

Older code used the prefixes `k`, `g`, and `m` to identify constants, global variables, and members respectively. You may see some code that uses the prefix `Pyr`; this refers to the origin of SuperCollider as a Max/MSP object called "Pyrite".

### Notes for UGen writers

The naming for UGens has fairly strict conventions, because SC's macros connect the function/struct names with the names used by a user. A UGen usually has a struct associated with it, which should take the same name as the corresponding sclang class (which implies it begins with a capital letter).

    struct SinOsc : Unit { ... };

In general the associated methods' names should begin with that name too: the constructor must take that name followed by _Ctor and the destructor (if used) must take that name followed by _Dtor.

    void SinOsc_Ctor(SinOsc *unit);

The DSP functions should take that name followed by `_next`, plus more text to distinguish the different DSP functions from each other as needed; e.g. audio-rate is postfixed by `_a` and control-rate is postfixed by `_k`. These postfixes might stack up for several parameter/rate combinations:

    void SinOsc_next_iak(SinOsc *unit, int inNumSamples);

Private methods within the plugin files don't have to follow strict naming but it is recommended to prefix them in a similar fashion, to identify the UGen(s) with which they belong.

### Lambdas

When writing lambdas, use explicit captures as much as possible. Avoid using `[=]` or `[?]` for the capture list.

### Indentation

We use 4-space indentation, same as [WebKit](https://webkit.org/code-style-guidelines/#indentation-no-tabs). 

### Line Breaking

The formatting tool will automatically wrap lines at 120 characters.

### Whitespace

Mostly follows [WebKit](https://webkit.org/code-style-guidelines/#spacing) guidelines but with a few differences. We always attach the opening brace to the same line as the control statement.

```cpp
// correct
if (condition) {
}

// incorrect
if (condition)
{
}

// correct
class FooBar {
};

// incorrect
class FooBar
{
};

// correct
void doSomethingAwesome(size_t howManyTimes) {
}

// incorrect
void doSomethingAwesome(size_t howManyTimes)
{
}
```

Function calls that include many arguments are automatically packed by clang-format to wrap at 120 characters.

```cpp

// correct
doSomething("string argument", 120.5, "another long string argument");

// incorrect
doSomething("string argument",
            120.5,
            "another long string argument");
```

Constructors should use initializer syntax indented at 4 spaces, but with the colon on definition line and the commas following the initializers, unlike [WebKit](https://webkit.org/code-style-guidelines/#punctuation-member-init).

```cpp
// correct
Example(int a) :
    m_aVariable(a),
    m_bVariable(0) {
}

// incorrect
Example(int a)
    : m_aVariable(a)
    , m_bVariable(0) {
}
```

Pointer and reference types should align the * or & to the left with the type, same as in [WebKit](https://webkit.org/code-style-guidelines/#pointers-cpp).

```cpp
// correct
int* a;
const std::string& userName;

// incorrect
int * a;
int *a;
const std::string & userName;
const std::string &userName;
```

Empty lines at the start of blocks will be automatically removed by clang-format.

```cpp
// correct
if (foo) {
    bazz();
}

// incorrect
if (foo) {

    bazz();
}
```

### Disabling Automatic Formatting

There may be some situations when the automatic formatting applied to all C++ code will substantially break readability or utility of a certain piece of code. Subject to approval by the code reviewer, it is possible to [disable automatic formatting on code](https://clang.llvm.org/docs/ClangFormatStyleOptions.html#disabling-formatting-on-a-piece-of-code) by using special comments.
