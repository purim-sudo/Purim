.PHONY: test test-python test-node install-node

test: test-python test-node

test-python:
	PYTHONPATH=PurimMonitor python -m unittest discover -s PurimMonitor/tests
	PYTHONPATH=NetWatch python -m unittest discover -s NetWatch/tests
	python -m compileall PurimMonitor NetWatch

install-node:
	cd SecureShare && npm install

test-node: install-node
	cd SecureShare && npm test
