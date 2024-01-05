# Reporting bugs, issues and feature requests

(create-issue)=
## Issues

Reporting bugs and other issues, including feature requests, is handled through the GitHub [Issue tracker](https://github.com/supercollider/supercollider/issues).

### Before creating an Issue

The purpose of the Issue tracker is not just to report that there's a problem with SuperCollider, but to effectively communicate what the problem is so that others can easily help reach a resolution.

1. **Investigate the issue** 
    - What is the minimum effort or code required to produce the issue? Does it happen every time? Can you get it to happen on someone else's computer? Someone else's operating system?
2. **See if an Issue already exists**
    - Search the [Open Issues](https://github.com/supercollider/supercollider/issues). 
    - If an issue for your problem already exists, read through the discussion thread to understand the current status, and consider joining the discussion, saying you can reproduce it on your system, plus any additional info that isn't already known in the issue thread.
3. **Ask the community** 
    - If you feel that you need some help investigating the issue, reach out to the community. There may be discussion around the issue or requested new feature on the [scsynth.org](http://scsynth.org/) forum or discord. That can help you add useful context for making your submission comprehensive.

### Creating an Issue

**File your Issue in the tracker**: When opening an issue you’ll see a template for you to fill out—please fill out as much of the template as possible. It's there so developers can understand your issue fully and efficiently.

- If appropriate, provide a [Minimal reproducible code example](https://en.wikipedia.org/wiki/Minimal_reproducible_example), along with the resulting erroneous output.
- When an issue involves crashing or the app is unresponsive, providing a crash report can give a helpful lead on the problem. See [Generating a crash report](https://github.com/supercollider/supercollider/wiki/Generating-crash-reports) for instructions for your platform.
    - _TODO:_ add the syntax for a markdown dropdown element to use for embedding the crash report
- One ticket, one Issue: if you have multiple issues to report, open separate tickets for each one.

Note: Be sure to create your issue in the appropriate repository. For example, [sc3-plugins](https://github.com/supercollider/sc3-plugins) are maintained in their own repository separate from SuperCollider.

## Feature requests

_TODO_

## Tips for filing GitHub Issues

Here are some tips for creating idiomatic issues. Taking just a little bit extra time will make your issue easier to read, easier to resolve, more likely to be found by others who have the same or similar issue in the future.

- Take some time to learn *basic* markdown.
    - This [Markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is helpful, as is the GitHub guide to [Basic Markdown](https://help.github.com/articles/markdown-basics/).
- Learn about [GitHub-flavored Markdown](https://help.github.com/articles/github-flavored-markdown/).
    - And if you want to really go above and beyond, read [Mastering Markdown](https://guides.github.com/features/mastering-markdown/).
- Wrap code using single backticks for inline formatting, e.g. \`myVariable\`, and a "code fence" of triple backticks for code blocks.
    - This ensures that code will retain its format, making it much more readable to others.
    - Use syntax highlighting for code in your submission (and in the discussion threads) by adding `supercollider` (or the appropriate language name) after the first code fence, e.g. ` ```supercollider `.
