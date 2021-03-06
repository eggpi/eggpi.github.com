---
layout: default
title: Partitioned heap in Firefox, part 2
tags: [mozilla, security, jemalloc]
---

It's been a few months since my first [post on implementing heap partitioning in Gecko](http://guilherme-pg.com/2014/10/15/Partitioned-heap-in-Firefox-pt1.html), and we've reached another milestone since then. In the previous update, I talked about how we chose to implement heap partitioning on top of jemalloc3 instead of PartitionAlloc, and how we still needed to address some of jemalloc3's rough edges to make it a suitable replacement for mozjemalloc.

This post is about how we finally made the switch to jemalloc3 on Nightly, which turned out to be a sizable project on its own, and in it, I'll go over some of the bugs I worked directly on (other MemShrink folks, in particular Eric Rahm and Mike Hommey, have their own jemalloc3 war stories, but I'm obviously not the best person to tell them).

<!-- RSS summary end -->

### Fixing regressions in memory metrics

[Bug 762448](https://bugzil.la/762448) was about investigating regressions in three of our memory usage metrics: 'dirty', which tracks the total memory taken by unused dirty pages the allocator hasn't returned to the system, 'waste', which is memory that is not used for either allocations or internal allocator data structures, and RSS, the amount of physical memory used by Gecko at any point in time.

The regression in 'dirty' went away when we configured jemalloc3 to be more aggressive about returning pages to the operating system. Unfortunately this had a negative effect on performance due to a jemalloc bug, which Mike Hommey tracked down and [fixed upstream](https://github.com/jemalloc/jemalloc/pull/192.) The problem with 'waste' was caused by the fact that mozjemalloc doesn't include 'bin-unused' -- memory reserved for fixed-size allocations that have not been made yet -- in 'waste', but jemalloc3 did. The solution, then, was to simply deduct 'bin-unused' from 'waste' in jemalloc3 as well.

The RSS regression can mostly be attributed to jemalloc3's thread cache (tcache) feature, though the patch for 'dirty' also caused the RSS to drop a little. The thread cache is a mechanism in which jemalloc will pre-allocate several memory regions and cache them in thread-specific data structures. That way, future allocations made in the same thread can be served by the cache, without requiring any locks at all -- which is great for highly parallel environments, but not so much for memory-constrained ones. Disabling the tcache solved this.

In order to make it more convenient to assess all of these memory metrics, Mike Hommey wrote (and [blogged about](http://glandium.org/blog/?p=3337)) a great tool for recording the memory allocations made by Gecko as it runs so they can later be replayed. John Schoenick used this to record an entire Are We Slim Yet? run, giving me a lot of data to experiment with. This also removes the noise and nondeterminism inherent to AWSY. [Bug 762448](https://bugzil.la/762448) contains graphs for my experiments with this tool.

### Measuring bookkeeping

Another important memory metric we track is 'bookkeeping', which is defined as the amount of memory used for data structures that are internal to the memory allocator. For readers that are well-versed in mozjemalloc's internals, 'bookkeeping' corresponds to base allocations plus arena and chunk headers.

Sadly, back when I was working on this, jemalloc3 didn't have a similar metric, and implementing it in the general case would have been quite tricky: not only would we be upstreaming our accounting logic as implemented in mozjemalloc, but we would also have to measure the bookkeeping for optional features (such as quarantine and tcache) that are not enabled in Gecko. Furthermore, some of this optional bookkeeping actually comes out of arenas, and as such is not easy to distinguish from actual allocations made by the application. It became apparent that the best solution then would be to import a simplified patch into our tree, measuring only what we really care about, which we did in [bug 899126](https://bugzil.la/899126.)

Recently, jemalloc3 has begun to accommodate our use case by exposing some new statistics on the memory used for allocator metadata, from which 'bookkeeping' can be computed. [Bug 1125514](https://bugzil.la/1125514) tracks the task of switching to this new mechanism.

### Junk filling on free only

As a debugging aid and security measure, mozjemalloc will initialize every byte of allocated memory with the special value @0xa5@ on debug builds, and fill every byte of deallocated memory with @0x5a@ on both debug and optimized builds, a feature known as junk filling. Unfortunately, jemalloc3 wasn't capable of junking memory on free only, so in order to keep our current behavior on optimized builds, we upstreamed a patch in [bug 1108045](https://bugzil.la/1108045) to enable that.

### Properly reporting huge allocations

Back in [bug 683597](https://bugzil.la/683597), mozjemalloc was tweaked so that accounting for huge allocations in our memory metrics considered the fact that modern operating systems are typically lazy when backing mapped memory with physical memory. Here, a 'huge' allocation is one that is (roughly) above (moz)jemalloc's chunk size, which we set to 1MiB.

Thus, an allocation of, say, 1 chunk + 1 byte would get rounded up by the allocator to 2 chunks internally, but under normal conditions, only 1 chunk + 1 page would ever get used by Gecko, and only when those pages were actually touched. We wanted our memory reporting tools to reflect that, and not the larger internal mapping. [Bug 801536](https://bugzil.la/801536) was filed to upstream that change to jemalloc3.

As it turns out, porting that change to jemalloc3 results in quite a big patch, and Jason Evans, the maintainer of jemalloc, was understandably reluctant to accept it. Unfortunately, his proposed solution ended up not being a great fit for our purposes, so as of this writing this bug is still unsolved. My big patch is attached to it, though.

### Other bugs we unveiled

Interestingly, switching memory allocators can inadvertently uncover subtle bugs. As far as I'm aware, this happened three times as we worked on jemalloc3, resulting in bugs [1088042](https://bugzil.la/1088042), [1107694](https://bugzil.la/1107694), and [1120937](https://bugzil.la/1120937.) All of these were the result of accessing uninitialized memory, whose contents changed when we switched allocators.

### Next steps

Despite the still-unresolved dependencies of the [jemalloc3 meta-bug](https://bugzil.la/762449) and remaining regressions in performance and memory usage in some platforms, it looks like jemalloc3 is here to stay, which means most of the pieces we need for heap partitioning are in place. This detour into memory allocators was great fun and taught me a lot, but there's still some work to be done back in security-land -- and I'll blog about that next time.
