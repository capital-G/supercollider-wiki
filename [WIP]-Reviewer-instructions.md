# Reviewer instructions

Here, you'll find information on how to review pull requests (PRs) for the SuperCollider project. Welcome!

## The big picture

Code reviews are essential to the development of quality software, but they can also be frustrating and time-consuming. There are a lot of great resources online on the philosophy, techniques, and best practices for code reviews. To get you started, here are some links worth checking out:

- https://blog.codereview.chat/2019/07/15/the-code-review-bottleneck.html
- https://github.com/joho/awesome-code-review

## Getting into reviewing easily

Some parts of SuperCollider are easier to review than others. If you're looking for an easy way to get involved as a reviewer, focus on PRs labeled `comp: help` and `comp: examples`. Most of these can be reviewed just by reading them. Following and participating in review discussions can also help you get quickly acquainted with the review process.

## Prerequisites for reviewers

- Be familiar with [CONTRIBUTING.md](https://github.com/supercollider/supercollider/blob/develop/CONTRIBUTING.md), [DEVELOPING.md](https://github.com/supercollider/supercollider/blob/develop/DEVELOPING.md), [git workflow](https://github.com/supercollider/supercollider/wiki/git-workflow-and-guidelines), [Code of Conduct](https://github.com/supercollider/supercollider/blob/develop/CODE_OF_CONDUCT.md), and this document
- Be familiar with or willing to learn about the part of the project related to the PR you're reviewing
- Have previously participated in PR review discussions, and/or have previous PR review experience
- Bring lots of patience. Reviewing is a very communicative process!

## Overview

The major tasks for reviewers are:

1. Determine whether a PR has merit, and if so, determine what steps are needed to merge it. This may require reading code, running tests, and requesting information or action from the PR author.

2. Communicate clearly about task (1) with PR authors and other collaborators. You should effectively use labels, milestones, and projects; redirect any spin-off discussions that may arise; and give PR authors accurate and direct instructions when needed.

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

1. It is important that we share basic assumptions to avoid unnecessary misunderstandings or disagreements during reviews, so please take some time to get yourself acquainted with the procedure.

2. Reach out to an active project maintainer. Brian H (@brianlheim) and Nathan H (@snappizz) are two such people who are usually reachable via email or Slack. You can also reach out to the general developer community on the sc-dev mailing list.

3. We'll add you to the Reviewers organization team.

4. Find a PR that interests you and start reviewing! You can also request to be assigned to specific PRs.

For your first few reviews, a more experienced reviewer will look over your review, leave any
necessary feedback, and perform the final merge.

## Various instructions and guidelines

### Using reviews

When you leave a review, you have three options: "Comment", "Approve", "Request changes". If you
have any request at all, including a request to rebase, a request for more documentation, or a request
for code changes, **leave a "Request changes" review**.

Give an "Approve" review only when you believe the PR is ready for merging.

Use the "Comment" review option for questions, concerns, and general commentary.

### Merging

New reviewers should not merge PRs. In general, each PR should be reviewed by at least one person and merged by a different person. If the PR is very trivial, one person can both review and merge. Examples of trivial PRs are typo fixes, formatting fixes, inter-branch merges (for example, 3.10 into develop) and cherry-pick branches ("cherry-pick #xyz onto 3.10"), code changes of a few lines that do not change functionality, and documentation improvements of a few lines.

### Using assignments

When you are ready to review a PR, **assign yourself as a reviewer**. In the interest of moving PRs
along, stay mindful of the PRs you're assigned to; you should start reviewing a PR within one week
of assigning yourself. If you don't think you will have time to do so, unassign yourself. After one
week of inactivity, another reviewer may unassign you and assign themselves if they are ready to
start reviewing.

If another maintainer has assigned themselves to a PR, feel free to leave a review or comments; however, if the assigned reviewer is a new reviewer (i.e., part of the [Reviewers team](https://github.com/orgs/supercollider/teams/reviewers), and not @snappizz or @brianlheim), let them review the PR themselves so they can gain experience.

### Using labels, milestones and projects

#### Labels

We use an extensive system of labels to categorize issues and pull requests. We consistently use the following labels:

- `comp: x` to indicate the affected *comp*onent of SuperCollider
- `os: y` if the issue or PR affects one operating system in particular
- `env: z` if the issue or PR affects one *env*ironment (SCIDE, Emacs, etc.) in particular

For issues, we use `bug` or `enhancement` to indicate whether the issue is reporting a bug or requesting a feature respectively. We also use `good first issue` to indicate issues that are clear in scope and would be a good place for an interested contributor to start.

Each PR should have at least one `comp:` or `env:` label; and each issue ticket should have at least one `comp:` or `env:` label and one `bug` or `enhancement` label. If you see an unlabeled issue or PR, please take the time to add a label! 

We do not yet have specific rules or practices around other labels; feel free to offer suggestions on how we can use existing or new labels more effectively.

#### Milestones

We use four tags to keep track of issues:

- Next patch (example: "3.9.1")
- Some patch (example: "3.9.x")
- Next minor (example: "3.10")
- Some minor (example: "3.x")

Patch-milestoned issues are those that will require bug fixes, while minor-milestoned issues are things like new
features and major changes that are better left for a minor release. The "Next patch"/"Next minor" milestones mark those issues that we've decided _must_ be addressed before the next respective release. They're either the most painful bugs or most requested features.

When, in the example milestones above, 3.10 is released, we would move all 3.9.x-milestoned issues to 3.10.x,
and then collectively decide which issues ought to move from 3.x to 3.11 and from 3.10.x to 3.10.1.

#### Projects

We use the [cherry-pick](https://github.com/supercollider/supercollider/projects/13) project board to indicate PRs from inexperienced contributors that ought to be cherry-picked from develop to 3.10 after they are merged.

We use the [PR backlog](https://github.com/supercollider/supercollider/projects/7) project board to indicate PRs that have been closed due to inactivity, but would be worthwhile to re-open if there were interest.

### Guideline: Ask questions

If you don't know how to review a PR, or have a question about reviewing, ask a more experienced contributor! These are opportunities to improve our process and identify additional project issues or feature ideas.

### Guideline: It's OK to make mistakes

Pressing the dangerously green "Merge" button can be pretty stressful the first times you go it. Fear not. Mistakes can happen. The main branches of the SuperCollider project are heavily protected against truly disastrous errors, and everything else is easily reversible.

### Guideline: Assume good faith 

Assume that a PR author is acting out of a genuine interest to improve this project. They may not understand technical language or immediately know to provide all the information we normally like to see in a PR. In addition, English may not be their first language. Always be patient and communicate transparently with PR authors. This applies particularly in cases where it is unlikely the PR will get merged.

### Guideline: Stay on topic

In the course of a PR, auxiliary discussions may arise about newly discovered issues, desired features, or even procedural (meta-review) topics. It is crucial that such discussions don't get in the way of reviewing the PR at hand. Any discussion not related to the PR should be respectfully relocated to a more appropriate venue; this may be a new PR, an issue ticket, or a discussion thread on some other forum.