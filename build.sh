#!/usr/bin/env bash

# Inspired by Will Styler: http://wstyler.ucsd.edu/posts/lmimg/spcv.txt

echo "Rendering Site"
find src -name "*.md" -type f -exec pandoc -B includes/header.html -A includes/footer.html -o {}.html {} \;
find . -depth -name '*.md.html' -execdir bash -c 'mv "$1" "${1/md.html/html}"' bash {} \;
find src -depth -name '*.md.html' -execdir bash -c 'mv "$1" ..' bash {} \;
