import re
import xml.etree.ElementTree as ElementTree

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

REFERENCE = re.compile(r'Physical Pin (\d{1,2})|GPIO (\d{1,2})', re.IGNORECASE)
OPAQUE = ('code', 'pre')
TITLE = 'Click for details about pin {}'


class PinReferences(Treeprocessor):
    def __init__(self, md, pins):
        super().__init__(md)
        self.pins = pins

    def physical(self, match):
        physical, bcm = match.group(1), match.group(2)
        if physical is not None:
            return physical if physical in self.pins else None
        return self.pins.bcm_to_physical(bcm)

    def spans(self, text):
        found = []
        leading = None
        position = 0

        for match in REFERENCE.finditer(text):
            pin = self.physical(match)
            if pin is None:
                continue

            chunk = text[position:match.start()]
            if found:
                found[-1].tail = chunk
            else:
                leading = chunk

            span = ElementTree.Element('span')
            if match.group(2) is not None:
                span.set('title', TITLE.format(pin))
            span.set('class', 'pin-hover')
            span.set('data-pin', pin)
            span.text = match.group(0)
            found.append(span)
            position = match.end()

        if not found:
            return None, []

        found[-1].tail = text[position:]
        return leading, found

    def visit(self, element):
        children = list(element)

        for child in children:
            if child.tag not in OPAQUE:
                self.visit(child)

        rebuilt = []
        changed = False

        if element.text:
            leading, found = self.spans(element.text)
            if found:
                element.text = leading
                rebuilt += found
                changed = True

        for child in children:
            rebuilt.append(child)
            if child.tail:
                leading, found = self.spans(child.tail)
                if found:
                    child.tail = leading
                    rebuilt += found
                    changed = True

        if changed:
            for child in children:
                element.remove(child)
            element.extend(rebuilt)

    def run(self, root):
        self.visit(root)


class PinReferenceExtension(Extension):
    def __init__(self, pins):
        super().__init__()
        self.pins = pins

    def extendMarkdown(self, md):
        md.treeprocessors.register(PinReferences(md, self.pins), 'pinrefs', 5)
