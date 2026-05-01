.PHONY: all build clean publish publish-test

PYTHON ?= python3
TWINE ?= twine

DATADIR := m1n1
VERSION := $(shell python -c "import setuptools_scm; print(setuptools_scm.get_version(search_parent_directories=True), end='')" )
WHEEL := dist/m1n1_proxyclient-$(VERSION)-py3-none-any.whl
TARBALL := dist/m1n1_proxyclient-$(VERSION).tar.gz
$(info VERSION=$(VERSION) WHEEL=$(WHEEL) TARBALL=$(TARBALL))

SOURCES := $(shell find m1n1 -name '*.py' 2>/dev/null)
DATA_FILES := $(DATADIR)/apple_regs.json $(DATADIR)/arm_regs.json

all: $(WHEEL) $(TARBALL)

$(WHEEL) $(TARBALL): pyproject.toml $(SOURCES) $(DATA_FILES)
	$(PYTHON) -m build

build: $(WHEEL) $(TARBALL)

publish-test: $(WHEEL) $(TARBALL)
	$(TWINE) upload --repository testpypi $(WHEEL) $(TARBALL)

publish: $(WHEEL) $(TARBALL)
	$(TWINE) upload $(WHEEL) $(TARBALL)

clean:
	rm -rf dist/ m1n1/_version.py m1n1_proxyclient.egg-info
