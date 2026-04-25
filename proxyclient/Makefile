.PHONY: all build clean upload-testpypi

DATADIR := m1n1
VERSION := $(shell grep '^version = ' pyproject.toml | sed 's/version = "\(.*\)"/\1/')
WHEEL := dist/m1n1_proxyclient-$(VERSION)-py3-none-any.whl
TARBALL := dist/m1n1_proxyclient-$(VERSION).tar.gz

SOURCES := $(shell find m1n1 -name '*.py' 2>/dev/null)
DATA_FILES := $(DATADIR)/apple_regs.json $(DATADIR)/arm_regs.json

all: $(WHEEL) $(TARBALL)

$(WHEEL) $(TARBALL): pyproject.toml $(SOURCES) $(DATA_FILES)
	poetry build

build: $(WHEEL) $(TARBALL)

publish-test: $(WHEEL) $(TARBALL)
	twine upload --repository testpypi $(WHEEL) $(TARBALL)

publish: $(WHEEL) $(TARBALL)
	twine upload $(WHEEL) $(TARBALL)

clean:
	rm -rf dist/
