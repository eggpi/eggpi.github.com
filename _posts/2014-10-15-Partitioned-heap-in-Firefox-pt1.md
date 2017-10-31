---
layout: default
title: Partitioned heap in Firefox, part 1
tags: [mozilla, security, jemalloc]
---

This post is meant to share some of the progress I've made in my current project at Mozilla, which I've been working on for about two months now. In short, the goal of this project is to use heap partitioning as a countermeasure for attacks based on use-after-free bugs, and in what follows, I'll (briefly) go over what we're trying to guard against, then proceed to explain what we're planning to do about it.

<!-- RSS summary end -->

### Use-after-free bugs and how they're exploited

Having very little security experience prior to taking this project, the first thing I did was spend a few days understanding how use-after-free bugs are exploited. As it turns out, they're often an essential part of attacks against browsers, given how malicious Javascript code can get the browser engine to perform arbitrary allocations while being executed.

In particular, if any script gets a chance to run after an object is freed, but before it is (mistakenly) used again, then that script could attempt to allocate, say, an ArrayBuffer in that free'd memory region. In a simplistic scenario, if that allocation succeeds - and, with a deterministic memory allocator, chances are it will succeed -, an attacker could overwrite the free'd object's vtable to control the execution flow of the browser when a method of the compromised object is next invoked.

