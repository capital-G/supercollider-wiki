This page contains information for the SuperCollider project Wiki: structure, organization, formatting and style guidelines, etc.

All guidance here is considered a _recommendation_ unless stated otherwise.

<!-- TOC start (generated with https://derlin.github.io/bitdowntoc/) -->

#### Table of contents

- [Making changes](#making-changes)
- [Duplicate content](#duplicate-content)
- [Tone and brevity](#tone-and-brevity)
- [Capitalization in titles and section headers](#Capitalization-in-titles-and-section-headers)
- [Section breaks](#section-breaks)
- [Tables of contents](#tables-of-contents)
   * [Anchoring back to the top](#anchoring-back-to-the-top)
- [Directory pages](#directory-pages)
- [The sidebar](#the-sidebar)
- [Works in progress (WIP)](#works-in-progress-wip)

<!-- TOC end -->


# Making changes

Become familiar with wiki conventions described in this document before making changes. 

We try to avoid wiki sprawl by avoiding duplicate content, putting information in a logical place within the wiki structure, and linking to that information if it is relevant in other parts of the project wiki.

It's helpful to consult others in the community ahead of making substantial changes. If the modification resulted from conversion in the Disussion or scsynth forums, etc., linking to the thread can be useful. In particular, consider communicating with a previous author (visible in the revision history) if you're substantially revising their changes.

Just as you would for git commits, try to make your changes in logical batches and make a note of the change in the "Edit message" field before saving.

_Use the Preview function_ before saving to avoid multiple minor follow-on changes that would clutter the history. 


# Duplicate content

Avoid duplicate content! Link to other pages/sections whenever possible to reduce maintenance effort avoid information going stale. 
For example, instead of listing all the places where you might get in touch with developers, link to a Community page, #Developers section.


# Tone and brevity

Try to be *complete* and *concise* with the information you present. Provide full context, without assuming your readers’ prior knowledge of the context. 

There’s a _lot_ of information in the wiki. Your readers are likely here for a specific reason and are in the middle of a mind-consuming task. The occasional joke is nice, but how will it land on the fifth read-through when you really just want to remind yourself of how to interactively rebase your commits? This section has already gone on too long.


# Titles and section headings

In wiki titles and section headings, use sentence case — capitalize only the first word in the title, but don't punctuate the end of a title or heading.

Avoid the use of special characters or symbols (+, /, -, &, etc.). They're sometimes stripped and can cause problems when cross-linking.


# Section breaks

Put two newlines between sections (and subsections) for readability:
    
```markdown
...
So ends this section.
    

# Next section

So begins the next section.
...
```
    
- _Recommend:_ If there is a one- or two-sentence overview at the start of the wiki, this goes _before_ the table of contents.

# Tables of contents

*Please update the ToC when making changes to a wiki!*

Tables of content (ToCs) are encouraged on wiki pages with any more than 3 sections and extend beyond 3 screen lengths.

Use your judgement about the `depth` of the ToC, but a depth of `2` generally strikes a balance between useful and concise.

Tables of contents can be automatically generated with onlin tools like [bitdowntoc](https://derlin.github.io/bitdowntoc/) or command line tools like [gh-md-toc](https://github.com/ekalinin/github-markdown-toc.go) (broken as of 11-2023). The specific tool doesn’t matter, and editing manual is of course ok (but error prone).

Make sure the “Table of contents” line is a level-4 header:

```markdown
#### Table of contents
```

This saves space while still making it easy to anchor to with the `^Top` backlink.

Now that you’ve made a ToC, does the wiki hierarchy make sense? If not, revise the wiki!


## Anchoring back to the top

Once the wiki grows longer than two or three screen heights, it is useful to link back to the top, by anchoring to the ToC, with the text alias `^Top`:

```markdown
...
So ends this section.

[^Top](#this-page-contains)


# Next section
...
```

Note two newlines are still kept after the previous section.

[^Top](#table-of-contents)


# Directory pages

Directory pages allow a multiplicity of wikis to be organized into a few broad categories. This also helps keep the sidebar slim and useable.

There are currently four categories: [[Contributing]], [[Development resources]], [[User resources]], and [[Community]]. This may change in the future but the goal is to keep the number of directory pages low.

It’s OK to link to the same wiki from multiple Directory pages. For example “Reviewer Instructions” may be useful under both the “Development Resources” Directory (devs are typically the Reviewers) and the “Contributing” Directory (Contributors may want to know how the review process for their PR).


# The sidebar

The side bar links to the categorical Directory pages. *All* wiki pages should be linked to from at least one of these wiki [Directory pages](#Directory-pages).

Each Directory page linik is followed by a brief description of the kinds of wikis found therein.

*Historical note:* Previously, the sidebar contained a long but incomplete list of pages that became unwieldy over time and the categorization didn’t clearly communicate content or priority. This categorical directory is a more sparse approach which (hopefully) improves clarity and maintainability, at the expense of place your favorite wiki two clicks away instead of one.

Note that _all_ pages in the SuperCollider wiki system are still viewable at once in the “Pages” toggle menu above the sidebar.


# Works in progress (WIP)

When publishing a wiki, it should be minimally viable. Avoid the [WIP] tag in the title, or a one-liner at the top saying “this is a work in progress”. 

Wikis are living documents—works-in-progress by nature. “WIP wikis” have a tendency to stay a WIP for *years.* This discourages people from trusting and consulting them or even contributing  to them under the assumption that they may be interfering with someone else’s effort to bring it to a “released” state.

If you’re drafting a wiki and want to make it public for feedback, you can host it on your fork of the SC repo and link to it on the forums for feedback.

If you’d like to collaboratively bring it to a minimally viable state on the main SC wiki (so others have write access), describe at the top what active process is underway to bring it out of the WIP state ASAP. The sooner its out of the WIP, the sooner it can be trusted, encourage discussion, and grow with help from others.

Don’t let the perfect be the enemy of the useful—it’s better to mark specific ********sections******** as works in progress, rather than an entire wiki. Even if the wiki is incomplete (within reason), there’s probably still some useful information there!

[^Top](#table-of-contents)