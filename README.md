# Notmuch2 Python Bindings

**If you are using notmuch v1, please checkout [notmuch](https://pypi.org/project/notmuch/)**

Pythonic bindings for the notmuch mail database using CFFI. This module makes
the functionality of the notmuch library (`https://notmuchmail.org`) available
to python using [CFFI](https://cffi.readthedocs.io/en/latest/)

_Disclaimer:_

Notmuch version 2 is still not released yet even it has already a second release
candidate. Please expect possible breaking changes.

## Installation

The intention of this repository is to make these bindings easily available for
dependency management. It is originally taken from
`https://git.notmuchmail.org/git/notmuch/bindings/python-cffi`.

### PyPI

Install the build project from [PyPI](https://pypi.org/).

```shell
$ pip install notmuch2
```

```shell
$ poetry add notmuch2
```

### Git

Reference the pure sources from
[GitHub](https://github.com/weilbith/notmuch-python-bindings2).

```shell
pip install from git+https://github.com/weilbith/notmuch2
```

```shell
poetry add --git=https://github.com/weilbith/notmuch2
```
