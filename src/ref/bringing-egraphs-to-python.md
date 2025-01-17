---
title: Bringing E-Graphs to Python
date: 2025-01-15T11:34
description-meta: 
status: 
tags:
  - ml
  - formal-methods
  - python
  - pl
  - accelerators
  - programming
---
![e-graphs-good](https://egraphs-good.github.io/assets/egg.svg)
![The Scientific Python Ecosystem](https://jupytearth.org/_images/python-stack.png)

Common things I take away from Saul's talk: 
* OSS Python could substantially benefit from frontier programming language (PL) research
* Talks about the birth of NumPy in 1995
* NumPy is "pointers, strides, dtypes" between Python and C arrays.
* History of OSS Python is an ecosystem of collaborative, multi-stakeholder, interdependent yet individual projects. 
* Terrific overview of the PyData library --> compiler / hardware targets, c. 2019
  !["How do we support targets today?"](https://egglog-python.readthedocs.io/latest/_images/ecosystem-graph.png)
  * With new heterogenous hardware environments and heavy industry incentives up and down the software/hardware stack, tools seldom interoperate anymore. **Now, people have to choose silos in Python.**
  * This talk argues that the entire python ecosystem is a compiler! (maybe, one that doesn't interoperate very well.)
  * egglog / egraphs make it easier for different libraries to write their own piece of the bigger compiler that is PyData


---
# References
["Bringing E-Graphs to Python by _Saul Shanabrook_](https://egglog-python.readthedocs.io/latest/explanation/2023_11_09_portland_state.html)

