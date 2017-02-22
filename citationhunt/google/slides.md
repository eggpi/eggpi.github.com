<!-- pandoc -i slides.md -t revealjs -s -o slides.html -V theme:white --!>

<a href="https://tools.wmflabs.org/citationhunt" data-preview-link>Always start with a demo.</a>

---

How can I begin to edit Wikipedia?

---

[Manual of Style](https://en.wikipedia.org/wiki/WP:MANUAL) is 63 pages long!

. . .

[Fighting strangers on the Internet](https://en.wikipedia.org/wiki/Wikipedia:Lamest_edit_wars)

. . .

What to edit?

---

Easy, uncontroversial, but still **interesting**

Citations!<sup style="font-size: medium; color: #0645AD">[<span style="font-style: italic">citation needed</span>]</sup>

---

![](img/early.png)

---

Simple Python (Flask) app

Parsing [Wikipedia dumps](https://dumps.wikimedia.org/)

Hosted on [Heroku](https://heroku.com)

Client-side search over fixed categories ([awesomplete](https://github.com/LeaVerou/awesomplete))

---

Announced on the [Village Pump](https://en.wikipedia.org/wiki/Wikipedia:Village_pump)

_“I like the playfulness and concision of the tool. (...) Very different, new and unique”_

<span style="font-size: small">[https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(idea_lab)/Archive_16#CitationHunt](https://en.wikipedia.org/wiki/Wikipedia:Village_pump_(idea_lab)/Archive_16#CitationHunt)</span>

---

[https://tools.wmflabs.org/citationhunt](https://tools.wmflabs.org/citationhunt)

Moved to [Tool labs](https://wikitech.wikimedia.org/wiki/Help:Tool_Labs):

> - Hosting environment for tools and bots
> - Access to live database
> - Borg-like grid engine
> - Easy support for Flask tools

---

Overnight success!

. . .

<sup style="font-size: medium; color: #0645AD">[<span style="font-style: italic">citation needed</span>]</sup>

---

\#1lib1ref?

---

“As part of the **Wikipedia 15** birthday celebration (#Wikipedia15) in January 2016,
the Wikipedia Library team (@WikiLibrary) ran a **social media campaign** asking
librarians all over the world to **Imagine a World where Every Librarian Added
One More Reference to Wikipedia.** We called it **#1lib1ref.**”

<span style="font-size: small">[https://blog.wikimedia.org/2016/04/25/engaging-librarians-1lib1ref/](https://blog.wikimedia.org/2016/04/25/engaging-librarians-1lib1ref/)</span>

---

“The combination of [Citation Needed] templates and the Citation Hunt tool
created a really low participation threshold. (...) Moreover, these tools
**facilitate a behaviour common amongst librarians: chasing information in
reference materials** (this is a core part of reference librarian training).”

<span style="font-size: small">[https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons](https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons)</span>

---

“Did my civic duty and added some references for #1lib1ref. Also forgot how
**addictive** Citation Hunt tool was ;)”

<span style="font-size: small">[https://twitter.com/marykatwahl/status/825424325188608000](@marykatwahl)</span>

. . .

“(...) It’s like a **pokie machine for librarians**. DING dopamine hit.”

<span style="font-size: small">[https://twitter.com/HughRundle/status/688171119610744832](@HughRundle)</span>

. . .

“Finding citation hunt to be **oddly soothing**”

<span style="font-size: small">[https://twitter.com/luis_in_140/status/696053379970134017](@luis_in_140)</span>

---

“We need more **simple, gamified** but substantive models for contributing to
Wikipedia. **Citation Hunt was an excellent tool for engaging librarians**, and
we have received feedback from librarians that the small action made the biggest
difference for their participation.”

<span style="font-size: small">[https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons](https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons)</span>

---

Internationalization:

- [translatewiki.net](https://translatewiki.net) is amazing!
- French, Polish, Italian...

---

[2016 Hackathon in Jerusalem](https://www.mediawiki.org/wiki/Wikimedia_Hackathon_2016):

- Hebrew (and RTL!) support
- [WikiProject support](https://en.wikipedia.org/wiki/Wikipedia:WikiProject)

----

More users:

- [WikiEdu](https://wikiedu.org)

- Various editathons

- Wikipedia/Twitter/Facebook promotion

---

![](img/wikipedia_btn.png)

<span style="font-size: small">[https://en.wikipedia.org/wiki/Wikipedia:Citation_needed](https://en.wikipedia.org/wiki/Wikipedia:Citation_needed)</span>

![](img/wikipedia_btn2.png)

<span style="font-size: small">[https://es.wikipedia.org/wiki/Ayuda:Cómo_referenciar](https://es.wikipedia.org/wiki/Ayuda:Cómo_referenciar)</span>

---

More features:

- Usage graphs

- Server-side category search

- New theme: Vector button style

- Spanish, Czech, Swedish...

---

...but not Turkish

. . .

![](img/turkish.png)

<span style="font-size: small">[https://tools.wmflabs.org/superyetkin/kaynak_avcisi.php](https://tools.wmflabs.org/superyetkin/kaynak_avcisi.php)</span>

. . .

(yet!)

---

Technical review

---

<img class="plain" src="img/overview.svg" height="50%" />

---

<div style="font-family: monospace; font-size: medium; text-align: justify">
===Competitions===

In May 2004, the websites Dark Blue and SearchGuild teamed up to create what
they termed the "SEO Challenge" to Google bomb the phrase "[[nigritude
ultramarine]]".<ref>{{cite web|last=Karch|first=Marziah|title=Google Bombs
Explained|url=http://google.about.com/od/socialtoolsfromgoogle/a/googlebombatcl.htm|work=About.com|accessdate=2011-03-30}}</ref>

In September 2004, another [[SEO contest]] was created. This time, the objective
was to get the top result for the phrase "[[seraphim proudleduck]]". A large sum
of money was offered to the winner, but the competition turned out to be a
hoax.**{{Citation needed|date=March 2008}}**

In March 2005's issue of [[.net (magazine)|''.net'' magazine]] published, a
contest was created among five professional web developers to make their site
the number-one site for the made-up phrase "crystalline incandescence".
</div>

becomes...

. . .

<div style="font-family: monospace; font-size: medium; text-align: justify">
In September 2004, another SEO contest was created. This time, the objective
was to get the top result for the phrase "seraphim proudleduck". A large sum of
money was offered to the winner, but the competition turned out to be a
hoax.&lt;sup class="superscript"&gt;**[citation needed]**&lt;/sup&gt;
</div>

---

<div style="font-family: monospace; font-size: medium; text-align: justify">
Google Brain was initially established by Google Fellow [[Jeff Dean (computer
scientist)|Jeff Dean]] and visiting Stanford professor [[Andrew Ng]]**&lt;ref
name=ng-dean-blog&gt;**{{cite web|author1=Jeff Dean and Andrew Ng|title=Using
large-scale brain simulations for machine learning and
A.I.|url=http://googleblog.blogspot.com/2012/06/using-large-scale-brain-simulations-for.html|website=Official
Google Blog|accessdate=26 January 2015|date=26 June 2012}}&lt;/ref&gt; (Ng since moved
to lead the artificial intelligence group at [[Baidu]]**&lt;ref&gt;**{{cite
web|url=http://www.scmp.com/news/china/article/1519211/ex-google-brain-head-andrew-ng-lead-baidus-artificial-intelligence-drive|title=Ex-Google
Brain head Andrew Ng to lead Baidu's artificial intelligence
drive|publisher=[[South China Morning Post]]}}&lt;/ref&gt;). As of 2014, team members
included [[Jeff Dean (computer scientist)|Jeff Dean]], [[Geoffrey Hinton]],
[[Greg Corrado]], [[Quoc Le]],**&lt;ref&gt;**{{cite web|title=Quoc Le - Behind the
Scenes|url=http://www.technologyreview.com/emtech/14/video/watch/quoc-le-behind-the-scenes/|accessdate=20
April 2015}}&lt;/ref&gt; [[Ilya Sutskever]], [[Alex Krizhevsky]], [[Samy Bengio]], and
[[Vincent Vanhoucke]].**{{citation needed|date=January 2015}}**
</div>

becomes...

. . .

<div style="font-family: monospace; font-size: medium; text-align: justify">
Google Brain was initially established by Google Fellow Jeff Dean and visiting
Stanford professor Andrew Ng&lt;sup class="superscript"&gt;**[1]**&lt;/sup&gt; (Ng since moved
to lead the artificial intelligence group at Baidu&lt;sup class="superscript"&gt;**[2]**&lt;/sup&gt;).
As of 2014, team members included Jeff Dean, Geoffrey Hinton, Greg Corrado, Quoc Le,&lt;sup class="superscript"&gt;**[3]**&lt;/sup&gt; Ilya Sutskever,
Alex Krizhevsky, Samy Bengio, and Vincent Vanhoucke.&lt;sup class="superscript"&gt;**[citation needed]**&lt;/sup&gt;
</div>

---

The snippet parser

- Extract snippets or full sections

- HTML (Wikipedia API) or plain wikicode output

- Support for per-language template handling (yuck!)

- Powered by [mwparserfromhell](https://github.com/earwig/mwparserfromhell/) and
  a lot of hackery

---

Some English numbers:

> - Typical day: 5-10 citations, ~500 snippets viewed
> - \#1lib1ref 2017: 50-70 citations/day, for 3 weeks!
> - **Largest** referrer: en.wikipedia.org
> - **Best** referrer: wikiedu.org (anecdotally)

<span style="font-size: small">[https://tools.wmflabs.org/citationhunt/en/stats.html](https://tools.wmflabs.org/citationhunt/en/stats.html)</span>

---

Future direction

---

The immediate stuff:

- UX problems
    - Category search is hard to find and use [#24](https://github.com/eggpi/citationhunt/issues/24)
    - Text is not clear, too idiomatic [#71](https://github.com/eggpi/citationhunt/pull/71)

- More languages
    - Better support for plurals [#79](https://github.com/eggpi/citationhunt/issues/79)

- Better snippets [#81](https://github.com/eggpi/citationhunt/issues/81)

---

Longer term:

- Prevent [citogenesis](http://en.wikipedia.org/wiki/WP:CITOGENESIS)? Bad sources?

- More gamification mechanics?
    - \#1lib1ref 2017: Competition between libraries

- Campaigns on special dates throughout the year?

- Generalize to other kinds of templates and backlog

---

[citationhunt.org](http://citationhunt.org)

[github.com/eggpi/citationhunt](https://github.com/eggpi/citationhunt)
