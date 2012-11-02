SHELL := /bin/bash

usage:
	@echo 'Usage:'
	@echo '    make release   -- release to pypi'

release:
	python setup.py register sdist upload
