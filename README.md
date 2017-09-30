# Environment File

This is a very simple package that makes it simple
to load a value from an environment variable if
one exists. If the environment variable is not
defined, then a file will be checked to see if a
variable with that name exists.

## Use case

This package is intended to be used in a scenario
where there are environment variables used in the
production environment for an application, but
these variables are either different or are more
convenient to define in a file in the development
environment.

## Installation

```
pip install environment-file
```
