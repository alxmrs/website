# website

![pandoc-build](https://github.com/alxmrs/website/workflows/pandoc-build/badge.svg)
![shellcheck](https://github.com/alxmrs/website/workflows/shellcheck/badge.svg)

Source for [alex.merose.com](https://alex.merose.com) – statically generated with [Pandoc](https://pandoc.org).

## Use

See my [`pandoc-website-template`](https://github.com/alxmrs/pandoc-website-template) project.

To build once:

- [Install Pandoc](https://pandoc.org/installing.html), e.g. `bin/install` on a debian machine.
- `bin/build`

Thereafter, to develop iteratively: 

- `bin/watch`
- (in another terminal) `cd public && python -m http.server`
