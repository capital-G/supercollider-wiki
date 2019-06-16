## Prerequisites

- Be familiar with CONTRIBUTING.md, DEVELOPING.md, git workflow, code of conduct, and this document
- Be familiar with or willing to learn about the part of the project related to the PR you're reviewing
- Have previously participated in PR review discussions, and/or have previous PR review experience
- Lots of patience and a willingness to take the time to communicate clearly with others

## Overview

The major tasks for a reviewer are:

1. Determine whether a PR has merit, and if so, determine what steps are needed to merge it. This may require reading code, running tests, and requesting information or action from the PR author.

2. Communicate clearly about task (1) with PR authors and other collaborators. This includes effectively using labels, milestones, and projects, triaging spin-off discussions that may result from a PR review, and giving PR authors accurate and direct instructions when needed.

3. Make SuperCollider an enjoyable project to contribute to. This includes being friendly and respectful toward PR authors and other collaborators, being transparent about project rules and procedures, and making sure PRs you review are merged or closed in a timely manner.

## Quick checklist

This is meant as a reference checklist of the bare minimum of things to check before approving or merging a PR.

- Is CI (continuous integration) passing? If not, why? If a build failure is the PR author's fault, inform them; otherwise, restart the job or ask another project member for advice.

- Review the changes. Do they reflect the stated intent of the PR? Review the quality of the code including comments, style, naming, correctness, and general code cleanliness. If needed, build the branch yourself and thoroughly test it. For a complicated or subtle change, don't hesitate to ask the PR author to explain how they tested their branch (and be skeptical if they haven't).

- Check the commits. It's not uncommon for a simple change to end up being split across several commits due to the review process. Request that the PR author squash their commits, or use the "Squash merge" option instead of "Create merge commit" option when merging the PR.

- Check the branches. Is the PR being made to the right branch? Let the PR author know they shouldn't be submitting PRs from their fork's release or develop branches. Request a rebase or add the PR to the "PRs to Cherry-Pick" project if necessary.

- Does the PR need documentation?

- Does the PR need tests? Are any new tests thorough enough, and do they follow our guidelines [link]? Unfortunately, tests written in SC don't currently run in CI, so those need to be checked manually by at least one reviewer. Talk to Brian H (@brianlheim) if you want to help fix this!

## How to get started as a reviewer

1. Make sure you meet all the prerequisites listed above. We won't quiz you, but it's important that we're all on the same page to avoid unnecessary misunderstandings or disagreements during reviews.

2. Reach out to an active project maintainer. Brian H (@brianlheim) and Nathan H (@snappizz) are two such people who are usually reachable via email or Slack. You can also reach out to the general developer community on a more public forum, such as the sc-dev mailing list.

3. We'll give you permissions so that you can review and merge PRs.

4. Find a PR that interests you and start reviewing!

## Various instructions/guidelines

### Using labels, milestones and projects

(Is this already documented somewhere/do we have any real procedures for this?)

### Guideline: Ask questions

If you don't know how to review a PR, or have a question about reviewing, ask a more experienced contributor! These are opportunities to improve our process and identity additional project issues or feature ideas.

### Guideline: It's OK to make mistakes

Pressing the "Merge" button can be pretty stressful the first few times you do it, but don't worry about making mistakes. The main branches of the SuperCollider project are heavily protected against truly disastrous errors, and everything else is easily reversible.

### Guideline: Assume good faith 

Given no evidence to the contrary, assume that a PR author is acting out of a genuine interest to improve this project. English may not be their first language, and so they may have difficulty understanding technical language or providing all the information we normally like to see in a PR. Be patient and communicate transparently with PR authors; even if it's obvious from the start that the PR will not be merged.

### Guideline: Stay on topic

In the course of a PR, auxiliary discussions may arise about newly discovered issues, desired features, or even procedural (meta-review) topics. It is crucial that such discussions don't get in the way of reviewing the PR at hand. Any discussion not related to the PR should be respectfully relocated to a more appropriate venue; this may be a new PR, an issue ticket, or a discussion thread on some other forum.