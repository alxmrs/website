"""
Generates a map of my Zettelkasten
"""
import panflute as pf
import collections
import pprint


def prepare(doc):
    doc.graph = collections.defaultdict(set)
    doc.current_doc = ''


def action(elem, doc):
    if isinstance(elem, pf.Doc):
        return None
    if isinstance(elem, pf.Link) and not elem.url.startswith('http'):
        pf.debug('------')
        header = get_header(elem)
        # pf.debug('header: ', pf.stringify(header), 'elem: ', elem.url)
        if header:
            doc.current_doc = pf.stringify(header)
        doc.graph[doc.current_doc].add(elem.url)

        pf.debug(elem.get_metadata())
        pf.debug(elem)

        return elem
    return []


def is_top_header(elem: pf.Element):
    x = isinstance(elem, pf.Header) and elem.level == 1
    # if x:
    #     pf.debug('header:', elem)
    return x


def get_header(elem: pf.Element):
    # pf.debug(elem)

    original_elem = elem

    if elem is None:
        return None

    if is_top_header(elem):
        return elem

    while elem is not None:
        # pf.debug('>>>>>>>>', pf.stringify(elem))
        if is_top_header(elem):
            return elem
        elem = elem.prev

    return get_header(original_elem.parent)


def finalize(doc):
    pf.debug(pprint.pformat(doc.graph))


def main(doc=None):
    return pf.run_filter(action, prepare, finalize, doc)


if __name__ == '__main__':
    main()
