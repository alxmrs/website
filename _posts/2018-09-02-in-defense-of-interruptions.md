---
layout: post
title: "In Defense of Interruptions"
date: 2018-09-02
---

(Much needed update on 2019-07-12)

Many believe that the [global minimum number of interruptions](https://heeris.id.au/2013/this-is-why-you-shouldnt-interrupt-a-programmer/) 
is good for software development. I disagree. This is problematic for three reasons: First, interruptions are inevitable 
and often useful. Second, It assumes a mindset that promotes bad software development. Third, resistance to 
interruptions often indicates the ability to learn quickly. 


## "Interruption" Is A Slur For Collaboration
First, interruptions are inevitable. In typical agile shops, there are stand-ups, sprint-plannings, retrospectives, and 
other corporate meetings. Communication takes place on Slack, HipChat, and the like. To butcher Kurt Vonnegut, being 
anti-interruptions "is like being anti-glacier" (that's what Slaughter House Five was about -- Scrum. *Right?*).

But, are interruptions all bad? No!

In fact, in the cases listed here, they are merely the realities in working in a collaborative work environment
<sup id="a1">[1](#f1)</sup>. Can we not lend 15 minutes to perform a code review for a colleague? Should we skip 
answering a question from an intern because it would interrupt our current work? 

Even if meetings are a drag<sup id="a2">[2](#f2)</sup> and you don't have any of the aforementioned, would you permit being 
interrupted for a `P0` bug? Of course you would. 

I think we should celebrate interruptions rather than demonize them. Yes, retrospectives are valuable even though I 
haven't finished my current story. Of course I will teach you about mime types, rising sophomore intern, instead of just
using the term in context. Give me a minutes to finish what I'm typing<sup id="a3">[3](#f3)</sup>, but then *yes*, I'll 
review your PR. 


## Vilifying Interruptions Reveals an Inability to Modularize Programs

Dijkstra says that software is the art of managing complexity. Only in software do we have to deal with data from the 
bit to the peta- (or exbi-) byte level<sup id="a4">[4](#f4)</sup>.

From this perspective, if interruptions like the ones listed above derail you, it represents an inefficiency at managing 
complexity. Try instead to break down the problem into small subcomponents that can reasoned about. 

Certain paradigms of software tend to relieve the mental burden of the programmer and let them be less vulnerable to the
negative effects of interruptions: 

- **Type-Driven Development**: Simply using types reduces ~15% of all programming errors. Make the linter / compiler rule 
out classes of errors for free just by using types! Plus, typed code is basically self-documenting, making it easier to 
collaborate with team members and remember things post-interruption.  
- **Top-Down Development**: Start by designing your system at the highest level, documenting, commenting, and stubbing 
out code all the way down. If you go by the book<sup id="a6">[5](#f5)</sup>, this means design the architecture first,
then components within the architecture, then class diagrams within each component, and then the functions within each 
class. In general, a particular implementation comes last -- at every step, you're writing stubs of classes and 
routines in order to perfect the interfaces of your application. Each level of the hierarchy is reduced to a manageable 
amount of complexity. You don't need to fit long branches of the tree into your working memory, just guarantee that 
the node plays well with it's parent, and delegate dealing with the children until later. 
- **Favor Composition**: Composition is a great pattern that's both functional and object-oriented. In OOP, it's often 
seen as the "has-a" relationship. The [Factory Pattern](https://en.wikipedia.org/wiki/Factory_method_pattern) and [Dependency Injection Pattern](https://en.wikipedia.org/wiki/Dependency_inversion_principle) are great examples of the great 
successes of composition. Within functional languages, composition is often expressed through [higher-order functions](https://en.wikipedia.org/wiki/Higher-order_function).
The concept of the higher order function has certainly [helped me a lot in my own programming work](http://alexrosengarten.com/blog/2018/07/06/higher-order-functions-on-pandas-dataframes).
Either way, the purpose of composition is often to isolate the logic you're trying to express while delegating the 
details of it for later (e.g. for a particular implementation).

If some or all of these approaches are employed, then the current state of the program is all the context that is 
needed to get back your train of thought. 


## Robustness to Interruptions is Comorbid with Rapid Adaptation

Writing code is half of software. The other half is reading it. A totally valid skill worth fine-tuning is the ability 
to understand *just* enough of a thing and intentionally ignore the rest. 

If you've just started a project, or joined a team with a small codebase, it's reasonable to expect that you can 
understand it all before contributing to it. This is quite often not the situation developers find themselves in: 
Most companies and teams maintain legacy systems that can be millions of lines of code. Not all of these codebases 
follow best practices and design. It's up to the developer to be able to quickly navigate unexplored territory, 
diagnose the situation, and contribute a fix. 




<b id="f1">1</b>. Lone Wolf Programmers (noun): extinct or mythical-beasts. [↩](#a1)

<b id="f2">2</b>. I like the advice of setting agendas *before* meetings and ending early when possible. [↩](#a2)

<b id="f3">3</b>. I hope you gathered by context that I'm not taking "interruptions" to their semantic extreme. [↩](#a3)

<b id="f4">4</b>. ![See alt text](../_assets/Code-Complete-Ch-5-Complexity.png "Managing complexity is the most important technical topic in software development. In my view, it’s so important that Software’s Primary Technical Imperative has to be managing complexity.    Complexity is not a new feature of software development. Computing pioneer Edsger Dijkstra pointed out that computing is the only profession in which a single mind is obliged to span the distance from a bit to a few hundred megabytes, a ratio of 1 to 10^9, or nine orders of magnitude (Dijkstra 1989).     This gigantic ratio is staggering. Dijkstra put it this way: “Compared to that number of semantic levels, the average mathematical theory is almost flat. By evoking the need for deep conceptual hierarchies, the automatic computer confronts us with a radically new intellectual challenge that has no precedent in our history.” Of course software has become even more complex since 1989, and Dijkstra’s ratio of 1 to 10^9 could easily be more like 1 to 10^15 today. "). [↩](#a4)

<b id="f5">5</b>. [See Chapter 5.2/pg 82](http://aroma.vn/web/wp-content/uploads/2016/11/code-complete-2nd-edition-v413hav.pdf). [↩](#a5)


