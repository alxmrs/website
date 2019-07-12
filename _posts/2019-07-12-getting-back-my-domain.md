---
layout: post
title: "Getting Back My Domain"
date: 2018-09-02
---

Well, here's a very meta story about this website and how I've grown since I started it. 

But first, I want to talk about an issue that may have bugged you like it's bugged me, and the annoying maze that I got 
myself in to fix it. 

Check out the URL of this domain. Is it secure? How do you know? Let me show you how *I* know it's not as of writing: 

[!I am not secure](_assets/alex-is-not-secure.png)

"How embarrassing. A software engineer who doesn't know how to set up HTTPS for his own personal site."

When I started this site in 2017, that was the case. At least, I was focused on getting something up and running quick, 
and snoozed on adding that feature. Like most software engineering, building things you don't know how to do is just a 
matter of Googling it and following directions. 

As time has gone on, I've kept snoozing on adding this feature, despite 
[learning how to implement it](https://github.blog/2018-05-01-github-pages-custom-domains-https/).
I've avoided addressing anything to do with my domain due to an completely-avoidable predicament that I got 
myself into all in the name of "security". Here I am today, writing support tickets to sort it all out.

<center>* * * </center>

When I was younger, I found this free Chrome extension that would provide me piece-of-mind while web-browsing. It was 
called MaskedMe, and the general idea was it helped you control spam and prevent hacking. It did this by generating a fake 
email address per website, and automatically forwarding all the emails to your real address. 

"Great!" I thought. "I can't be subject to a [password-reuse attack](https://xkcd.com/792/) if every email I use is different, right?"

It had services, totally for free, for replacing phone numbers and credit cards, so you never had to give up personal information. 
So I replace a lot of information an various accounts with generated emails, cellphone numbers, and credit cards. 

Sometime around the end of high school or early college, after adopting MaskMe, I thought to myself,
 "I should buy my personal domain before [another Alex Rosengarten](https://www.facebook.com/public/Alex-Rosengarten) beats me to it."

So I did. But I had the *brilliant* idea to make the account holding my domains as anonymous as possible. 
You know, just in case I wanted to buy *other* domains where I would *need* anonymity (spoiler: this never happened). 
I filled out my account information without my actual email, name, or phone number, but at least a real credit card.


Fast forward several years. 

I somehow get into my domain name service (namecheap) and wire up my domain to point to github pages. I set up a quick, 
custom jekyll blog, autopay for my domain every year, and never have to log into the domain name service for any reason. 

Fast forward, later still.

By around this time, I'm familiar with AWS and use that to buy other domains. For simplicity, it makes sense to transfer 
all my domains into one provider for simplicities sake, right? 
I start to log on to namecheap, which should be easy because I actually remember my username and password. 
I hit the next screen: 

[!MFA is masked](_assets/namecheap-mfa-masked.png)

Ok, not a problem, I'll just grab it the information from my ol' MaskedMe account. 

A google search gets me [here](https://www.abine.com/).

Apparently MaskMe has re-branded as Abine, offering two services: Blur (same services as MaskMe) and DeleteMe, a way to 
scrub your online footprint off the web.

"That's fine", I think. "They'll have all my account information in tact."

Spoiler: They didn't. 

Apparently, masked credit cards and phone numbers are now part of their **premium** services. 





I have not missed the great, dual irony of the situation: 
- I used a series of indirections to remain anonymous... to publicize myself via personal domain. 
- I took security measures... that made me far less secure.



I've learned this general pattern about how I use to (and sometimes, still) do things: I "greedily" generalized early. 
In other words, I deferred doing the simple thing in order to make my life easier in the long run, so much so that it made things more complicated in the long run. 
In better words: ["Premature optimization is the root of all eval"](https://en.wikiquote.org/wiki/Donald_Knuth#Computer_Programming_as_an_Art_(1974)).

So much of software engineering is pure computer science theory, yet a great deal of of it is craftsmanship. 
