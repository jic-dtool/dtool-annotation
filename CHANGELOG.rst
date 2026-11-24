CHANGELOG
=========

This project uses `semantic versioning <http://semver.org/>`_.
This change log uses principles from `keep a changelog <http://keepachangelog.com/>`_.

[Unreleased]
------------

Added
^^^^^


Changed
^^^^^^^


Deprecated
^^^^^^^^^^


Removed
^^^^^^^


Fixed
^^^^^


Security
^^^^^^^^


[0.1.2] - 2026-11-24
--------------------

Added
^^^^^

- GitHub Actions workflow that publishes a release to PyPI when a version
  tag is pushed

Changed
^^^^^^^

- Build system switched to hatchling with hatch-vcs; the version is now
  derived from git tags
- Require ``dtool-cli>=0.7.2``; earlier releases import ``pkg_resources``,
  which is not available without setuptools

Removed
^^^^^^^

- Support for Python < 3.10


[0.1.1] - 2021-06-20
--------------------

Fixed
^^^^^

- Licence file now included in release thanks to Jan Janssen (https://github.com/jan-janssen)



[0.1.0] - 2019-10-25
--------------------

Initial release.

Added
^^^^^

- The CLI command 'dtool annotate set'
- The CLI command 'dtool annotate get'
- The CLI command 'dtool annotate ls'
