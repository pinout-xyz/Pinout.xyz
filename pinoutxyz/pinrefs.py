import re
import xml.etree.ElementTree as ElementTree

from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

REFERENCE = re.compile(r'Physical Pin (\d{1,2})(?!\d)|GPIO ?(\d{1,2})(?:/(\d{1,2}))?(?!\d)',
                       re.IGNORECASE)
OPAQUE = ('code', 'pre')
TITLE = 'Click for details about pin {}'


class PinReferences(Treeprocessor):
    def __init__(self, md, pins):
        super().__init__(md)
        self.pins = pins

    def span(self, text, pin, titled):
        span = ElementTree.Element('span')
        if titled:
            span.set('title', TITLE.format(pin))
        span.set('class', 'pin-hover')
        span.set('data-pin', pin)
        span.text = text
        return span

    def nodes(self, match):
        physical, bcm, paired = match.group(1), match.group(2), match.group(3)

        if physical is not None:
            if physical not in self.pins:
                return [], match.start()
            return [self.span(match.group(0), physical, False)], match.end()

        pin = self.pins.bcm_to_physical(bcm)
        if pin is None:
            return [], match.start()

        text = match.group(0)
        partner = None if paired is None else self.pins.bcm_to_physical(paired)

        if partner is None:
            head = text if paired is None else text[:text.rindex('/' + paired)]
            return [self.span(head, pin, True)], match.start() + len(head)

        head = self.span(text[:text.rindex('/' + paired)], pin, True)
        head.tail = '/'
        return [head, self.span(paired, partner, True)], match.end()

    def spans(self, text):
        found = []
        leading = None
        position = 0

        for match in REFERENCE.finditer(text):
            nodes, consumed = self.nodes(match)
            if not nodes:
                continue

            chunk = text[position:match.start()]
            if found:
                found[-1].tail = chunk
            else:
                leading = chunk

            found += nodes
            position = consumed

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
