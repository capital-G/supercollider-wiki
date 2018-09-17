This is a collection of FAQs I've seen around the issue tracker. Hopefully this can be put someplace more public once it gains steam. This is meant as an addition to the longer guides about doing specific basic things like installing and configuring. - Brian

## Env seems to work differently than I expect

Source: https://github.com/supercollider/supercollider/issues/3629#issue-311070157

Answer: https://github.com/supercollider/supercollider/issues/3629#issuecomment-378478356

jamshark70:

> This is a common misunderstanding. We often think an envelope segment goes from level A to level B, and the next segment from B to C. But that's not correct. An envelope segment always goes from the envelope's current output level to the segment's target level.
>
> An envelope segment has no fixed, unchanging start level. If it did, it would be impossible to jump early to the release segment, or to loop back.
>
> But, when the EnvGen starts, it has no current level at first. So the Env provides one extra level, at the beginning. levels[0] initializes the EnvGen, and then this level is never touched again. So, levels[0] doesn't correspond to any envelope node. It's only a start value. The first envelope segment goes to levels[1].

## Can we change parameter names of methods? The current naming confuses me/I don't like it

Source: https://github.com/supercollider/supercollider/issues/3629#issue-311070157

Answer: Sometimes.

The important thing to note is that code can pass arguments this way:

```supercollider
foo.bar(param1: 7);
```

So, any change to a public-facing parameter name is a potential breaking change. We might be able to do this in a minor version release, but only if the parameter is rarely used or unlikely to be used with a keyword argument.

## Can I make X addition to the language syntax?

Please think _very hard_ about this before submitting a ticket. Conversations about this tend to fall apart very quickly unless the change is presented:

- clearly
- with examples
- with strong justification
- with discussion of tradeoffs

Also, remember to look and see if this idea has already been discussed.

## Why does sclang make me put `var` statements at the top of functions? Why can't I define classes at runtime?

These quirks and limitations of sclang are well known:

- all `var` statements have to go at the top of a function
- all class extensions have to come after classes in a class file
- classes can't be imported dynamically
- there is no namespacing

The sclang lexer/parser/compiler is one of the few parts of the platform that is still relatively intact from SuperCollider 1. The sclang code is huge, undocumented, poorly organized, and minimally tested, and even minor syntax changes are a massive undertaking and should be accompanied by a equally massive cleanup effort. There just aren't developer resources to address these right now. If you would like to help, please do.

## Is `?` or `??` faster?

James: https://www.listarc.bham.ac.uk/lists/sc-dev/msg58256.html

`??` is faster.

## Can we get code folding in the IDE?

Source: https://github.com/supercollider/supercollider/issues/2264

Answer: https://github.com/supercollider/supercollider/issues/2264#issuecomment-238515818

crucialfelix:

> The IDE isn't intended to become a full professional level code editor. That would suck up precious developer time that needs to be spent on the core feature (music). It's pretty complicated to do code folding correctly.

## Can I use SC in a game audio engine?

SuperCollider is licensed under the GNU GPL, a fairly restrictive open source license. This runs against the interests of most commercial game developers. 