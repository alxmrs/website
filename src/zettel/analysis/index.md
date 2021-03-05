# Abstract Interpretation
_Notes from Cousot & Cousat, 77'_

_started: 2021-03-04_
```
@inproceedings{10.1145/512950.512973,
    author = {Cousot, Patrick and Cousot, Radhia},
    title = {Abstract Interpretation: A Unified Lattice Model for Static Analysis of Programs by Construction or Approximation of Fixpoints},
    year = {1977},
    isbn = {9781450373500},
    publisher = {Association for Computing Machinery},
    address = {New York, NY, USA},
    url = {https://doi.org/10.1145/512950.512973},
    doi = {10.1145/512950.512973},
    abstract = {A program denotes computations in some universe of objects. Abstract interpretation of programs consists in using that denotation to describe computations in another universe of abstract objects, so that the results of abstract execution give some information on the actual computations. An intuitive example (which we borrow from Sintzoff [72]) is the rule of signs. The text -1515 * 17 may be understood to denote computations on the abstract universe {(+), (-), (±)} where the semantics of arithmetic operators is defined by the rule of signs. The abstract execution -1515 * 17 → -(+) * (+) → (-) * (+) → (-), proves that -1515 * 17 is a negative number. Abstract interpretation is concerned by a particular underlying structure of the usual universe of computations (the sign, in our example). It gives a summary of some facets of the actual executions of a program. In general this summary is simple to obtain but inaccurate (e.g. -1515 + 17 → -(+) + (+) → (-) + (+) → (±)). Despite its fundamentally incomplete results abstract interpretation allows the programmer or the compiler to answer questions which do not need full knowledge of program executions or which tolerate an imprecise answer, (e.g. partial correctness proofs of programs ignoring the termination problems, type checking, program optimizations which are not carried in the absence of certainty about their feasibility, …).},
    booktitle = {Proceedings of the 4th ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages},
    pages = {238–252},
    numpages = {15},
    location = {Los Angeles, California},
    series = {POPL '77}
}
```

Abstract interpretation of programs is, in my own works, a means of reasoning  
about abstract properties of a program. A program contains, let's say, high 
dimensions of data. In AI, we may project this representation down to a single 
quality so that we can reason about this quality. 

For example, we may project the calculation `-1515 * 17` onto the dimension of
"signs". In this world, we do not know about numbers, we only know about three 
things: `{(-), (+), (+/-)}`. Thus, the abstract view of this equation is 
`(-) * (+) => (-)`. Sometimes, in this view, we cannot fully determine a result,
which we could if we had all the information of the concrete case. Take 
`-1515 + 17`: `(-) + (+) => (+/-)`.

> Abstract interpretation allows the programmer or the compiler to answer 
> questions which do not need full knowledge of the program execution or which 
> tolerate an imprecise answer

Abstract program properties can be modelled by a 
[complete semilattice](/zettel/analysis/semilattice/complete/).

## Syntax & Semantics of Programs

The paper describes a way of breaking down a program into Nodes.

Each node in a program has  successor and predecessor nodes. Nodes are broken up
into subsets (type of node): Entries, Assignments, Tests, Junctions, and Exists.

* `Entries`: have no predecessors and have one successor.
* `Assigment`: has one predecessor and one successor. These are broken up into 
 two subtypes (subsets): 
  * `Ident`: identifiers
  * `Expr`: expressions
