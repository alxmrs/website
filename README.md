# alxrsngrtn.github.io
The source code for [alexrosengarten.com](https://alexrosengarten.com).

## What's this website all about?
It's a place for me to cross reference public profiles, host assets like profile pics, and occasionally share my 
thoughts (usually on programming).

## I got here from a comment in my browser's dev tools... now what?
I dunno. You and I are both in unexplored territory here. Maybe... star this repo?

## Setup
**Pre-requisite**: Install [`pandoc`](https://pandoc.org/installing.html)
- I installed `pandoc` via Anaconda: 
  1. [Install `Anaconda`](https://docs.conda.io/projects/continuumio-conda/en/latest/user-guide/install/download.html)
  1. Create a conda environment for working with this website: `conda create -n website python=3.6 -y`
  1. `conda activate website`
  1. `conda install pandoc`
1. Add, remove, edit Markdown files
1. `./build.sh`
1. [Serve the static contents](https://gist.github.com/willurd/5720255) to see if you're happy with the site.
1. Commit + push the changes to `master` 
1. That's it!
