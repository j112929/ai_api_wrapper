.PHONY: setup install run clean test

VENV := .venv
PYTHON := $(VENV)/bin/python
PIP := $(VENV)/bin/pip

# Default target
all: run

# Create virtual environment if it doesn't exist
$(VENV)/bin/activate:
	python3 -m venv $(VENV)

# Install dependencies
setup: $(VENV)/bin/activate
	$(PIP) install -r requirements.txt

# Run the main application
run: setup
	$(PYTHON) main.py bank_core_legacy.cbl

# Run in demo mode
demo: setup
	$(PYTHON) main.py bank_core_legacy.cbl --demo

# Clean up build artifacts and cache
clean:
	rm -rf __pycache__
	rm -rf core/__pycache__
	rm -f modernized_api.py
	rm -rf build/
	rm -f *.spec

