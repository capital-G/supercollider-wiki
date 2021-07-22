Every issue should have one of these two labels:

- `bug` – application misbehavior
- `enhancement` – any request that describes new behavior or functionality

### bug-related labels

- `crash` – for any bug related to a crash or hang
- `severe` – for non-crashing bugs that otherwise have a severe impact
- `performance` – for any bug related to performance / audio drop-outs / launch time / etc.
- `known issue` / `wont fix` – use this when closing a bug that is not fixed. This is often appropriate for platform issues, Qt issues, or bugs that reflect limitations of SuperCollider itself
- `needs unit test` – use for bugs that are good candidates for a unit test

### general labels

- `duplicate` – use this when closing an issue that is duplicated elsewhere
- `api change` – for enhancements that add new API’s, or change existing API behavior (this especially includes `sclang` and ClassLib changes). Anything with this label should end up in the next minor-version or major-version release, and never a patch release. When closing an issue with this label, verify that the change has been documented
- `comp:...` – comp tags reflect the area of SuperCollider that this bug or enhancement affects
- `env:...` – for bugs/enhancements that pertain to a specific work environment (i.e. the IDE)
- `os:...` – for bugs/enhancements that affect only this OS - in general, issues are assumed to affect all OS’s unless this label is present