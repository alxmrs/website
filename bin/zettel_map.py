"""
Generates a map of my Zettelkasten
"""
import panflute as pf
import collections
import pprint


def prepare(doc):
    doc.graph = collections.defaultdict(list)
    doc.current_doc = ''


def action(elem, doc):

    if isinstance(elem, pf.Link) and not elem.url.startswith('http'):
        pf.debug('------')
        header = get_header(elem)
        # pf.debug('header: ', pf.stringify(header), 'elem: ', elem.url)
        if header:
            doc.current_doc = pf.stringify(header)
        doc.graph[doc.current_doc].append(elem.url)


def is_top_header(elem):
    x = isinstance(elem, pf.Header) and elem.level == 1
    if x:
        pf.debug('header:', elem)
    return x


def get_header(elem):
    pf.debug(elem)
    if elem is None:
        return None

    if is_top_header(elem):
        return elem

    while elem.next is not None and not is_top_header(elem.next):
        elem = elem.next

    while elem.prev is not None:
        if is_top_header(elem):
            return elem
        elem = elem.prev

    return get_header(elem.parent)


def finalize(doc):
    pf.debug(pprint.pformat(doc.graph))


def main(doc=None):
    return pf.run_filter(action, prepare, finalize, doc)


if __name__ == '__main__':
    main()
