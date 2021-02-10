# [Machine Learning: The High Interest Credit Card of Technical Debt](https://research.google/pubs/pub43146/)
```
@inproceedings{43146,
title	= {Machine Learning: The High Interest Credit Card of Technical Debt},
author	= {D. Sculley and Gary Holt and Daniel Golovin and Eugene Davydov and Todd Phillips and Dietmar Ebner and Vinay Chaudhary and Michael Young},
year	= {2014},
booktitle	= {SE4ML: Software Engineering for Machine Learning (NIPS 2014 Workshop)}
}
```

## Summary

It's difficult to enforce strict abstraction boundaries for ML systems, 
unlike in traditional software engineering, due to its inherent depends 
on data (and the data's subsequent quirks).

### Entanglement
ML systems are subject to the CACE principle, or "Change Anything 
Changes Everything".

One way of mitigating this problem is to "isolate models and serve 
ensembles", but this comes with scalability issues. And, within each 
model, entanglement issues still abound. 

Another mitigation: use tools (or metrics) to visualize effects of 
high-dimensional data. 

One can consider using sophisticated regularization techniques to 
enforce that any changes in performance bear a cost to the objective
function in training. However, this is still not a guarantee, and might
add more debt via system complexity. 

Impact of entanglement: "Shipping the first version ... is easy, but
... making subsequent improvements is unexpectedly difficult."

### Hidden Feedback Loops
Systems that depend on data from the world, but _bear an effect on the
state of the world_ have an inherent problem of hidden feedback loops.
For example, a model that predicts some user behavior (CTR of news 
headlines) at `week_t`, but measures that same user behavior at 
`week_{t-1}`. 

In these situations, the ML system can degrade in a way that's 
really hard to notice, esp if models are tested in quick experiments.

Hidden feedback loops should be detected and removed wherever possible. 

### Undeclared Consumers

Without access control for the output of the ML model, some people can
consume the service _undeclared_. This will tightly couple other parts
of the stack to that model, which can be detrimental to the system, and
can make it hard to change your ML model. Further, it can introduce a 
hidden feedback loop!

### Unstable Data Dependencies

_Unstable_ input signals qualitatively change behavior over time.
Changes and improvements to an input signal may be regularly rolled out, 
but this may adversely affect downstream ML models (CACE). 

Mitigation: version signals. Then, updates can be vetted. However, 
care is needed to manage versions well, as to not create other 
technical debt.

### Underutilized Data Dependencies

_Underutilized_ dependencies are packages that are mostly unneeded.
These are features that provide little incremental value.

These are costly since they make systems unnecessarily vulnerable to 
change. These data deps can come is as *legacy features* (needed once, 
but necessary no longer), *bundled features* (a group of features
is found to be beneficial, but some are not that valuable), or
*epsilon-features* (added to marginally improve the model accuracy).

Mitigation: regularly evaluate the effect of removing individual 
features.

### Static Analysis of Data Dependencies

Without static analysis of data dependencies, it can be difficult
to manually track the use of data in the system. It's possible that
an upstream team can change something about the data and have unknown
effects on many consumers. On the other side, a maintainer of some
data source might bot be able to delete / clean up their data out of
fear that they may affect some downstream consumer. 

(What if they somehow used Bazel?)

### Correction Cascades

A model "correction" is where you learn a model `a'(a)` that takes 
another model `a` and learns a small correction to solve a different
but related problem. 

While this is good to create a first version, this creates a system
dependency on model `a`. It's possible that improving the accuracy of
`a` could lead to systems-level detriments. 

Mitigation: augment `a` to learn the corrections directly within the 
same model by adding features to help that model distinguishs
among the various use cases. 

(My perspective: it seems like what the authors are recommending 
against has since taken off with huge successes – Transfer Learning.)

### Glue Code

_Glue code_ is where a massive amount of supporting code is written to 
get data into an out of general-purpose packages. 
Glue code can freeze the system to the peculiarities of a specific
package. 

Sometimes, to reduce glue code, it's better to re-implement the ML 
algorithm with considerations for the whole system rather than to 
re-use a package from a library. The resulting system may be
easier to test & maintain. You can also inject specific optimizations 
for your specific problem. (See: e.g. )


