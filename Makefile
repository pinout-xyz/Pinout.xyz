LANG ?= en-GB

LANG := $(subst .UTF-8,,$(LANG))
LANG := $(subst _,-,$(LANG))

all:
	./generate-html.py $(LANG)
	cp -r resources output/$(LANG)/

clean:
	rm -r output/$(LANG)/*

serve: all
	./serve.py $(LANG)
