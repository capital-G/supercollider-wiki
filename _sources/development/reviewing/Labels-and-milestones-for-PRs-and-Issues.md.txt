(labels-and-milestones)=
# Labels and milestones for PRs and Issues

Issues and Pull Requests are categorized using a system of [labels](https://github.com/supercollider/supercollider/labels?page=1&sort=name-asc), and the release version that they are targeted for resolution or merging is set by their [milestones](https://github.com/supercollider/supercollider/milestones).

## Labels

Required labels for both Issues _and_ PRs are _either_

- `comp: x` indicates the affected **comp**onent of SuperCollider, _or_
- `env: y` if the issue or PR affects one **env**ironment (SCIDE, Emacs, etc.) in particular

Further required labels for Issues are _either_

- `bug` indicates … a bug, _or_
- `enhancement` indicates a feature request

We do not yet have specific rules or practices around other labels, but other common tags are

bug-related labels

- `crash` – for any bug related to a crash or hang
- `severe` – for non-crashing bugs that otherwise have a severe impact
- `performance` – for any bug related to performance / audio drop-outs / launch time / etc.
- `known issue` / `wont fix` – use this when closing a bug that is not fixed. This is often appropriate for platform issues, Qt issues, or bugs that reflect limitations of SuperCollider itself
- `needs unit test` – use for bugs that are good candidates for a unit test

general labels

- `good first issue` indicates issues that are clear in scope and would be a good place for an interested contributor to start
- `os:...` – for bugs/enhancements that affect only this OS - in general, issues are assumed to affect all OS’s unless this label is present
- `api change` – for enhancements that add new API’s, or change existing API behavior (this especially includes `sclang` and ClassLib changes). Anything with this label should end up in the next minor-version or major-version release, and never a patch release. When closing an issue with this label, verify that the change has been documented
- `duplicate` – use this when closing an issue that is duplicated elsewhere

Feel free to offer suggestions on how we can use existing or new labels more effectively.

If you see an unlabeled issue or PR, please take the time to add a label!

## Milestones

We use four tags to keep track of issues:

- Next patch (example: `3.12.1`)
- Some patch (example: `3.12.x`)
- Next minor (example: `3.13`)
- Some minor (example: `3.x`)

Patch-milestoned Issues will require bug fixes.

"Next” patch/minor milestones mark those issues that we've decided *must* be addressed before the next respective release. They're either the most painful bugs or most requested features.

Minor-milestoned Issues are things like new features and major changes that are better left for a minor release.

An example: 

When `3.13` is released, we would move all `3.12.x`-milestoned Issues to `3.13.x`, then collectively decide which issues ought to move from `3.x` to `3.14` and from `3.13.x` to `3.13.1`.
