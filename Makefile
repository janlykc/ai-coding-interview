PYTHON ?= python3
VENV := .venv
VPY := $(VENV)/bin/python

.PHONY: setup doctor test lint format build check
setup:
	$(PYTHON) -m venv $(VENV)
	$(VPY) -m pip install -r requirements-dev.lock
	$(VPY) -m pip install --no-build-isolation --no-deps -e .
doctor:
	$(VPY) scripts/harness.py doctor
test:
	$(VPY) -m pytest tests/harness
lint:
	$(VPY) -m ruff check .
	$(VPY) -m ruff format --check .
format:
	$(VPY) -m ruff format .
build:
	$(VPY) -m build --no-isolation
check: lint test build doctor
