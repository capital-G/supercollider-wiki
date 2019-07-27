Continuous Integration and Skipping Commits
-------------------------------------------

We have CI provided by AppVeyor (Windows) and Travis (Linux, macOS). If a commit changes _only_
non-schelp documentation, _without_ renaming, adding, or removing files, you may want to consider
adding `[skip ci]` to the commit message so it does not waste CI resources.

S3 Build Hosting
----------------

Builds of all commits to branches on the main project repository are uploaded to Amazon's S3 hosting service. This means that commits in Pull Requests are often not uploaded, which is the case if they originate from other respositories (i.e. forks). These builds are available for macOS, Windows x86, and Windows x86-64. To download the latest build of a branch named `topic/foo`, the URLs are of the form:

* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/osx/topic/foo-latest.html
* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/win32/topicfoo-latest.html
* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/win64/topicfoo-latest.html

Note that for the Windows builds only, the branch name is stripped of forward slashes.

To find a build for a specific commit (assuming it exists), use the full SHA hash of the commit. For example, the
binaries for commit
[8c3563a8065cb623087f267dfe50e228224a4572](https://github.com/supercollider/supercollider/commit/8c3563a8065cb623087f267dfe50e228224a4572)
are at:

* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/osx/SC-8c3563a8065cb623087f267dfe50e228224a4572.zip
* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/win32/SC-Windows-x86-8c3563a8065cb623087f267dfe50e228224a4572.zip
* http://supercollider.s3.amazonaws.com/builds/supercollider/supercollider/win64/SC-Windows-x64-8c3563a8065cb623087f267dfe50e228224a4572.zip

A build for a specific commit may not always be available: for instance, if the build was cancelled early or failed to
complete.

AppVeyor builds
---------------
Independently from Amazon S3 hosting service, AppVeyor stores its Windows builds temporarily for 6 months. In contrast to the Amazon S3 hosting, these builds are available for _all_ pull requests. The URL to these builds includes AppVeyor's job number and is unrelated to commit SHA, e.g.

`https://ci.appveyor.com/api/buildjobs/76sh4cu20rh50bp1/artifacts/art_folder.zip`

These builds may be accessed either from [AppVeyor's build history](https://ci.appveyor.com/project/supercollider/supercollider/history), or from individual pull request's page. For the latter, find section `All checks have passed` at the bottom of the page, toggle `Show all checks` and choose `Details` next to the AppVeyor entry.

On the page with the selected build, choose the desired job from the list (32bit vs 64bit), and then `artifacts` on the right. This will reveal a link to `art_folder.zip` which contains the build.

Boost Update Script
-------------------

Location: `external_libraries/extract_boost.sh`, `external_libraries/boost_sc_changes.patch`

### Purpose

Update Boost libraries packaged with SuperCollider, and apply the SuperCollider organization's patches for Boost.

### Usage

Should be run as soon as possible after a new release of Boost. See instructions in `external_libraries/README_BOOST.md`
for more information.
