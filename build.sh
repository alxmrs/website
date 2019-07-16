#!/usr/bin/env bash

# Inspired by Will Styler: http://wstyler.ucsd.edu/posts/lmimg/spcv.txt

echo "Rendering site"
find . -name "*.md" -type f -exec \
 pandoc -B includes/header.html \
        -A includes/footer.html \
        --highlight-style=kate \
        -c /css/main.css \
        --email-obfuscation=javascript \
        -t html5 \
        -V pagetitle="Alex Rosengarten" \
        -o {}.html {} \;
find . -depth -name '*.md.html' -execdir bash -c 'mv "$1" "${1/md.html/html}"' bash {} \;
echo "Rendering complete"