_This document is a work in progress!_ Feel free to question it and suggest improvements. The document's main author is Brian Heim (@brianlheim).

Guide to SuperCollider Unit Testing
===================================

Content overview:
- Purpose
- What is testing?
- Testing terminology
- The UnitTest class
- Unit testing guidelines
- SCClassLibrary testing standards
- Adding tests to the SCClassLibrary test suite
- Examples
- Resources

Purpose
-------

This guide is meant for SuperCollider users as well as developers working on the SuperCollider
project.

The first two sections -- "What is testing?" and "Testing terminology" -- are meant for those new
to testing. "The UnitTest class" is an introduction to the core unit testing framework in
SuperCollider. "Unit testing guidelines" contains a list of general good-practice guidelines for
writing and maintaining unit tests; "SCClassLibrary testing standards" apply specifically to
maintainers of the SCClassLibrary test suite. In the "Examples" section you will find real-world
excerpts that illustrate common situations encountered while writing tests. Finally, "Resources"
contains links and references for further reading.

What is testing?
----------------

In *Clean Code*, Steve McConnell writes:

> Testing can never completely prove the absence of errors. If you have tested extensively and found
> thousands of errors, does it mean that you've found all the errors or that you have thousands more
> to find? An absence of errors could mean ineffective or incomplete test cases as easily as it
> could mean perfect software.

Testing terminology
-------------------

### Types of tests

These are names for frequently encountered types of tests and testing approaches:

**Unit tests** are small, modular tests that verify a "unit" of code. Examples include verifying
that a multiplication function correctly multiplies 5 and 8, verifying that constructing an object
with some flag set to `true` has the intended effect, and checking that the result of `"hello, " ++
"soundworld"` is what you expect. These are typically at the heart of a test suite, because they
allow a developer to quickly pinpoint where (and hopefully why) a failure is happening.

**Regression tests** are tests that ensure behavior is maintained when a system changes. This type
of test is very similar to unit tests; the main difference is that it typically is written after
(possibly long after) the original code, and serves to record its current behavior, regardless of
whether it fits a particular specification. This is useful because when later changes are made, it
is easy to tell if the behavior has changed in ways that are unexpected.

For example, one of the tests in the SuperCollider test suite checks that the server correctly loads
and plays a `SynthDef`. This `SynthDef` caused an issue at one point during development, so in order
to make sure the same error wasn't introduced again, we use it as a regression test.

**Integration tests** are used to ensure that when two components are combined, they behave as
expected. A good example is testing that when an option is set using `ServerOptions` for a `Server`,
the server program uses the right settings when it boots. Usually these kinds of tests are used in
cases where multiple objects need to interact tightly together.

**End-to-end tests** check that the whole pipeline of a larger system works as expected. The purpose
of these tests overlaps with regression and integration testing; the main difference is the scale.

From "The Philosophy of Testing" by Max Kanat-Alexander: "You start up the whole system, perform
some action at the entry point of user input, and check the result that the system produces. You
don't care about how things work internally to accomplish this goal, you just care about the input
and result. [...] End to end tests are valuable, particularly as an initial stopgap for a system
that entirely lacks tests."

**Monkey testing** is a technique that uses randomized input (often in large quantities) to try to
"throw a wrench" in the system. It is important to make sure that if a failure happens, it can be
recorded an repeated (in other words, you should be able to find the wrench after you've thrown
it!). This kind of test is also called a **smoke test**.

As you can probably tell, these terms are not strictly defined and usually reflect intent more than
some specific property of the test itself. Understanding the different ways of approaching testing
and using them effectively is a great skill to develop.

### Black-box and white-box testing

The term **black-box testing** refers to tests written without any knowledge about what might be
going on inside the method or class being tested; the developer writing the tests only has access to
external information such as the method signature and specifications. **White-box testing**, on the
other hand, refers to testing where the developer has knowledge of the implementation of the
component being tested. Both black-box and white-box testing are valuable: with black-box testing, a
tester might overlook test conditions that would seem obvious if they knew implementation details,
and vice versa for white-box testing.

### Test suites

A test suite is a set of tests or test suites. At minimum, it is a subclass of `UnitTest` that has
at least one `test_` method. We typically refer to the whole set of tests in the SuperCollider
repository, which contains many test suites itself, as "the test suite."

### Mock objects

