export SHELL:=/bin/bash
.ONESHELL:

clean:
	rm -rf .venv

init: clean
	virtualenv .venv
	source .venv/bin/activate
	pip install -r requirements/requirements.txt
	pip3 install --upgrade requests


