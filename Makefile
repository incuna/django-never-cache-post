SHELL := /bin/bash

usage:
    @echo "make release   -- release to pypi"

release:
    python setup.py register sdist upload
