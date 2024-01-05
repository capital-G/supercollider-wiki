# Project tasks organization

This is a freeform / work in progress document that is intended to serve a few purposes:

- provide an overview of the different parts of the project and where work needs to be done
- give people a sense of where they could help out
- help maintainers be more organized

------------------------------

This is mostly based on notes Gianluca took during a conversation with Brian. Feel free to add to it, elaborate on things, move things around, ask questions.

## Most help needed

- quarks
- test frameworks
- reviewing PRs

## Easiest to help with

- eliminate compiler warnings
- get rid of old wikis
- incrementally improve documentation

## Issues by area

project management:

- figure out how to manage PRs/issues efficiently
- testing
- consistent naming style
- build process could be made easier, especially on windows (deps download)

Code quality / project-wide issues:

- eliminate compiler warnings / turn more on
- reorganize sclang primitives to reduce boilerplate / make easier to write
- use modern CMake
- use modern C++ (RAII vs malloc, etc.)
- make a library out of the files in `common/`?
- Pyr → SC_
- finish up inclusive terminology RFC

Long term compatibility

- figure out deprecation policy

Documentation

- translation / translation infrastructure
- get rid of sourceforge page wiki, github.io pages wiki
- find notation for [runtime complexity, exception-safety, etc.] and add to documentation
- improve SCDoc syntax
- fully document 'core' class library like Object, numbers, collections, basic ugens, etc.

IDE

- re-evaluate what to do with it long-term

Language

- debugger
- profiler
- dynamic class library
- imports
- preprocessors?
- better error messages
- better type checking
- language plugins (like bindings to libraries)

scsynth

- merge with supernova?

Plugins:

- easier to put plugins in quarks
- a process to add ugens to main distribution
- how to performance test plugins?
- define a policy for public API for the stuff in `include/`
- move sc3-plugins in quarks

Dependencies de-vendoring

GUIs

- maybe more customization? custom css?

Misc:

- improve unit test framework
- improve quarks

Moderation:

- channel for communication among moderators
- code of conduct
- code of conduct for moderators
