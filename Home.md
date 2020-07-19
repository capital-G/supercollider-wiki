First and foremost, thank you! We appreciate that you want to contribute to SuperCollider. Your time is valuable, and your contributions mean a lot to us.

This page is the new home for the document formerly known as `CONTRIBUTING.md`. It serves as a quick onboarding guide for SuperCollider developers.

You may also be looking for [the SuperCollider documentation](http://doc.sccode.org/).

## Joining the Community

SuperCollider users and developers communicate on a number of different channels. Here's how to access them:

- [Sign up for a GitHub account](https://github.com/signup/free) and give us a star.
- [Join the sc-users and sc-dev mailing lists](https://www.birmingham.ac.uk/facilities/ea-studios/research/supercollider/mailinglist.aspx).
- [Join the forums](https://scsynth.org/) for a more modern alternative to the listservs.
- [Join our Slack channel](https://join.slack.com/t/scsynth/shared_invite/zt-ezoyz15j-SVM7JVul94pxtDiUDRnd0w). It's not mandatory, but it's very convenient for talking to other devs!
- Watch the above channels for announcements of our weekly-ish developer calls on Skype. Everyone is welcome to join them!

## What does "contributing" mean?

Creating an issue is the simplest form of contributing to a project. But there are many ways to contribute, including the following:

- [Updating or correcting documentation](https://github.com/supercollider/supercollider/wiki/[WIP]-contributing-helpfiles)
- Fixing an open issue
- Requesting a feature
- Reporting a bug (see [Issues](#Issues) below)
- [Translating the IDE](https://github.com/supercollider/supercollider/wiki/Translating-the-IDE) into a language you know
- Creating a [Request for Comments (RFC)](https://github.com/supercollider/rfcs) to propose 'something big'

If you're new to this project, check out the issues tagged ["good first issue"](https://github.com/supercollider/supercollider/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22) – fixing one of these is a great way to get started as a contributor!

If you'd like to learn more about contributing to open source projects in general, the [Guide to Idiomatic Contributing](https://github.com/jonschlinkert/idiomatic-contributing) has a lot of useful information.

## Issues

### Before creating an issue

The purpose of the issue tracker is not just to report that there's a problem with SuperCollider, but to effectively communicate what the problem is so that others can easily help reach a resolution.

**Investigate the issue**: What is the minimum effort or code required to produce the issue? Does it happen every time? Can you get it to happen on someone else's computer? Someone else's operating system?

**See if a ticket already exists**: Search SuperCollider's [open issues](https://github.com/supercollider/supercollider/issues). If an issue for your problem already exists, it may be appropriate to leave a polite comment stating that you can reproduce it on your system, plus any additional info that isn't already known in the issue thread.

**Ask the community**: If you feel that you need some help investigating the issue, it may help to ask sc-dev, sc-users, or Slack.

**Fill out the issue template**: Once you feel that you have information for an effective issue, file an issue on the GitHub issue tracker and fill out the template. Please don't erase the template — it's there to help structure your report effectively.

Be sure to create your issue in the appropriate repository. Note that [sc3-plugins](https://github.com/supercollider/sc3-plugins) are maintained in their own repository separate from SuperCollider.

**One ticket at a time**: If you have multiple issues to report, please open separate tickets for each one.

### Creating an issue

We have provided an issue template for you to fill out so that the basic gist of the issue is easily determined at a glance. Please don't erase the template. It's there for a reason.

When an issue involves a crashing or unresponsive executable and you don't know why, providing a crash report can give developers a very helpful first step toward resolving the problem. See "Generating a crash report" below for instructions for your platform.

### Above and beyond

Here are some tips for creating idiomatic issues. Taking just a little bit extra time will make your issue easier to read, easier to resolve, more likely to be found by others who have the same or similar issue in the future.

- Take some time to learn basic markdown. This [markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is super helpful, as is the GitHub guide to [basic markdown](https://help.github.com/articles/markdown-basics/).
- Learn about [GitHub Flavored Markdown](https://help.github.com/articles/github-flavored-markdown/). And if you want to really go above and beyond, read [mastering markdown](https://guides.github.com/features/mastering-markdown/).
- Use backticks to wrap code. This ensures that code will retain its format, making it much more readable to others
- Use syntax highlighting by adding "supercollider" or the appropriate language name after the first "code fence" ("\`\`\`supercollider")

## Pull Requests (PRs)

Graciously accepted.

Before working on a pull request, consider whether it might be better to go through the [Request for Comments (RFC)](https://github.com/supercollider/rfcs) process first!

SuperCollider uses the [git-flow](https://nvie.com/posts/a-successful-git-branching-model/) branching model. We use the `develop` branch for new features, deprecations, and breaking changes, and we use the `3.10` branch for bug fixes for the next 3.10.x patch release that have no chance of breaking anything.

If you aren't too familiar with git, please see our guide: [Creating pull requests](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests).

## Developer Reference

*Please don't change the title of this section — it is the new location of `DEVELOPING.md`, which links here.*

Check the sidebar for a full list of reference documents for SuperCollider development. Here are a few that are particularly good for new contributors. You don't need to read and understand all of this before contributing! We are happy to help guide you through your first contributions. If you run into confusion or need help, you are always welcome to ask.

* [Project Structure](https://github.com/supercollider/supercollider/wiki/Project-Structure)
* [Setting up your development environment](https://github.com/supercollider/supercollider/wiki/Setting-up-your-development-environment)
* [Creating pull requests](https://github.com/supercollider/supercollider/wiki/Creating-pull-requests)
* [Reviewer Instructions](https://github.com/supercollider/supercollider/wiki/%5BWIP%5D-Reviewer-instructions)
* [git cheat sheet](https://github.com/supercollider/supercollider/wiki/git-cheat-sheet)
* [Code style guidelines](https://github.com/supercollider/supercollider/wiki/Code-style-guidelines)
* [C++ code style guidelines](https://github.com/supercollider/supercollider/wiki/Cpp-code-style-guidelines)
* [C++ formatting instructions](https://github.com/supercollider/supercollider/wiki/Cpp-formatting-instructions)
* [Unit Testing Guide](https://github.com/supercollider/supercollider/wiki/Unit-Testing-Guide)
