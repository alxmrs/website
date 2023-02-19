---
title: Getting Back My Domain
---

_2019-07-23_

Well, here's a very meta story about this website and how I've grown since I started it. 

Let's talk about an issue that has bugged me for quite some time and the annoying maze I had to get out of to 
fix it. 

Check out the URL of this domain. Is it secure? How do you know? Let me show you how *I* know it's not, as of writing: 

![My site does not use HTTPS, and therefore is not secure](/assets/alex-is-not-secure.png "A URL bar with no HTTPS support")

"How embarrassing. A software engineer who doesn't know how to set up HTTPS for his own personal site."

When I started this site in 2017, that was the case. At least, I was focused on getting something up and running quickly, 
and snoozed on adding that feature. Like most of software engineering, building things outside of your current ability 
is just a matter of Googling it and following directions. 

As time has gone on, I've kept postponing this feature, despite 
[learning how to implement it](https://github.blog/2018-05-01-github-pages-custom-domains-https/).
I've avoided addressing anything to do with my domain due to a completely avoidable predicament that I got 
myself into all in the name of "security". Here I am today, writing support tickets to sort it all out.

* * * 

When I was younger, I found this free Chrome extension that would provide me piece-of-mind while web-browsing. It was 
called MaskedMe, and the general idea was it helped you control spam and prevent hacking. It did this by generating a 
fake email address per website, and automatically forwarding all the emails to your real address. 

"Great!" I thought. "I can't be subject to a [password-reuse attack](https://xkcd.com/792/) if every email I use is 
different, right?"

It had additional services, totally for free, for replacing phone numbers and credit cards, so you never had to give up 
personal information. So I replaced a lot of information on various accounts with generated emails, cell phone numbers, 
and credit cards. 

Sometime around the end of high school or early college, after adopting MaskMe, I thought to myself,
 "I should buy my personal domain before [another Alex Rosengarten](https://www.facebook.com/public/Alex-Rosengarten) 
beats me to it."

So I did. But I had the *brilliant* idea to make the account holding my domains as anonymous as possible. 
You know, just in case I wanted to buy *other* domains where I would *need* anonymity (spoiler: this never happened). 
I filled out my account information without my actual email, name, or phone number, but with a real credit card.


Fast forward several years. 

I somehow get into my domain name service (Namecheap) and wire up my domain to point to Github pages. I set up a quick, 
custom jekyll blog, autopay for my domain every year, and never have to log into the domain name service for any reason. 

Fast forward, later still.

I've gained maturity as a developer and know my way around cloud technologies (like GCP and AWS). I'm motivated to 
consolidate my tools on to one platform so I can build more advanced things. 
To this end, I attempt to log on to Namecheap, which should be easy because I actually remember my username and password. 
I enter those pieces of information. Then, I hit the next screen: 

![I have to wait on a text to a phone number I don't control](/assets/namecheap-mfa-masked.png
 "A MFA screen showing my MaskedMe phone number")

Ok. This is *annoying*, but not too big of a problem. I'll just log into my MaskedMe account, get the multi-factor 
authentication (MFA) code, and move along.

A Google search gets me [here](https://www.abine.com/): Apparently MaskMe has re-branded as Abine, offering two 
services: Blur (same services as MaskMe) and DeleteMe, a way to scrub your online footprint off the web.

"That's fine", I thought. "They'll have all my account information in tact."

Spoiler: They didn't. 

Apparently, masked credit cards and phone numbers have become part of their *premium* services. 

From here, I took several approaches to recover this proxy cell number. I filed a support ticket (longer wait for free 
customers). I called their support phone line (a dead end loop that tells you to email them). I even tried to sign up 
for premium -- for some reason, my attempts to upgrade failed every time (likely because my data was stale, they built 
their service around new customers instead of maintaining connections for old ones). 

Eventually, I got a hold of Abine support. They said that after a long enough period of inactivity, they deprecate text
message proxies. This means that there was no way that I could access the MFA number, and was likely permanently 
locked out of my Namescheap account. 

This sucked a lot. Not only was I unable to maintain, upgrade, or configure my domain, I risked losing it after my 
credit card expired and ceased payments. 

The next lever I had left to pull was contacting Namecheap support. In my first conversation with their live help chat 
service, I saw a glimmer of hope: Their customer service members could override MFA temporarily if I could prove 
ownership of the account. This glimmer was extinguished soon, however, when I learned that to identify me, they 
needed the phone number on the account.

With nothing left to do, I filed a ticket at their risk management team, hoping that they could help me. If that failed,
 my hail mary option was to modify the content of my website, proving that it was really me after all. 
 
A day later, they got back to me. Without the phone number, they could do nothing for me.

* * * 

I have not missed the great, dual irony of the situation: 

- I used a series of indirections to remain anonymous... to publicize myself on the internet. 
- The security measures I took... made me more vulnerable and less in control.

"Congratulations," [my partner](http://camille.merose.com) told me. "You played yourself."

Thanks, hun.


Over the next few days, I searched my email and other records for traces of that number with no success. I knew that 
this was a futile effort, but I did it anyway out of desperation. 

Then, I had an idea. When I originally created my account, I paid for extra services to make sure that any identifying 
data about the domain wouldn't be publicly listed. I decided to check that anyway, just in case. 

I ran a query via Whois.org --

"There it is!" I discovered.

Apparently, I had only paid for a year's worth of this service. It had expired long ago. But there it was, a phone 
number ending in `057`.

Soon after, I had another live chat with Namecheap customer support. Before I knew it, I bypassed the MFA.

* * * 

In my younger days, I had an unbalanced sense of trust. I had strong feelings towards protecting myself online, but no 
context to correctly model risk. At the time, I didn't know of the importance of certain choices -- like how [important 
HTTPS is for web browsing](https://doesmysiteneedhttps.com/). I also 
neglected to consider the longevity of other choices. I needed to ask myself, "how dependable are the tools I choose to 
rely on?" 

Further, this situation could have been avoided if I performed regular maintenance. The logic I practiced 
was akin to the idea that you can't fall victim to a phishing attack if you never check email. Or, it was always 
tomorrow Alex's problem. Now that I'm in a less turbulent time in my life, I can work on minimizing my digital footprint and tending to my virtual garden.

In addition to risk assessment and orderliness, this experience has been a great lesson in skepticism. Before, I 
thought I needed to be robust against human adversaries. As I've matured, it's clear that I need to be robust against 
human error.

