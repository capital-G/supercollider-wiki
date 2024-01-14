# scdoc style guidelines

The following guidelines apply to `.schelp` files in _/HelpSource_.

Guidelines are also available for other parts of the project:

[[Style Guidelines: SuperCollider]], [[Style Guidelines: Cpp]], [[The Wiki Wiki]].

## Tag capitalization

Prefer using the lowercase forms of tags (`code:: ::`, `method::`), unless this would break with convention in the context being edited.

## Indentation

Use tabs for indentation, both for schelp-formatted text and code examples.

## Private methods

Hide all of a class's private methods using `private::`.

## Method documentation

Prefer using `argument::` and `returns::` instead of the method description body to document parameters and return values.

Either all of the parameters and/or return value should be documented, or none should be.

When documenting a parameter or return value, make sure to include the expected type.
