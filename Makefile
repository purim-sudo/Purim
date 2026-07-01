.PHONY: test test-python test-node install-node

test: test-python test-node

test-python:
	PYTHONPATH=PurimMonitor python -m unittest discover -s PurimMonitor/tests
	PYTHONPATH=NetWatch python -m unittest discover -s NetWatch/tests
	PYTHONPATH=LogLens python -m unittest discover -s LogLens/tests
	python -m compileall PurimMonitor NetWatch LogLens

install-node:
	cd SecureShare && npm ci

test-node: install-node
	cd SecureShare && npm test
