---
title: Random ideas to solve Alex's Anniversary Paradox
date: 2022-06-16
---

_WIP?_

I've been thinking a bunch about how to tackle [this problem](https://alxmrs.com/anniversary/). It seems like my trip
to the barber shop seems like a weird variant of the [Birthday Paradox](https://en.wikipedia.org/wiki/Birthday_problem):
What is the probability, in a group of `n` randomly chosen people, at least three will have the same name and wedding
day?

I've poked around stats exchange and found some [general solutions](https://stats.stackexchange.com/a/1718) to the
birthday paradox, including an [R implementation](https://stats.stackexchange.com/a/335132). Though, I'm not convinced
that this is a good approach. How do you maintain assumptions and also account for names?

It seems like a better way would be to collect data on birthdays and wedding anniversaries, and calculate the
distribution. A project for another day...
