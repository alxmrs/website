---
title: Notes on Torch Datasets & DataLoaders
date: 2025-02-11T14:07
description-meta: 
status: 
tags:
  - ml
  - systems
  - programming
  - notes
  - python
  - torch
---
DataLoader vs Dataset: 
* Dataset: stores samples + labels
* DataLoader: like an iterable Dataset, provides easy access to samples.

I think it's worthwhile to look at built-in datasets to see how they are structured. 

A custom _Dataset_ must have a constructor, `__len__` and `__getitem__`. Constructors don't need to call `super()`.  `__getitem__` returns a sample/label pair, i.e `X,y`.

A custom _DataLoader_ is like a dataset that is mini-batch aware. It assists in data reshuffling and parallelizing data access. IMO, much of this should be managed in Xarray via xbatcher, when possible. DataLoaders are iterable, and thus, often called with `next(iter(train_loader))`.

DataLoaders should be compatible with Torch's _Samplers_.

A DataLoader is invoked in train scripts like so:
```python
def train(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    model.train
	### Note the iteration pattern! ###
    for batch, (X, y) in enumerate(dataloader):
        X, y = X.to(device), y.to(device)

        # Compute prediction error
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), (batch + 1) * len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")
```


A convention for data loaders is to couple them with _transforms_. `transform` and `target_transform` modify the data and label, respectively. I wonder if `xbatcher` has specific affordances for these s.t. we can write stuff in Xarray's fluent API before converting the underlying numpy arrays to torch Tensors?

There are two Dataset types made available to DataLoaders:
* map-style, which is described above (`__getitem__` and `__len__`).
* iterable-style, which are subclasses of `IterableDataset`. This is used when random reads are expensive or improbable, where batch size depends on the fetched data.

When using `IterableDataset`, which is more like the Xarray case, replicates of the loader are typically made across multiple processes. Thus, the data needs to be configured well to avoid duplicate data loading. 

Iterable style datasets naturally lend themselves to chunking where a batch is yielded all at once. 

Instead of using the shuffle flag in map-style data loaders, users can specify custom Samplers. These yield the next index/key to fetch. Samples can also be used to configure batches via the `batch_sampler` arg.

Sampler cannot be used with iterable-style datasets.

By default, loaded data is collated into batches. A batch dimension is added as the first dimension. This is configurable if you want to get single samples or manage this yourself. 
I believe the collate_fn converts numpy arrays to torch tensors, and most of the time adds a batch dimension.

According to [this GH issue](https://github.com/pytorch/pytorch/issues/13246#issuecomment-905703662), one shouldn't use dicts and lists inside a `__getitem__` call, but instead use numpy arrays or similar, in order to avoid memory exploding from copy-on-write/refcounting behavior in python multiprocessing.

CUDA Tensors should not be used in mulit-processing; Automatic memory pinning is faster.

## To Pin or Not Pin Memory in Data Loaders?

> For data loading, passing `pin_memory=True` to a [`DataLoader`](https://pytorch.org/docs/stable/data.html#torch.utils.data.DataLoader "torch.utils.data.DataLoader") will automatically put the fetched data Tensors in pinned memory, and thus enables faster data transfer to CUDA-enabled GPUs.

– memory pinning | data API [^red]

> In this example, we are transferring many large tensors from the CPU to the GPU. This scenario is ideal for utilizing multithreaded `pin_memory()`, which can significantly enhance performance. However, if the tensors are small, the overhead associated with multithreading may outweigh the benefits. Similarly, if there are only a few tensors, the advantages of pinning tensors on separate threads become limited.

See references for the full article[^blue], it's a complex topic. 

---
# References
* https://pytorch.org/tutorials/beginner/basics/data_tutorial.html
* https://pytorch.org/tutorials/beginner/basics/quickstart_tutorial.html
* https://pytorch.org/docs/stable/data.html

[^blue]:  https://pytorch.org/tutorials/intermediate/pinmem_nonblock.html#additional-considerations
[^red]: https://pytorch.org/docs/stable/data.html#memory-pinning