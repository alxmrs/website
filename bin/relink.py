#!/usr/bin/env python3
"""Pandoc filter to convert links from markdown-to-markdown files to HTML-to-HTML.

When expressing links in markdown, both Obsidian and PyCharm prefer to target to existing files on
the filesystem, not the eventual generated HTML. Pandoc alone, unfortunately, does not convert the
value of links from ending in ".md" to the final URL value. This filter should fix this problem.
"""

from pandocfilters import toJSONFilter, Link, Image


def relink(key, value, format, meta):
  if key == 'Link':
    # The last value is a tuple known as a "Target"
    url, title = value[-1]

    # Core logic to replace values on a URL. Here, we do three things:
    # - If `src/` is at the front, remove it
    # - If `.md` is at the end, remove it
    # - Add `/` to the front, so it is a relative link.
    new_url = f"/{url.removeprefix('src/').removesuffix('.md')}"

    updated = value[:-1] + [(new_url, title)]
    return Link(*updated)

  if key == 'Image':
    # The last value is a tuple known as a "Target"
    url, title = value[-1]

    # Core logic to make local asset links render properly.
    # When rendering the HTML, refer to the root asset folder.
    if url.startswith('assets/'):
      new_url = f'/{url}'

      updated = value[:-1] + [(new_url, title)]
      return Image(*updated)


if __name__ == "__main__":
  toJSONFilter(relink)
