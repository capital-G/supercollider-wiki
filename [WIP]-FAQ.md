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

## Can we change parameter names of methods? The current naming confuses me

Source: https://github.com/supercollider/supercollider/issues/3629#issue-311070157

Answer: Sometimes.

The important thing to note is that code can pass arguments this way:

```supercollider
foo.bar(param1: 7);
```

So, any change to a public-facing parameter name is a potential breaking change. We might be able to do this in a minor version release, but only if the parameter is rarely used or unlikely to be used with a keyword argument.

## Can I make X change to the language syntax?

Please think _very hard_ about this before submitting a ticket. Conversations about this tend to fall apart very quickly unless the change is presented:

- clearly
- with examples
- with strong justification
- with discussion of tradeoffs

Also, remember to look and see if this idea has already been discussed.