---
layout: default
title: CitationHunt
tags: [wikipedia, citationhunt, citation-needed]
---

As with most people who were students at some point over the past decade, I use Wikipedia quite heavily: it's simply the best source for getting an overview of a new topic and finding a trail of references for in-depth study. It's a project I truly believe in and to which I've always wanted to give something back.

In addition to that, I've become increasingly interested lately in the process of welcoming and mentoring newcomers in open source communities. I began to think that, while it would be nice to turn myself into a Wikipedia editor, it would be great if I could also produce some sort of tool for simplifying the daunting task of making the first few edits.

So I built [CitationHunt](https://tools.wmflabs.org/citationhunt).

<!-- RSS summary end -->

## The idea

[CitationHunt](https://tools.wmflabs.org/citationhunt) is a minimalistic tool for browsing unsourced statements -- those marked with the [iconic](http://knowyourmeme.com/memes/citation-needed) "[citation needed]" superscript -- in the English Wikipedia.

My thought process in coming up with it went something like this: as a wannabe editor, I asked myself what was getting in the way of my contributing. Three main factors came to mind:

1. The Wikipedia [manual of style](https://en.wikipedia.org/wiki/Wikipedia:Manual_of_Style) is hefty and intimidating;
2. I didn't want to accidentally get involved in a [lame edit war](https://en.wikipedia.org/wiki/Wikipedia:Lamest_edit_wars);
3. I didn't quite know how to find articles and sections in need of editing.

I tried to think of a class of edits that would be at the same time easy to perform and uncontroversial, but still interesting, and adding citations seemed like a good fit. The remaining problem was, of course, to facilitate the search for article snippets lacking citations, and that's the problem I sought to address.

To keept it from being overwhelming, CitationHunt had to be simple, even to the detriment of the feature set, and minimalistic in appearance. The user experience was inspired by the swipe right/swipe left mechanics of the [Tinder](http://www.gotinder.com/) dating app. The most technically challenging part of this project is the correct and reliable parsing of [Wikipedia dumps](https://dumps.wikimedia.org/), but thankfully none of its complexity made its way into the web interface.

I hosted a first working version on Heroku and used it to fill in a few references. The [first I ever did](https://en.wikipedia.org/w/index.php?title=1_Night_in_Paris&diff=prev&oldid=648055729) was on the article about Paris Hilton's sex tape, something I'm equally proud and embarrassed about. This early dogfooding was fundamental in assuring me there was some value in what I was doing, if only for my own use.

I then introduced CitationHunt to the community on the [Village Pump](https://en.wikipedia.org/wiki/Wikipedia:Village_pump_%28idea_lab%29/Archive_16#CitationHunt) page, where it was quite well received. Other Wikipedians were quick to inform me that the Wikimedia Foundation is kind enough to provide [hosting](https://tools.wmflabs.org/) for tools like mine, and I immediately moved CitationHunt to their infrastructure.

## Lessons learned

This project has taught me a few interesting lessons:

_Adding citations can be super easy, but also super hard_: Many unsourced statements reflect the source nearly verbatim. Anyone with basic search engine skills can easily fill them up. On the other hand, if you can find the decades-old pamphlet in which hardcore singer H.R. is described as "James Brown gone berserk" (one of the snippets in CitationHunt), I'll be immensely impressed.

_Serendipity happens_: Just as I was looking for an autocomplete library that didn't depend on JQuery, [Ilya Grigorik tweeted](https://twitter.com/igrigorik/status/570350118416699393) about [Awesomplete](https://github.com/LeaVerou/awesomplete), which is pretty great. Speaking of him, CitationHunt incorporates quite a few tricks from his book [High Performance Browser Networking](http://www.amazon.com/High-Performance-Browser-Networking-performance/dp/1449344763/).

_Parsing Wikipedia dumps is hard_: It's a lot of data, and few parsers properly support templates. Several snippets appear broken because of that. I'm sorry.

_Speed is a feature_: Not really a new lesson, but the only way I could support the streamlined experience I wanted for CitationHunt was for it to be very fast. This motivates the use of aggressive caching, prefetching and the move away from sqlite to MySQL on the server.

## Conclusion

CitationHunt has been pretty useful to me, and I've made several edits through it since its launch. If you made it this far in the post, do consider [trying it out](https://tools.wmflabs.org/citationhunt) and letting me know what you think!
