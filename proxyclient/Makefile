.PHONY: all test build clean publish publish-test

PYTHON ?= python3
TWINE ?= twine

DATADIR := m1n1
VERSION := $(shell python setup.py --version)
WHEEL := dist/m1n1_proxyclient-$(VERSION)-py3-none-any.whl
TARBALL := dist/m1n1_proxyclient-$(VERSION).tar.gz
$(info VERSION=$(VERSION) WHEEL=$(WHEEL) TARBALL=$(TARBALL))

SOURCES := $(shell find m1n1 -name '*.py' 2>/dev/null)
DATA_FILES := $(DATADIR)/apple_regs.json $(DATADIR)/arm_regs.json
PACKAGING_FILES := pyproject.toml setup.py MANIFEST.in LICENSE README.md

all: build

build: $(WHEEL) $(TARBALL)

$(WHEEL) $(TARBALL): $(SOURCES) $(DATA_FILES) $(PACKAGING_FILES)
	$(PYTHON) -m build

publish-test: $(WHEEL) $(TARBALL)
	$(TWINE) upload --repository testpypi $(WHEEL) $(TARBALL)

publish: $(WHEEL) $(TARBALL)
	$(TWINE) upload $(WHEEL) $(TARBALL)

test:
	LC_ALL=C pytest

clean:
	rm -rf dist/ m1n1/_version.py m1n1_proxyclient.egg-info