While studying this, I found this [description of a Firefox vulnerability found during Pwn2Own 2014](http://www.vupen.com/blog/20140520.Advanced_Exploitation_Firefox_UaF_Pwn2Own_2014.php) and this [write-up on a WebKit exploit](http://scarybeastsecurity.blogspot.com.br/2013/02/exploiting-64-bit-linux-like-boss.html) to be particularly useful. In the former, an ArrayBuffer is corrupted to leak some interesting memory addresses (thus bypassing [Address Space Layout Randomization](https://en.wikipedia.org/wiki/Address_space_layout_randomization)), which are then used to form a [ROP](https://cseweb.ucsd.edu/~hovav/dist/geometry.pdf) payload that is entered after a jump is made to an address kept in memory that is used after being free'd. In the latter, a truly mindblowing sequence of steps is employed to overwrite the vtable of a free'd then used object.

### Heap partitioning as a countermeasure

Attacks based on use-after-free bugs basically hinge on the predictability of the memory allocator: an attacker must be reasonably confident that triggering a memory allocation of the same size as a chunk of memory that was just free'd will cause the allocator to return that very same chunk.

Thus, an effective way to counter these attacks is to _partition_ the heap such that allocations that may be controlled by an attacker will never reuse memory that was previously allocated to internal browser objects. Specifically, Javascript objects that cause buffers to be allocated (and whose memory contents can be arbitrarily manipulated by an attacker), such as ArrayBuffers, should be allocated from an entirely separate memory pool than the rest of the browser engine.

This approach has been [implemented in other browsers](https://labs.mwrinfosecurity.com/blog/2014/06/20/isolated-heap-friends---object-allocation-hardening-in-web-browsers/) to various extents, and Gecko already does partition a restricted set of objects, in addition to poisoning freed memory to help catch use-after-free bugs. However, despite being [very effective](http://blog.fortinet.com/post/is-use-after-free-exploitation-dead-the-new-ie-memory-protector-will-tell-you), segregating entire classes of objects doesn't come at no cost: there's a very real risk of increasing memory fragmentation, and thus memory usage, which is something we've [extensively tweaked in the past](http://blog.pavlov.net/2008/03/11/firefox-3-memory-usage/) and care a lot about.

### A word on memory allocators

After studying the available options, we came up with two alternatives for implementing heap partitioning - tweaking the existing allocator, or replacing it with Blink's PartitionAlloc.

Firefox currently uses an allocator dubbed [mozjemalloc](http://dxr.mozilla.org/mozilla-central/source/memory/mozjemalloc/jemalloc.c?from=memory/mozjemalloc/jemalloc.c), a modified version of the jemalloc allocator. It is not too difficult to understand its inner workings by reading the code and stepping through some allocations with a debugger, but I also found a [Phrack article](http://www.phrack.org/issues/68/10.html#article) about jemalloc to be a valuable resource. As a bonus, the article is written from an attacker's perspective, which is good for "knowing-your-enemy" purposes.

While it is not too hard to tweak mozjemalloc so it uses different partitions, we're currently in the process of updating our allocator back to [unmodified jemalloc](https://bugzilla.mozilla.org/show_bug.cgi?id=762449) (aka jemalloc3), so it's more sensible to implement partitioning on top of jemalloc3 instead of mozjemalloc. Plus, jemalloc3 provides handy API calls that can be used for partitioning, which is less intrusive than what we'd need to do with mozjemalloc.

[PartitionAlloc](https://code.google.com/p/chromium/codesearch#chromium/src/third_party/WebKit/Source/wtf/PartitionAlloc.h) (PA for short), on the other hand, is built from the ground up with partitioning in mind, and while it will certainly cause a lot more integration woes than jemalloc3, it's definitely worth experimenting with. Given that it's an off-the-shelf solution for partitioning, I haven't bothered too much with understanding how it works yet, nor have I found any references about it aside from the code itself.

### Building up to the experiments

After taking in all that new information, it became apparent that there was a lot of work to be done in both fronts - jemalloc3 and PA -, up until the milestone where we'd get some data to compare them and pick the winner.

The JS engine folks advised me that the simplest way to get some experimental data for memory usage would be to not try to allocate specific objects in a separate partition, but rather to separate all engine allocations from the rest of the browser. Given that the buffers we're interested in isolating account for most of the memory used by SpiderMonkey, this would give us a good approximation of the final results without having to worry too much about their [hierarchy of memory functions](http://dxr.mozilla.org/mozilla-central/source/js/src/vm/MallocProvider.h?from=MallocProvider.h#7.)

Thus, I spent the following weeks attempting to create two builds: one in which SpiderMonkey allocates from a separate jemalloc3 partition from the rest of Gecko, and another in which it allocates from PA, with jemalloc3 being used for the rest of Gecko. The latter may sound odd (that's because it is), but it proved to be a lot easier than replacing the allocator for all of Gecko with PA, and I believe it is enough for comparison purposes. Additionally, I began working on the jemalloc3 transition by helping upstream some changes that had been made on mozjemalloc ([bug 801536](https://bugzil.la/801536).)

As an interesting aside, the PA builds unveiled several violations of the JS engine API in which the memory allocators used by Gecko and SpiderMonkey were mixed (for instance, attempting to free from one of them memory that was allocated from the other), all over the code. [I](https://bugzil.la/1078451) [fixed](https://bugzil.la/1071998) [all](https://bugzil.la/1071996) [that](https://bugzil.la/1071993) [I](https://bugzil.la/1071976) [could](https://bugzil.la/1082547) [find](https://bugzil.la/1071967.)

### Experiments

We have a great tool for measuring Firefox's memory footprint under realistic loads called [Are We Slim Yet?](https://areweslimyet.com), which I'll refer to as AWSY for brevity. Once the necessary builds were ready, the next step was to run them through AWSY and see how they performed.

<div class="img-wrap standout" style="width: 90%">
    <img style="width: 100%" alt="AWSY results" src="/img/awsy-sm-partitions3.png" title="AWSY results" />
    <label class="img-caption">-- Columns, left to right: jemalloc3 with partition, mozjemalloc, jemalloc3 without partition, PartitionAlloc + jemalloc3 Frankenbuild</label>
</div>

The graph above shows RSS, the main metric we're interested in - the amount of physical memory used by Firefox - in four different builds. From left to right: [jemalloc3 with a separate partition for SpiderMonkey](https://tbpl.mozilla.org/?tree=Try&rev=5b12055c00ed), [an unmodified build using mozjemalloc](https://tbpl.mozilla.org/?tree=Try&rev=696668013ff4), [jemalloc3 without a separate partition](https://tbpl.mozilla.org/?tree=Try&rev=5810e3365b9d), and [jemalloc3 with PartitionAlloc for SpiderMonkey](https://tbpl.mozilla.org/?tree=Try&rev=d6d5b9d5921e) . The [complete AWSY run](https://areweslimyet.com/?series=sm-partitions3&evenspacing) has all the results, but it also shows pretty obviously that the in-browser memory accounting is broken with PartitionAlloc, so it's best to constrain our analysis to RSS.

### Conclusions and next steps

Despite the iffiness of the jemalloc3 + PartitionAlloc Frankenbuild, the experimental evidence shows that:

1. There's no reason to expect PartitionAlloc's memory footprint to be much better than jemalloc3's
2. Partitioning jemalloc3 should introduce little additional memory overhead
3. jemalloc3 regresses significantly when compared with mozjemalloc

Given the difficulty in integrating PartitionAlloc and conclusion 1 above, the takeaway is that the best way forward is to give up on PartitionAlloc for now and invest in jemalloc3, which we're more than halfway through in transitioning to anyway. Of course, should our jemalloc3 solution prove insufficient for any reason, we now also have evidence that PartitionAlloc is a worthy contender in the future.

Conclusion 2 gives us some confidence that going with jemalloc3 will not cause Firefox's memory usage to skyrocket, but point 3, for which there is a [known bug](https://bugzil.la/762448), is a bit more worrying, so I'll investigate that next.

### Acknowledgements

Special thanks to Daniel Veditz, Mike Hommey, Nicholas Nethercote, Terrence Cole, Steven Fink and John Schoenick for contributing to and guiding me through the various parts of these experiments.
