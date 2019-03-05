---
layout: post
title: "Dockerfile for Streaming an RTSP into OpenCV with Anaconda"
date: 2017-12-04
---


## Problem

I was assigned a task at my new job to consume a video stream from an rtsp 
endpoint into OpenCV. This seemed straightforward initially, as SO posts and documentation
indicated that consuming rtsp video streams should be as simple as calling `cv2.VideoCapture('rtsp://...')`.
However, I found myself spinning my wheels, staring at a dead connection with no 
apparent cause. 

Apparently, one needs to ensure that OpenCV is compiled with `ffmpeg` or some backend to
handle streaming video. (Thanks, https://stackoverflow.com/a/43001630)

I did find [Valian's docker container](https://hub.docker.com/r/valian/docker-python-opencv-ffmpeg/) 
to be a good solution to the problem. I like how the py version and cuda support are 
configurable with tags. The missing piece that we needed was an anaconda managed 
python environment to be compatible with the rest of our workflow.


### Why double namespace? 

### Benefits of Anaconda
- Conda install is faster
- Have access to the anaconda cloud, which is better for scientific computing
- 

### Other approaches

Package demo with setup.py, pip install from github repo to Valian's docker container. 

## Solution

