---
layout: default
title: Skiplists
tags: [skiplists, algorithms]
---

As part of a class on probabilistic algorithms I recently took, I prepared a [presentation](/blog_includes/skiplist-presentation.pdf) on a probabilistic data structure called Skiplist, first introduced in a 1989 paper entitled [Skip Lists: A Probabilistic Alternative to Balanced Binary Trees](ftp://ftp.cs.umd.edu/pub/skipLists/skiplists.pdf). Skiplists are a very simple data structure that builds upon linked lists and nondeterministic behavior to achieve insertion, deletion and search operations in O(log n) expected time, with high probability.

<!-- RSS summary end -->

Interestingly, as author William Pugh himself puts it towards the end of the paper,

> From a theoretical point of view, there is no need for skip lists. Balanced trees can do everything that can be done with skip lists and have good worst-case time bounds (unlike skip
> lists). However, implementing balanced trees is an exacting task and as a result balanced tree algorithms are rarely implemented except as part of a programming assignment in a data
> structures class.

Which means skiplists have the same big advantage over balanced binary trees as many other probabilistic algorithms and data structures have over deterministic alternatives: simplicity. Having implemented a balanced binary tree a long time ago, I know that things can get very messy, very quickly; in a way, probabilistic algorithms pose a new tradeoff -- worst-case performance for developer time -- which is definitely desirable if you need to roll your own implementation for whatever reason.

This is what a skiplist looks like:

<div class="img-wrap standout">
    <img alt="A complete skiplist" src="/img/skiplist.png" title="A complete skiplist" />
    <label class="img-caption">-- A complete skiplist, taken from the original paper</label>
</div>

Basically, the data structure consists of a few sorted linked lists, stacked on top of one another, where each element always belongs to the bottom list (the one at level 0), and given that it belongs to the i-th level, it will also belong to the i+1-th level with some probability p, usually 0.5. In addition to that, all we need is a header node that points to the beginning of the list at each level, and a sentinel node at the end.

Searching a skiplist is not too different from searching a linked list; in fact, all we need to do is start searching in the list at the top level, and whenever we find an element larger than the one we're looking for, descend to the level below. Inserting consists of a search to determine where the new element should be placed in each list (remember, the lists are sorted), then drawing the node's random height (that is, the number of linked lists it participates in) from a geometric distribution with parameter 1-p. Removals also follow directly from the linked list algorithm, and if we're a little bit clever with these algorithms, it can be proven that they take O(log n) time on a skiplist of n elements, with high probability.

The explanation above is, of course, not nearly enough to really understand what skiplists are all about. If this sounds interesting, I recommend reading both the original paper and [my presentation](/blog_includes/skiplist-presentation.pdf), which contains a derivation of skiplists from linked lists, the proof for the O(log n) bound, and a sample implementation of the search and insertion algorithms in Python.
