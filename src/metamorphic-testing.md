---
title: Metamorphic Testing
date: 2025-01-13T14:14
status: 
tags:
  - testing
  - formal-methods
  - programming
---
Property based testing is difficult because it's hard to find good properties. Metamorphic testing is a type of PBT under a "metamorphic relation". Here, we see if the outputs _all match_ when many of them have undergone automated mutation (that shouldn't but _could_ affect the output).

> For example, if a given soundclip transcibes to output `out`, then we should _still_ get output `out` if we:
>
>- Double the volume, or
>- Raise the pitch, or
>- Increase the tempo, or
>- Add some background static, or
>- Add some traffic noises, or
>- Do any combination of the above.

...
>We could, for example, download an episode of _This American Life_, run the transformations, and see if they all match.[1](https://www.hillelwayne.com/post/metamorphic-testing/#fn:tam) We have useful tests _without listening to the voice clip._ We can now generate complex, deep tests without the use of an oracle!

---
# References

https://www.hillelwayne.com/post/metamorphic-testing/
