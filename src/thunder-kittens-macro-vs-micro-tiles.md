---
title: Thunder Kittens & Macro vs Micro Tiles
date: 2025-01-15T10:17
description-meta: Does a chunk by any other name still burr as sweet?
status: 
tags:
---
A product of the [hazy-research-and-flash-attention](hazy-research-and-flash-attention.md) lab is [ThunderKittens](https://github.com/HazyResearch/ThunderKittens). In their README, they write (emphasis mine): 

> ThunderKittens is built from the hardware up -- we do what the silicon tells us. And modern GPUs tell us that they want to work with fairly small tiles of data. A GPU is not really a 1000x1000 matrix multiply machine (even if it is often used as such); it’s a manycore processor where each core can efficiently run ~16x16 matrix multiplies. **Consequently, ThunderKittens is built around manipulating tiles of data no smaller than 16x16 values.**

This reminds me a lot of this issue I filed in Cubed comparing Triton tiles and Zarr chunks: https://github.com/cubed-dev/cubed/issues/490

![Macro vs Micro tiles in ](https://private-user-images.githubusercontent.com/2322439/342781480-044981cc-5d8f-47a6-8fe4-96505b4139ae.jpeg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzY5NjU1NDUsIm5iZiI6MTczNjk2NTI0NSwicGF0aCI6Ii8yMzIyNDM5LzM0Mjc4MTQ4MC0wNDQ5ODFjYy01ZDhmLTQ3YTYtOGZlNC05NjUwNWI0MTM5YWUuanBlZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTAxMTUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwMTE1VDE4MjA0NVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM5NTk1ZTJiNDY1OWZmNDI2NzE1OTE4N2E3ZThhNWZkMWRjODQ1YzI4ZjBkMmYzOWM2ZTA4YjdlNmUwMjA4MDImWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.tuTKZgQW5ubbM80j0bg0YX8VLePLu7L1sC-vaFkP-8g)
---
# References
- [gpus-go-brrr](gpus-go-brrr.md)

