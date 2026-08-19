LANG ?= en

LANG := $(subst -, ,$(LANG))
LANG := $(subst _, ,$(LANG))
LANG := $(firstword $(LANG))

PYTHON ?= python3
PINOUTXYZ := $(PYTHON) -m pinoutxyz

.PHONY: all deps html site serve watch translations check clean

all: site

deps:
	$(PYTHON) -m pip install -r requirements.txt

html:
	$(PINOUTXYZ) build $(LANG)

site:
	$(PINOUTXYZ) build --site

serve:
	$(PINOUTXYZ) serve --lang $(LANG)

watch:
	$(PINOUTXYZ) serve --lang $(LANG) --watch

translations:
	$(PINOUTXYZ) translations list

check:
	$(PINOUTXYZ) translations check

clean:
	rm -rf output
