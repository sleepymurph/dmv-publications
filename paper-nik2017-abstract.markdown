---
fontsize: 10pt
papersize: a4paper
linestretch: 1.2
...

Abstract --- Distributed Media Versioning
==================================================

A typical computer user has multiple devices holding an increasing amount of
data. Most users will have at least a computer and a mobile phone. Many will
also have a work computer, tablet, or other device. These devices vary in
processing power and storage capacity. They may also be in different locations,
on different networks, or turned off at any time. A user's data will be of
varying file sizes and media types, from kilobyte text documents to
multi-gigabyte videos. The amount of data is also always increasing as mobile
cameras and other sensors collect photos, videos, and other new streams of data.
This data is strewn across these devices in an ad-hoc fashion, according to
where it is produced and consumed. When a particular piece of data is needed,
the user must either remember where it is or perform a time-consuming
multi-device search. Multiple copies can also diverge if they are updated on
separate devices.

Cloud computing avoids this trouble by centralizing data in a third-party
service. Centralized data will not diverge and is easy to search. However,
availability is determined by the bandwidth and latency of the connection to the
service. Handing the data to a third-party also raises concerns about privacy,
service longevity, and cost. A distributed filesystem would keep the user's data
on the user's own devices, but traditional DFSs are designed for the data center
rather than the wide variation of consumer devices.

This paper explores distributed version control systems as an alternative
approach to managing data across various devices. DVCSs keep writable copies of
a data set an multiple locations, track update history, and allow merging at a
later date. However, version control systems are designed for the small text
files of source code and are not suited to larger binary files. We perform
experiments to explore the scalability limits of existing version control
systems. We find that maximum file size is limited by available RAM, and that
commit times increase dramatically as the number of file sizes increases into
the millions. We describe the architecture, design, and prototype of a new tool
that tries to avoid these limitations. The new tool will resemble version
control but it will be more flexible. It will allow the user to shard and
replicate a data set across many devices with fine-grained control. It will keep
a unified view of the data set as subsets of the data are copied or moved
between devices by user request. Data may be updated on any device, and the tool
will keep a history. It will track diverging versions and allow them to be
merged later. We compare our early prototype to existing systems, and we find
that it repeats certain design mistakes that lead to performance degradation
when managing many files. We propose corrective changes for further work.