A **mock object** is an object created for the purpose of a test that simulates the behavior of real
objects in enough ways for the test to run. Think of the way engineers use a wind tunnel to test the
aerodynamics of a plane. Typical use cases are testing for an error that is difficult to produce
naturally, testing with an object whose "real" version is too slow, or testing with an object that
would normally provide non-deterministic results. The main goal is to achieve greater isolation for
the test environment.

For more information, see the related [Wikipedia
article](https://en.wikipedia.org/wiki/Mock_object).

### Test-driven development (red/green testing)

**Test-driven development (TDD)** and **red/green testing** refers to a software development
process that emphasizes test-writing as the first and primary action in a development cycle. That
is, tests are written first that do not pass ("red" tests), then code is written until they do pass
(reaching "green" status), at which point the code is refactored and polished. One of the tenets of
this approach is to only write as much as is needed for all tests to pass.

For more information, see the
[Wikipedia article](https://en.wikipedia.org/wiki/Test-driven_development).

The UnitTest class
------------------

See the `UnitTest` help file.

Unit testing guidelines
-----------------------

### Tests should be independent

Sometimes, you want to run a single test by itself; sometimes, only a few tests out of a test suite;
and sometimes, you want to reorder the tests in a suite. Unit tests should be resilient to all of
these possibilities: they should be independent. It should not matter how many tests out of a suite
are run, nor should it matter what order they're run in. If you need something to happen before or
after a test is run, consider whether it should go in the **setUp** or **tearDown** for that suite.

### Tests should have exactly one assertion

This might seem a little draconian, and there are certainly times when having multiple assertions in
a test is justified. But, in the vast majority of unit tests, making multiple assertions is a strong
indicator that you are testing more than one "unit" at once, which will make it harder to understand
the purpose of the test when it fails.

Consider a class `Bip` that has a method named `udpateFoo` that sets the `foo` field on the object,
returns `foo`'s old value, and increments a `fooUpdateCount`. There are two ways you could test the
`updateFoo` method. One approach is to test all three effects at once:

```
// in TestBip.sc

test_updateFoo() {
	var bip = Bip(); // initial values of foo and fooUpdateCount are 0
	var oldFoo;

	oldFoo = bip.updateFoo(3);

	this.assertEquals(oldFoo, 0);
	this.assertEquals(bip.foo, 3);
	this.assertEquals(bip.fooUpdateCount, 1);
}
```

Another approach is to use three separate tests:

```
test_updateFoo_setsFoo() {
	var bip = Bip();
	bip.updateFoo(3);
	this.assertEquals(bip.foo, 3);
}

test_updateFoo_returnsOldFoo() {
	var bip = Bip();
	var oldFoo = bip.updateFoo(3);
	this.assertEquals(oldFoo, 0);
}

test_updateFoo_incrementsFooUpdateCount() {
	var bip = Bip();
	bip.updateFoo(3);
	this.assertEquals(bip.fooUpdateCount, 1);
}
```

The second approach requires more lines of code and may take more time to write, but consider what
you gain:
- The name of each test clearly defines what it is testing. In the case of a failure, reading the
	test name alone is enough to tell you what is wrong.
- Furthermore, having clear names means there are no comments required to explain what the test is
	doing. This is a good rule of thumb for deciding whether or not your test is well-designed.
- It is easier to check at a glance that each test is correctly written.
- It is easier to maintain. The more complex a block of code is, the more likely it is that errors
	will be introduced when attempting to modify it. Similarly, the more complex it is, the longer it
	will take for another programmer (perhaps you, several months later) to understand it. Modifying
	tests should be fast and easy; sometimes, writing more literal lines of code means that fewer
	lines will have to be read and updated later.

This might seem like a trivial example, but it's easy to find real-world methods that have several
side effects like this, or are even more complicated.

### Avoid grouping conditions in asserts

It may be tempting to group several conditions together:

```
this.assert(bip.foo == 3 and: oldFoo == 0 and: bip.fooUpdateCount == 1);
```

You should avoid doing this for several reasons:
- It is more difficult to read.
- It requires use of `assert`, when `assertEquals` would give us more information (see below).
- When the test fails, it will be impossible to tell which of the three conditions are false!

### Prefer assertEquals to assert

Wherever possible, prefer using `assertEquals` to `assert`. When you use `assertEquals`, the
automatically generated failure message will give you information about the experimental value and
the expected value. When you use `assert`, you only know that the values were unequal. Therefore,
you can save yourself time spent both writing the assert message and reading the test code by using
`assertEquals`.

The same argument goes for using `assertFloatEquals` over a hand-written `assert` that tests the
same condition. Therefore, this rule could be generalized to: "use the most specific `assert` method
possible"; use of `assertEquals` just happens to be the most frequent situation where it applies.

### Test only what you need

If a test wouldn't tell you anything new about how well a component functions, don't write it! Not
only do redundant tests require more time to write, they also take more time to run and give a false
sense of security. If you have a test that checks the result of `1 + 2`, there's no need to write a
second test for `3 + 4` unless you have some reason to suspect that your addition operation might be
treating those operands differently. A good rule of thumb is: if you can't easily describe how one
test differs from another, they probably aren't both necessary. Remember, the goal of writing tests
is to find errors, not to show that code is correct.

### Test for common mistakes

From *Code Complete*:

> good programmers use a variety of less formal, heuristic techniques to expose errors in this code.
> \[...\] \[Error guessing\] means creating test cases based upon guesses about where the program
> might have errors.

Some good things to test are:

- boundary cases:
	- unique integers like 0, -1, 1, and maximum and minimum integer values
	- unique floats like `NaN` (`0/0`), `-inf`, `+inf`, negative and positive large floating-point
		numbers, empty strings, strings
	- unique strings like the empty string, very long strings, strings with character values in
		the ASCII control range (1-31) and non-ASCII range (128-255), and strings will null
		characters
- bad data:
	- garbage or semirandom input (for example, strings or arrays in an invalid format)
	- numbers outside the expected "valid" range
	- less data than expected
	- more data than expected
	- objects with bad or invalid state used as input

It's important to consider the specific component being tested and craft your inputs accordingly.
This is the part of testing where you get to be mean to your code!

Testing on these kinds of inputs has the additional benefit of forcing you to think about the
guarantees of the component being tested. Should it ignore bad inputs silently? Post a warning?
Throw an error? Not even test, and put the burden of validation on the caller? Each of this is a
valid design choice depending on the situation; the important point is that it ought to be a
*choice*, not an afterthought.

### Use test cases that are easy to check manually

Prefer using simple values like `"book"` and `2000` as test inputs. Complicated-looking values like
`"yzzoinnnpon"` and `19645583` are usually no more likely to discover errors than their visually
simpler counterparts. This makes checking the correctness of a test by hand or by eye easier.

### Automate everything

If a test has to be run manually, it is likely to be run less often than automated tests, perhaps
not even at all. It's worth it in the long run to make tests automated. If you find it difficult to
automate a particular test, don't forget that the best solution could be to add code to the
component being tested!

### Tests should be repeatable

Running a test multiple times should only produce a different result when the code being tested is
modified. A test that randomly fails or passes the first time it is run is a hindrance rather than
an aid to testing. So is a test that fails the second or third time it is run. If a test relies on
certain preconditions, it should establish that when it runs, or you should establish it in the
class's `setUp`.

### Tests should be thorough

This may seem obvious, but it's worth saying: tests should cover as much code as is possible and
reasonable. Reaching 100% test coverage is simply not possible or practical for many codebases, but
around 70-80% is healthy. As Kent Beck says in "What Should We Unit Test?": "Write tests until fear
is transformed into boredom."

### Naming test methods

Normally when naming variables and functions, the developer tries to strike a balance of clarity
between specificity and brevity. However, naming test methods clearly often means using more
characters than usual. Some authors recommend the "SSR" (subject-scenario-result) approach. For
example, a method that tests that the `onFailure` parameter of `Server.waitForBoot` actually gets
executed when the server fails to boot might be named:

```
test_waitForBoot_ifServerFailsToBoot_runsOnFailureParameter()
```

Here is the subject (`waitForBoot`), a scenario ("if the server fails to boot"), and the expected
result ("runs the `onFailure` parameter"). Note that each of these elements is separated by an
underscore in the method name.

This approach might seem unnecessarily verbose at first glance, but again, consider that when the
test fails, all you will see initially is the name of the test. Without looking at the test code,
you have a crystal clear diagnosis of the problem; so clear, in fact, that you may not even need to
look at the test code at all. Tests are read and run much more often than they are written, so
investing in a descriptive name while writing unit tests is well worth the effort.

Remember that the name of the test suite is also shared in the test report. This means that if you
have a lot of tests for this method, you can group them all together in a test suite named something
like `TestServer_WaitForBoot`. Then, you don't have to use the name of the method in the name of
each test; the report of a failure on
`TestServer_WaitForBoot:test_ifServerFailsToBoot_runsOnFailureParamter()` carries the exact same
information.

Whatever approach you use to name your test methods, ensure that they are descriptive and explicit.

### Write the test first

The reason for this is simple: the test is bound to be written at some point in time, and working on
a fix with a test already written gives you the opportunity to quickly run the test to check a fix.
If you wait until later, you may spend extra time making the solution more complex than it needs to
be.

### The arrange-act-assert approach

An elegant and straightforward way to organize your tests is with the arrange-act-assert approach:

1. **Arrange** the conditions necessary for the test.
2. Perform the **act** whose result you are testing.
3. **Assert** that the act had the expected consequences.

Take the dead-simple example of a calculator class:

```
// in TestCalculator.sc

test_addingTwoNumbers_producesSum() {
	// Arrange: create a calculator object
	var calc = Calculator();

	// Act: perform the action to be tested (addition)
	var result = calc.add(3, 8);

	// Assert: check that the addition was performed correctly
	this.assertEquals(result, 11);
}
```

Following this pattern religiously can produce very readable and maintainable test code, because the
flow of logic is clear and natural.

Sometimes, you might need a small "cleanup" section after the assert. For example, creating a server
in a test method requires calling `remove` on it to remove it from the global registry. Code
segments in the "arrange" and "cleanup" parts of a test are excellent candidates for things that
might be better off in the `setUp` or `tearDown` of the test suite.

### Avoid excessive boilerplate

There are a number of ways to cut down on repeating yourself in test code:
- Consider moving code into `setUp` and `tearDown` for the test suite. If a majority, but not all,
	methods in the suite use the same setup and tear-down code, consider whether it might be better to
	split the suite into two parts.
- Consider creating a small method for the sole purpose of performing repeated actions. You should
	not do this too often, because it has the potential to make test code much harder to understand.
- Consider refactoring the code you're testing! Code that works is not always written to be testable,
	and vice versa. If it's a pain to use a class or method, the problem might be best remedied by
	changing it so that it handles the setup itself or performs fewer tasks. Modularity is a quality
	of good interface design.

### But, some boilerplate is okay

Avoid the temptation of writing "helper" functions and abstract classes to aid tests. This increases
complexity, which makes your tests harder to understand and more likely to contain errors of their
own. Ideally, another developer should be able to understand what your test is doing without looking
outside the test method itself.

### Write testable code

Writing code that can be tested efficiently is a skill worth developing. Writing testable code is
often closely aligned with writing well-designed code in general: methods should be kept small and
focused, complex state should be avoided, and results should be logical and predictable. Writing
tests is a good time to reflect on what could be improved in the design of a method or an object -
if it's difficult for you to test, chances are it will be difficult for a user to use.

SCClassLibrary testing standards
--------------------------------

*Note:* these guidelines are aspirational. They are not all used in current practice. This guide
takes precedence over anything you might see in the test suite. Changes that bring them into sync
with these guidelines are very welcome!

### One class per file

Every test class should test methods on exactly one library class. This may make some tests slightly
less intuitive to write - for example, when testing interfaces shared across multiple classes - but
makes organization and maintenance straightforward. Tests on methods for `String` should go in
`TestString`, those for methods on `Routine` should go in `TestRoutine`, and so on. However, if
there are large number of tests to be written, they may be divided across several classes.

### Testing one class in multiple files

If your test file is becoming very large (over 300 lines) or you find yourself writing a lot of
tests for the same method or set of methods, the tests may be broken into several classes according
to the format: `TestClass_Method` or `TestClass_Component`.

### Using external datasets

If a test requires a large dataset, place it in a separate file in `testsuite/classlibrary/data` and
read it in during the test. This keeps test class source files neat and readable. See "Examples" for
a basic test demonstrating this.

### Naming

#### Classes

When a class only needs one test class: `TestSomeClass`.

When testing a method or component of a class: `TestClass_Method` and `TestClass_Component`.

Class names should always consist of capitalized words (never `TestClass_method`).

The file should be named to match the name of the class it contains.

#### Methods

Methods: in general, use SSR `test_subject_inSituation_respondsCorrectly()`. Use names that are
concise but descriptive, and can be reasonably well-understood without looking at the source code.

Spell out numbers.

#### Datasets

The filename should begin with the name of the test class in which it is used, and include a word or
two describing its contents or purpose. If a dataset is used by multiple test classes, the first
part of the name can be ommitted. Examples of dataset names are:

- `TestServer_hugeOSCArray`
- `TestMyStream_trickyInputSequence`
- `complexSynthdef.scsyndef`

Use a file extension only if the file is in a recognized format (such as `.csv`, `.scsyndef`).
Otherwise, omit the extension.

### Avoid using the default server

Don't use the default server unless your test absolutely depends on the "default" default server
(note that you can make a new server the default server). Tests using a pre-existing server violate
the independence of tests. Instead, prefer creating a new server using either the name of the method
or the name of the class as its name, to avoid name collisions. Make sure to call `remove` on it
when done.

### Use `Server:-bootSync` to boot a `Server`

Prefer using this method instead of `UnitTest:-bootServer`.

### Avoid use of `wait`

Generally, hard-coded delays are bad practice, and should be replaced with waiting or hanging on a
condition. Extra waiting slows down the test suite and introduces the possibility for unexpected
behavior if the sleeping thread wakes up early. If you write `1.wait` in a test, think about why you
need to do so. If there is no way to wait on a true condition, either add code to the system being
tested such that it is possible, or leave an explanatory comment.

### Using `guard-sclang`

[`guard-sclang`](https://github.com/aspiers/guard-sclang) is a tool written by Adam Spiers that
provides a continuous and automatic red/green testing. Developers are encouraged to use this tool.
For more information on setup and usage, see
[these instructions](https://github.com/supercollider/supercollider/wiki/%5BWIP%5D-Developer-info-%40DEVELOPING.md%41#continuous-automatic-redgreen-testing-via-guard-sclang).

### Avoid using class variables

Use of class variables increases the likelihood of tests becoming unintentionally interdependent.
They also make tests harder to understand, because values are initialized far from where they are
used.

In general, restrict usage of class variables to objects that are constructed and destructed in
`setUp` and `tearDown`.

Adding tests to the SCClassLibrary test suite
---------------------------------------------

It's easy to get started adding new tests to the SCClassLibrary test suite! The suite is in
`testsuite/classlibrary` in the main repository.

Before starting, you should review the SCClassLibrary test suite guidelines in the previous section
so that your code can be integrated with as few changes as possible.

To add tests:

1. Find the test file for the class you're testing. You may need to create a new file for this.
2. Add new test methods for the conditions you're testing until you're satisfied (or bored).
3. Run the test class's unit tests with `TestSomeClass.run` to determine whether they pass.
4. Revise the tests until they pass, then submit your changes!

If you run into any difficulties or have questions, feel free to ask a member of the dev team on
GitHub or email the sc-dev mailing list.

Examples
--------

These examples are intended as best-practice templates that can adapted easily to a variety of test
situations. Many of them are based on a fictitious `Calculator` class which has all the common
functions of a handheld calculator.

### A simple test

```
// in TestCalculator.sc

test_addition_twoPlusThree_isFive() {
	var calc = Calculator();
	var expected = 5;

	calc.enterNumber(2);
	calc.enterPlus();
	calc.enterNumber(3);
	calc.evaluate();

	this.assertEquals(calc.currentResult(), expected, "Addition works");
}
```

### A more complex test

```
test_globalLibrary_checkingOutABook_removesBookFromLibrary() {
	var library = Library.global();
	var bookName = "War and Peace";
	var book = library.checkOut(bookName);

	this.assert(library.hasBook(bookName).not);

	library.reset();
}
```

### A test using randomness

In this test, some string-related method is fed a large number of random strings (a "monkey test" -
see "Testing terminology") and is expected to return false for all of them.

The main purpose of this example is to demonstrate the correct way to handle randomness in a test:
by using a fixed seed so that the results are deterministic and reproducible. In practice, tests
like this are not needed often, since hand-crafted inputs are often just as good (or even better) at
catching corner cases.

```
test_someMethod_handlesRandomStrings {
	var seed = 5;
	var n = 100;
	var stringSize = 10;

	thisThread.randSeed = seed;

	n.do {
		var string = String.fill(stringSize, {
			rrand($a.ascii, $z.ascii).asAscii
		};
		var result = string.someMethod();

		this.assert(result.not, "Input:" + string);
	}
}
```

### A test using a server

This test checks that setting `clientID` on a `Server` object during construction works. It
demonstrates several important points about server-related tests:
- avoid using the default server
- give the server object a somewhat unique name (in this case, the name of the class serves as
	reasonably unique)
- use `Server:-bootSync`
- `quit` and `remove` the server after use

```
test_setWithConstructor {
	var options = ServerOptions.new.maxLogins_(4);
	var server = Server(this.class.name, nil, options, 3);

	server.bootSync;
	this.assertEquals(server.clientID, 3, "clientID should be settable by Server constructor.");
	server.quit;
	server.remove;
}
```

### A test using condition variables

In this test, `someAsyncMethod`, a method on `SomeAsyncClass`, is an asynchronous method that
provides a callback parameter. Many asynchronous functions in SuperCollider provide such a
callback mechanism, such as `loadToFloatArray`. The parameter is typically named `action` or
`onComplete`. This test checks that after calling `someAsyncMethod`, the callback function is
eventually run and `result` is set to `1`. The conventional way to do this is by using a `Condition`
variable to wait for the callback to run, and forking a separate timeout thread in case it fails to
fire.

```
test_someAsyncMethod_runsCallback() {
	var async = SomeAsyncClass();
	var cond = Condition();
	var input = "async input";
	var result = 0;

	async.someAsyncMethod(input, { |i| result = i; cond.unhang });
	fork { 3.wait; cond.unhang };

	cond.hang;

	this.assertEquals(result, 1);
}
```

### A test using an external dataset

This shows how to run a test that depends on some external dataset stored as a CSV file in a `data`
directory relative to the test.

```
test_processData_givenSomeData_returnsThree {
	var someObj = SomeClass();
	var dataPath = "data/SomeClass_someData.csv".resolveRelative;
	var data = CSVFileReader.read(dataPath);
	var expected = 3;

	var got = someObj.processData(data);

	this.assertEquals(got, expected);
}
```

Alternatives to using a CSV file format include space-separated (with `FileReader`), tab-separated
(`TabFileReader`), and archived objects created with `obj.writeArchive` (read using
`Object:*readArchive`.

### A test using `setUp` and `tearDown`

In this test suite for a fictitious `Discotheque` class, each test method acts on a `Discotheque`
that's open and playing music. Since repeating this test code in every method would be highly
repetetive and prone to copy-pasting errors, it's best to use `setUp` and `tearDown`.

```
TestDiscotheque {

	var disco;

	setUp() {
		disco = Discotheque();
		disco.open;
		disco.playMusic(\trance);
	}

	tearDown() {
		disco.stopMusic;
		disco.close;

		// while not strictly required, setting class variables to `nil`
		// after use can help prevent accidental reuse.
		disco = nil;
	}

	test_emptyDiscotheque_isEmpty() {
		this.assert(disco.isEmpty());
	}

	test_addGuest_addingOne_numGuestsIsOne() {
		disco.addGuest(\Natalie);
		this.assertEquals(disco.numGuests, 1);
	}

	test_changeMusic_musicIsChanged() {
		disco.changeMusic(\house);
		this.assertEquals(disco.music, \house);
	}

	/* etc. */

}
```

Resources
---------

[The Philosophy of Testing](https://www.codesimplicity.com/post/the-philosophy-of-testing/)

[Writing Great Unit Tests: Best and Worst Practices](http://blog.stevensanderson.com/2009/08/24/writing-great-unit-tests-best-and-worst-practises/)

[What Should We Unit Test?](https://www.philosophicalhacker.com/post/what-should-we-unit-test/)

[Unit Testing Basics: Best Practices](https://stackify.com/unit-testing-basics-best-practices/)

[Top Five Best Practices for Writing Unit Test Scripts](https://www.developer.com/mgmt/top-five-best-practices-for-writing-unit-test-scripts.html)

[General Service Testing Best Practices](https://msdn.microsoft.com/en-us/library/hh323702%28v=vs.100%29.aspx)

[Integration Testing](https://msdn.microsoft.com/en-us/library/hh323698%28v=vs.100%29.aspx)

[JavaScript Unit Testing Guide (mawrkus)](https://github.com/mawrkus/js-unit-testing-guide)

[Ruby Programming: Unit Testing](https://en.wikibooks.org/wiki/Ruby_Programming/Unit_testing)

McConnell, Steve. *Code Complete*. 2nd Edition. Microsoft Press, 2004.

<!---EOF-->
