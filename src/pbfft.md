---
title: "The Petabyte FFT: Accelerated Cubed"
date: 2025-01-14T16:00
status: draft
tags:
  - designdoc
  - python
  - jax
  - ml
---
_Originally sketched on September 29, 2023_

I'm incredibly excited about [Cubed](https://cubed-dev.github.io/cubed/). When I first learned about the project via this [Xarray blog post](https://xarray.dev/blog/cubed-xarray) (which is my favorite intro to the project, short of reading the docs), I knew it was a project worth betting on. To be able to perform array computation serverlessly -- without having to worry about managing memory (!!) -- seems like the future of data science in the cloud. 

Maybe the primary source of my excitement was in this project's potential to change array acceleration. Today, performing computation with arrays on GPUs/TPUs is still really difficult, even with the cloud. 

![All hope is lost](https://preview.redd.it/explain-please-v0-ma2mz5wxftod1.jpeg?auto=webp&s=2b90dfa3b12e064f54333e1080b3dabbad914f48)
– _[source](https://www.reddit.com/r/ExplainTheJoke/comments/1fgsbw7/explain_please/)_

Even more difficult, today, is working with really, really large arrays on accelerators. For most ML projects, the standard recommendation is to put as much of the dataset in memory (i.e. RAM) in order to minimize wasted cycles traversing the memory hierarchy (both the CPU and (G/T)PU hierarchies). Most ML data pipelines (e.g. tfds) are designed to efficiently schedule resources (network, disk, RAM, CPUs, etc.) to keep GPUs saturated. ML examples are often written into protobuf (tf.records) or flatbuffers (I assume what pytorch uses?) and then efficiently loaded into memory to keep [accelerator hardware as busy as possible](hazy-research-and-flash-attention). 

This become much, much tricker to do when you can't dump all your tf.Examples in memory, or even on disk. This setting is common in the world of frontier LLMs, but more interesting to me, in scientific computing settings. How do you train an ML models when your dataset is over a petabyte in size (or, say, [6 PiBs](https://x.com/shoyer/status/1805735177517416749))?

Worse, still: many modern ML tasks don't only make use of a single dataset, but multiple. Each example is commonly a [jittered](jitter) combination of several data sources. In the geosciences, for example, it's really typically to require combinations of multi-petabyte data sources. Can you imagine pre-caching these windowed combinations as protobufs? It literally could _factorially_ expand the amount of data needed to be stored -- starting from petabytes!!

This, in a nutshell, is why work improving cloud-optimized data loaders is so important. Imagine keeping accelerators busy while creating ML examples just-in-time. Since streaming data into the unit of compute is inevitable when it can only be stored in cloud buckets, data loaders keeps accelerators saturated by navigating the memory hierarchy for you, hopefully with a flexible interface. [xbatcher](https://earthmover.io/blog/cloud-native-dataloader/), pioneered by [EarthMover](https://earthmover.io/) and the [Pangeo collective](https://pangeo.io/), is one such example of this infrastructure. Maybe the one I'm most excited to use soon is [this internal data loader](https://github.com/neuralgcm/neuralgcm/issues/97) developed by the team who created [NeuralGCM](https://research.google/blog/fast-accurate-climate-modeling-with-neuralgcm/). (I figure, the more I keep talking about it, the more likely the good folks at Google will turn it into an open source package 😉). This is also why, I argue, investment spent [benchmarking and optimizing the internal components](https://github.com/earth-mover/icechunk/issues/570) of these data loaders is time well spent. 

Data loading is an important component in effortless array computation in the cloud. Maybe a second critical component is accelerating array computation. 

---
_early notes for the post_.


What would it take to compute an FFT on a Petabyte of data on distributed accelerators? Say, how could we perform an FFT on ARCO-ERA5 across a rig of TPUs s.t. a) it would not run out of memory b) finish in a reasonable amount of time (about a day? an hour? minutes?)?

Specifically, could we mold Cubed to make this effortless?

https://github.com/cubed-dev/cubed/issues/304



## Why build this?

This could provide a new programming model for scientific supercomputing. It could make ML development across large datasets (e.g. Geospatial, Weather, Microscopy) or even traditional modern ML (LLMs) much easier to implement. 

## What is the right intersection?

- MLIR?
    - Mojo
    - Direct via dialect
- XLA?
    - Jax
    - Direct via bindings
- Triton?
    - Python bindings
    - Interesting due to core concept of tiles

What have I done so far? 
https://github.com/cubed-dev/cubed/issues?q=+is%3Aissue+author%3Aalxmrs+ 

---
# References

- https://github.com/jax-ml/jax/discussions/10131
