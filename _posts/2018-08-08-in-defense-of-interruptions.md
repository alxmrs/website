---
layout: post
title: "In Defense of Interruptions during Software Development"
date: 2018-08-08
---

It's a troupe that interruptions are bad in software. Take the scene in "The Social Network", where the early Facebook
developers are "plugged in" and can't be even slightly interrupted.

Are they really the devil that they are made out to be? I don't think so. 

> "Organizations which design systems are constrained to produce designs which are copies of the communication structures of these organizations." 
- [M. Conway](https://en.wikipedia.org/wiki/Melvin_Conway).

Interruptions are inevitable if you are working in a team. Developers from other projects will have questions for you, 
the interns will need checking in and guidance, and your peers will want you to review their pull requests.  



















One engineering meeting, my boss Charles asked all of the engineers at my company if we should start a "traffic cone" 
system. This is where if we need to hunker down and focus on the task we're working on, we are not to be interrupted. 
The premise of this, he noted, was that software engineering requires less interruptions so we can get complicated logic
figured out. 

This system seemed problematic to me for a number of reasons. At the core, this reveals a flawed perspective about how 
software should be written. 

If a brief interruption displaces hours of momentum allocated towards solving a problem, it's a reflection of [an inability
to break down the problem][an inability to think modularly]. 

This impacts the developers process on two fronts. First, the programmer is incentivised to do top-down design of the system
they are building, even if informally. At one end of the spectrum, the developer can do document-driven development where
the plan out the communication between routines, classes, packages, and modules. On the other end of the spectrum, planning
is closer to the code: Stub out all of the classes, interfaces, and functions that you'll eventually need to have written. 
Take a particular set of routines, assume they are implemented (or will be, within a reasonable amount of time), and see
how they work together to solve the larger problem.  

The aim every developer should take when composing programs is to try to get to the next best
"stopping place." At this point, that module or function can then be tested for correctness. If you're playing a video game
that lets you arbitrarily save at any point, you're efforts are best spent getting as quickly to the next checkpoint and 
saving your progress rather than trying to complete the level in one go. Why not apply the same methodology to software? 
There's no reason not to tighten the rope when scaling a rock wall.

This implement-test/test-implement cycle is strengthened when you combine it with top-down design. 
 

I think that software engineers should embrace interruptions. 
