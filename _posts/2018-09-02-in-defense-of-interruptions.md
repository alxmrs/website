---
layout: post
title: "In Defense of Interruptions"
date: 2018-09-02
---

Many believe that minimizing interruptions is good for software development. I disagree, focusing on reducing 
interruptions is problematic for two reasons: 1) Interruptions are inevitable and often useful. 2) It assumes a mindset
that promotes bad software development.  

## "Interruption" Is A Slur For Collaboration
First, interruptions are inevitable. In typical Agile shops, there are stand-ups, sprint plannings, retrospectives, and 
other corporate meetings. Communication takes place on Slack, HipChat, and the like. To butcher Kurt Vonnegut, being 
anti-interruptions "is like being anti-glacier" (that's what Slaughter House Five was about -- Scrum. Right?).

But, are interruptions all bad? No!

In fact, in the cases listed here, they are merely the realities in working in a collaborative work environment
<sup id="a1">[1](#f1)</sup>. Can we not lend 15 minutes to perform a code review for a colleague? Should we skip 
answering a question from an intern because it would interrupt our current work? 

Even if meetings are a drag<sup id="a2">[2](#f2)</sup> and you don't have any of the aforementioned, would you permit being 
interrupted for a `P0` bug? Of course you would. 

I think we should celebrate interruptions rather than demonize them. Yes, retrospectives are valuable even though I 
haven't finished my current story. Of course I will teach you about mime types, rising sophomore intern, instead of just
using the term in context. Give me a minutes to finish what I'm typing<sup id="a3">[3](#f3)</sup>, but then yes, I'll 
review your PR. 

## Vilifying Interruptions Reveals an Inability to Modularize Programs

In the book Code Complete, Steven McConnel writes that software is the art of managing complexity. Only in software do 
we have to deal with data from the bit to the peta- (or exbi-) byte level<sup id="a4">[4](#f4)</sup>.

From this perspective, if interruptions like the ones listed above derails you, it represents an inefficiency at managing 
complexity. A means to the end of managing complexity is to break down the problem at hand such that it can be easily 
reasoned about (in order to produce correct, performant programs).  

Certain paradigms of software tend to relieve the mental burden of the programmer and let them be less vulnerable to the
negative effects of interruptions. There's a whole spectrum of type-driven development: Simply using types
reduces ~15% of all programming errors. This is not to mention the benefits of using a type system to delegate program
correctness to the compiler<sup id="a5">[5](#f5)</sup>. 

Many paradigms advocate for top-down design approaches<sup id="a6">[6](#f6)</sup>. Try stubbing out functions, then 
composing them together instead of writing a program linearly. Make use of higher-order functions. Program to an 
Abstract Data Type (interfaces). Try out document-driven development. In sum, use abstraction to work smarter. 

This family of approaches readily lends itself to Test Driven Development (TDD). If you can break down a problem into 
isolated sub-parts, then you can take time to test each sub-component for correctness before moving on to the rest. Then, 
you gain future time-saving efficiencies by having a base level of tests by the time you're ready to submit your feature.


<b id="f1">1</b>. Lone Wolf Programmers (noun): extinct or mythical-beasts. [↩](#a1)
<b id="f2">2</b>. I like the advice of setting agendas *before* meetings and ending early when possible. [↩](#a2)
<b id="f3">3</b>. I hope you gathered by context that I'm not taking "interruptions" to their symantic extreme. [↩](#a3)
<b id="f4">4</b>. See [here](/_assets/Code-Complete-Ch-5-Complexity.png). [↩](#a4)
<b id="f5">5</b>. Or interpreter/linter. [↩](#a5)
<b id="f6">5</b>. In my experience, life is better when you [go by the book](http://aroma.vn/web/wp-content/uploads/2016/11/code-complete-2nd-edition-v413hav.pdf) (see chapter 5.2/pg 82). [↩](#a6)

