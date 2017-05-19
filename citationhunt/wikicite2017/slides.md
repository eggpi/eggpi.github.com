<!-- pandoc -i slides.md -t revealjs -s -o slides.html -V theme:white --!>

<a href="https://tools.wmflabs.org/citationhunt" data-preview-link>Always start with a demo.</a>

---

\#1lib1ref

---

“We need more **simple, gamified** but substantive models for contributing to
Wikipedia. **Citation Hunt was an excellent tool for engaging librarians**, and
we have received feedback from librarians that the small action made the biggest
difference for their participation.”

<span style="font-size: small">[https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons](https://meta.wikimedia.org/wiki/The_Wikipedia_Library/1Lib1Ref/Lessons)</span>

---

Some English numbers:

- Typical day: 5-10 citations, ~500 snippets viewed
- \#1lib1ref 2017: 50-70 citations/day, for 3 weeks!

<span style="font-size: small">[https://tools.wmflabs.org/citationhunt/en/stats.html](https://tools.wmflabs.org/citationhunt/en/stats.html)</span>

---

Technical notes

---

Data extraction:

- Snippets or full sections marked with a template

- HTML output, annotated with custom CSS classes

---

Other (reusable?) goodies:

- Lightweight MediaWiki API library
    - POST for large requests
    - Persistent connection support

- Client-side autocomplete based on [Awesomplete](https://github.com/LeaVerou/awesomplete)

---

Future direction

---

- More languages

- Improve detection of fixed snippets ([#70](https://github.com/eggpi/citationhunt/issues/70))

- UI glitches ([#73](https://github.com/eggpi/citationhunt/issues/73))

- Generalize to other kinds of templates and backlog

---

[tools.wmflabs.org/citationhunt](https://tools.wmlabs.org/citationhunt)

[ggp.name/citationhunt/wikicite2017/slides.html](http://ggp.name/citationhunt/google/slides.html)

[github.com/eggpi/citationhunt](https://github.com/eggpi/citationhunt)
