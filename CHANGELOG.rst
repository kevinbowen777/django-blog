.. _`changelog`:

=========
Changelog
=========

``django-blog`` issues are filed on `GitHub <https://github.com/kevinbowen777/django-blog/issues>`_, and each ticket number here corresponds to a closed GitHub issue.

All notable changes to this project will be documented in this file.

The format is based on `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_, and this project adheres to `Semantic Versioning <https://semver.org/spec/v2.0.0.html>`_.

This project uses `towncrier <https://towncrier.readthedocs.io/>`_ for keeping
the changelog. DO NOT commit any changes to this file.

Backward incompatible (breaking) changes should only be introduced in major versions
with advance notice in the **Deprecations** section of releases.


..
    You should *NOT* be adding new change log entries to this file, this
    file is managed by towncrier. You *may* edit previous change logs to
    fix problems like typo corrections or such.
    To add a new change log entry, please see
    https://pip.pypa.io/en/latest/development/contributing/#news-entries
    but note that in toolbox the "news/" directory is named "changelog/".

.. towncrier release notes start

django-blog 0.3.5 (2026-08-11)
==============================

Improved documentation
----------------------

-  (`#644 <https://github.com/kevinbowen777/django-blog/644>`_): Add towncrier 25.8.0.


New features
------------

-  (`#670 <https://github.com/kevinbowen777/django-blog/670>`_): Upgrade to Django 6.0.8

django-blog 0.3.4 (2026-07-24)
==============================

Contributor-facing changes
--------------------------

-  (`#448 <https://github.com/kevinbowen777/django-blog/448>`_): Update Docker with Python 3.14 & Postgres 15.15.

-  (`#458 <https://github.com/kevinbowen777/django-blog/458>`_): Add Python 3.14 support.

-  (`#662 <https://github.com/kevinbowen777/django-blog/662>`_): Update with Python 3.14.6 & 3.13.14.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#658 <https://github.com/kevinbowen777/django-blog/658>`_): Drop support for Python 3.11.


New features
------------

-  (`#660 <https://github.com/kevinbowen777/django-blog/660>`_): Upgrade Django to 5.2.15.

django-blog 0.3.3 (2025-04-29)
==============================

Contributor-facing changes
--------------------------

-  (`#561 <https://github.com/kevinbowen777/django-blog/561>`_): Upgrade PostgreSQL to 15.11.

-  (`#572 <https://github.com/kevinbowen777/django-blog/572>`_): Update Poetry to 2.1.2.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#568 <https://github.com/kevinbowen777/django-blog/568>`_): Drop Python 3.10 support.


Improved documentation
----------------------

-  (`#567 <https://github.com/kevinbowen777/django-blog/567>`_): Update Sphinx to 8.2.3.


New features
------------

-  (`#561 <https://github.com/kevinbowen777/django-blog/561>`_): Upgrade Docker image to Python 3.13 & Poetry 2.1.1.

-  (`#574 <https://github.com/kevinbowen777/django-blog/574>`_): Upgrade Django to 5.2.


Security updated
----------------

-  (`#576 <https://github.com/kevinbowen777/django-blog/576>`_): Replace safety package with pip-audit.

django-blog 0.3.2 (2025-01-09)
==============================

Contributor-facing changes
--------------------------

-  (`#500 <https://github.com/kevinbowen777/django-blog/500>`_): Upgrade to psycopg 3.

-  (`#509 <https://github.com/kevinbowen777/django-blog/509>`_): Add support for Python 3.13

-  (`#548 <https://github.com/kevinbowen777/django-blog/548>`_): Re-build pyproject for Poetry 2.0.


New features
------------

-  (`#540 <https://github.com/kevinbowen777/django-blog/540>`_): Upgrade Django to 5.1.4

django-blog 0.3.0 (2023-12-21)
==============================

Contributor-facing changes
--------------------------

-  (`#369 <https://github.com/kevinbowen777/django-blog/369>`_): Bump Safety version to 2.4.0.

-  (`#406 <https://github.com/kevinbowen777/django-blog/406>`_): Upgrade Poetry to 1.7.1.

-  (`#415 <https://github.com/kevinbowen777/django-blog/415>`_): Update Python to 3.12.1.


Deprecations (removal in next major release)
--------------------------------------------

-  (`#235 <https://github.com/kevinbowen777/django-blog/235>`_): Drop support for Python 3.9.


Improved documentation
----------------------

-  (`#318 <https://github.com/kevinbowen777/django-blog/318>`_): Update Sphinx theme to Furo


New features
------------

-  (`#411 <https://github.com/kevinbowen777/django-blog/411>`_): Upgrade to Django 5.0.

django-blog 0.2.0 (2023-05-11)
==============================

Contributor-facing changes
--------------------------

-  (`#244 <https://github.com/kevinbowen777/django-blog/244>`_): Install ruff. Drop flake8-* packages.

django-blog 0.1.0 (2023-05-08)
==============================

Contributor-facing changes
--------------------------

- : Implement nox for testing

- : Mirror to GitLab.

-  (`#15 <https://github.com/kevinbowen777/django-blog/15>`_): Drop pipenv for project management. Add Poetry.

-  (`#216 <https://github.com/kevinbowen777/django-blog/216>`_): Add support for Python 3.12.

-  (`#222 <https://github.com/kevinbowen777/django-blog/222>`_): Re-write for compatibility with Poetry 1.4.1.

-  (`#227 <https://github.com/kevinbowen777/django-blog/227>`_): Upgrade PostgreSQL to 15.2


Improved documentation
----------------------

-  (`#30 <https://github.com/kevinbowen777/django-blog/30>`_): Add Sphinx for documentation


New features
------------

-  (`#245 <https://github.com/kevinbowen777/django-blog/245>`_): Upgrade to Django 4.2.

django-blog 0.0.1 (2022-02-25)
==============================

New features
------------

- : Build Docker support for Heroku deployment.

- : Support Django 4.0.4.


Miscellaneous internal changes
------------------------------

- : Initial commit
