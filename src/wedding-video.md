---
title: How I backed up all my wedding footage in the cloud
date: 2022-11-22
---

<iframe id="album" title="camille &amp;amp; alex // brick wedding highlight film // san diego, ca"
src="https://player.vimeo.com/video/759313365?h=b758ca6554&amp;dnt=1&amp;app_id=122963" width="960" height="409"
frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen=""></iframe>

My wife and I absolutely love our [wedding video](https://amariproductions.com/camille-alex/). I honestly can’t imagine
how it could have been any better. In addition to their excellent work, we
chose [Amari Productions](https://amariproductions.com/) as our videographers because they offered us the ability to get
all our wedding footage in raw. This really appealed to us since we think it would make a really great anniversary
present down the line to eventually produce a longer wedding movie. This presents us a problem — how do we download and
store all this video?

We face an immediate problem: Amari has sent us a Google Drive folder with the 100 or so gigabytes of raw files (zipped)
that will be deleted in about a few weeks. My wife and I are not at home at the moment, so it’s a bit impractical for us
to download all of this to a terabyte hard drive.

<aside>

💡 Aside: Apparently, hard
drives [expire](https://datarecovery.com/rd/ssd-lifespans-how-long-can-you-trust-your-solid-state-drive). This doesn’t
bode well if we want to keep something so precious indefinitely.

</aside>

A remote backup is definitely the right move. However, I am not quite ready yet
to [pay for that much Google Drive space](https://workspace.google.com/pricing.html) every year. Can I do better with
Google Cloud Storage?

Ideally, I want to solve for both 1) convenient data transfer and 2) cheap long-term storage.

# What’s this going to cost?

My approach was to set up a Google Cloud Storage bucket as cheaply as possible. (For the non-technical reader: A bucket
is like a folder in Drive.) I’ve estimating that it would cost me about $14 in the first year, given that I need to
transfer the data and I’ll probably want to download it once. This is cheap enough that I don’t really care to estimate
the exact annual cost thereafter, which will almost certainly be lower (maybe $7 a year).

I don’t expect to access the data that often, so the archival storage class seems good enough for me. I feel pretty
confident about GCP’s lack of data loss, so I only chose to host the data in a single data center.

[Wedding Footage Cloud Storage Cost Estimates](https://www.notion.so/68ac24431daf417d9b1a1c5de1416064)

## How did I back it all up?

I basically
followed [this article](https://philipplies.medium.com/transferring-data-from-google-drive-to-google-cloud-storage-using-google-colab-96e088a8c041)
’s approach for copying data between Google Drive and Google Cloud Storage. The steps for me looked like:

1. I “Added a Shortcut” from Amari’s shared folder to my personal drive. This was essential for the it to show up in my
   mounted drive later on.
2. I created a cloud bucket that suited my needs. I called it `gs://merose-wedding-video-raw`. I typically use long,
   verbose names like these since bucket names have to be globally unique.
3. I created a new Colab notebook and followed the steps mentioned in the article. After the setup, the actual transfer
   more or less amounted to a `gsutil` invocation.

Here’s the actual Colab that I used to make the transfer, if you’d like to do something similar yourself (remember to
change the Drive folder name and destination bucket).

[Google Colaboratory](https://colab.research.google.com/drive/11BtoMT2hf1b-rWCojZy5zNXfpaiC8kPO#scrollTo=eLxQNdSwXQBZ)

## Takeaways

I think I’ve met all my goals to have a convenient, cheap backup of my wedding videos. This whole process was incredibly
easy: With Colab, I didn’t have to install or set anything up. Writing this article probably took ten times as long as
it did to write the code. My favorite part: this basically amounts to renting a hard drive from Google, where they’re on
the hook for maintenance.