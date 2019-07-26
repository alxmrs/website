# Ideas for Posts/Projects

## 2019-07-12 Structure site to abuse Jekyll
I just realized that you don't need Jekyll to host githubpages sites. I can just write static assets and serve them. 
I think there are some niceities to Jekyll. Well, the only one I can think of is a markdown --> HTML conversion. 

I think What I'll do is try to keep that aspect of it and disreguard all the rest. 

The benefit of using strait HTML is that I get a better dev cycle. I know exactly what the output can look like without
installing anything. Maybe that's an argument to get rid of jekyll to begin with and just generate the static assets.

Here's one option: Create a new repo that generates static assets, create a CICD rule that deploys the built files 
to this repo. 

If I was *really* cool, I would write the static website generator code in Rust or Kotlin, and compile it to WASM `:)`.

Yeah. I think that's what I'll do. 

## 2019-07-10 Advice for undergraduates that emailed me.
So far, I've been cold emailed by not one, but two (!) undergraduates from UCSD. Look, Ma, I'm famous!

They've written to me asking for advice, generally in the pattern of "I'm at A, how do I get to B"? 
I have already written an email to the first one, but have not had the time to respond to the second (it came today). 

After I email / chat this latest solicitor, I think I'll clean up and publish the posts for all to read. 

## 2019-04-14 Algebra Book Exercise:
Based on Printer's Algebra, pg 29, exercise C:
Write a program that uses a unit tests approach to test if "operations" have certain qualities. The ones listed are communativity, associativity, identity, and invertability.
The first set of operators are all the ops in a 2-valued set (should be 16 possible combinations). 

Next step: Adapt the code s.t. it works on more than 2 valued sets. 
Better still: Adapt the code s.t. it works on arbitrary operators. 

