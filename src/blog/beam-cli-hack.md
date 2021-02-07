---
title: Beam Pipelines as CLIs: A Hack
date: 2021-01-04
---

I love using [CLIs installed via Pip](https://python-packaging.readthedocs.io/en/latest/command-line-scripts.html).
I'd much prefer to call a well-named command than I
would run a Python script (e.g. 
`$ python3 main.py ...`). So, when I got a chance 
to build a general-purpose data pipeline at work, I
knew I wanted to follow this UX.

For our project, we used Apache Beam to build 
our pipeline, which we ran on GCP's Dataflow
service. I was surprised to find out that [nowhere
in the documentation](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/)
was there any instruction on 
how to package a Beam pipeline in a pip-installable 
fashion. Sure, the instructions used setuptools, but the 
intention was to ultimately invoke Python on a 
script.

After some trail and error, I ended up figuring out 
a hack to make it work. A full demo of my solution
can be found in [this project on Github](https://github.com/alxrsngrtn/beam-cli-example).

The secret ingredient to make this work was to have
nested `setup.py` files. The inner `setup.py` file 
is necessary so that each Beam worker get the 
dependencies it needs (library code + third party 
deps). However, the other `setup.py` is needed to 
publish the project and make a CLI entry-point 
available.
