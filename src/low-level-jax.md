---
title: Low-level control in Jax with `shard_map` and Pallas
date: 2025-01-17T14:25
description-meta: 
status: 
tags:
  - jax
  - accelerators
  - python
---
_Notes from the OpenXLA talk:_ JAX: Low-level control with shard_map and Pallas. _See references for the full video._

## Shard-Map
"A souped-up parallel map" that parallelizes functions on multiple devices, with each device receiving a different shard from the input data.

"shmapped"
![](assets/shard-map.png)
## Custom Kernels

### `triton_call`
Call triton code from Jax

### `pallas_call`
Recommended. Expresses Kernes in Jax.

Custom kernels take in GPU array references (buffers), not arrays. Must be loaded before computations can be run. 
![](assets/pallas-kernels-example.png)
Refs support mutation, unlike the rest of Jax!

![](assets/calling-a-pallas-kernel-in-jax.png)

Pallas concepts like Grid and Block specs allow us to automatically pipeline memory access in TPU and run across multiple async threads in GPU.

Because matmul can be implemented recursively, we can break down a big matmul into a smaller one. Then, small kernels can be more effectively utilized on the hardware.

**Grids**: specify how many times we exec the kernel, and specify which instance of the kernel to execute. The grid, on GPU, is executed asynchronously in parallel, and on TPU is executed sequentially, pipelined.
![](assets/matmul-pallas-grids.png)

**Block shape**: How do we break down the inputs and outputs into smaller components to be operated on by the kernel. 
![](assets/matmul-pallas-block-shape.png)
Pallas will automatically care up arrays into the right block shape.

**Index map**: for a particular instance in the kernel in teh grid, which blocks should be inputs vs outputs. 
![](assets/matmul-pallas-index-map.png)

## Why Pallas?
* Need to express an idea against the wishes of the compiler. Or, it's easier to work low level.
* Supports both TPU (Mosaic/MLIR) and GPU (Triton).
* It can sometimes fuse normal JITed code with custom kernel code!!
* Don't need to learn new APIs, just use JAX
* Debuggable
* Memory access APIs allow for advanced scheduling optimizations
* TPU Only: remote DMAs (allows custom collective kernels)
	* TODO(alxmrs): I need to look this up.

## Is there a program model difference btw Pallas and Triton?
Main difference: Pallas is higher level wrt memory access. You can say up-front what memory you're going to use and it allows for automatic scheduling. 

Pallas does not have autotuning like Triton does.


---
# References
<iframe width="560" height="315" src="https://www.youtube.com/embed/5ilr4gcenaA?si=lPJ-jEjwFElzND-Z&amp;start=89" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

