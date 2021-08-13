# Beam Pipelines as CLIs: A Hack

*2021-02*

*updated: 2021-08*

While building a [Beam](https://beam.apache.org/) pipeline for work, I found 
myself surprised to find there was [no documentation](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/)
on how to structure the pipeline as a CLI [[1]](#1). I wanted to make running 
my pipeline as easy as possible. What's easier than installing a python 
package via pip, and invoking a well-documented command? With features like
[`pip search`](https://pip.pypa.io/en/stable/reference/pip_search/#) and 
`--help` messages, one never needs to leave the terminal.

It's a bit strange to structure a Beam pipeline as a CLI. When I usually use 
CLIs, I think about manipulating files on my local machine, not orchestrating a
distributed system to process potentially petabytes of data. Maybe this is 
starting to change. AWS, GCP, and the like all offer developers the ability to 
manipulate whole cloud architectures from a CLI. Why not do the same for my ETL
job?

After some trail and error, I ended up figuring out a hack to make it work. A 
full demo of my solution can be found in [this project on Github](https://github.com/alxmrs/beam-cli-example).

```
.
├── LICENSE
├── README.md
├── mytool
│   ├── __init__.py
│   ├── boom
│   ├── setup.py
│   └── subtool
│       ├── __init__.py
│       ├── helper.py
│       └── main.py
└── setup.py

2 directories, 9 files
```

The secret ingredient to getting this right was to have nested `setup.py` files.
The inner `setup.py` file is necessary so that each Beam worker gets the 
dependencies it needs (library code + third party deps). However, the outer
`setup.py` is needed to publish the project and make a CLI entry-point 
available. The script registered in the outer setup file, here called `boom`,
passes the path to the inner setup file. 

This may be unclear, let me show rather than tell: 

```python
#!/usr/bin/env python3
# mytool/boom

import glob
import logging
import os
import subprocess
import sys
import tempfile

import mytool

if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)

    site_pkg = mytool.__path__[0]

    try:
        from subtool import cli
    except ImportError:
        # Install the subpackage.
        subprocess.check_call(f'{sys.executable} -m pip install {site_pkg}'.split())

        from subtool import cli

    with tempfile.TemporaryDirectory() as tmpdir:
        # Convert subpackage to a tarball
        subprocess.check_call(
            f'{sys.executable} {site_pkg}/setup.py sdist --dist-dir {tmpdir}'.split(),
        )

        # Set tarball as extra packages for Beam.
        dist_files = glob.glob(os.path.join(tmpdir, '*.tar.gz'))
        cli(['--extra_package', dist_files[0]])

```

This imports the `cli` function, an entrypoint to the pipeline. 
The `--extra_package` is a standard way to [package non-PyPi dependencies](https://beam.apache.org/documentation/sdks/python-pipeline-dependencies/#local-or-nonpypi)
in your pipeline. 

```python
# mytool/subtool/__init__.py

from .main import run


def cli(extra=[]):
    import sys
    run(sys.argv + extra)
```

Thus, by nesting packages and pointing to the path to the inner package, 
we get the best of both worlds: Beam can install the inner package as a
library to each remote worker. Users can install the tool using python 
standards. 

---
<span id="1">**1**</span>: Sure, the docs talk about packaging workers with `setuptools`,
but this explanation lacks my use case exactly. The workers still
need to be run from an executor, and I want that executor to be
installed with pip.
