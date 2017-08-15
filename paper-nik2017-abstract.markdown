---
fontsize: 10pt
papersize: a4paper
linestretch: 1.1
...

Abstract --- Distributed Media Versioning
==================================================

A typical computer user has multiple devices holding an increasing amount of
data. Most users will have at least a computer and a mobile phone. Many will
also have a work computer or tablet. Others may have even more. These devices
vary in processing power and storage capacity. They may also be in different
locations, on different networks, or turned off at any time. A user's data will
be of varying size and media types, from kilobyte text documents to
multi-megabyte photos to multi-gigabyte videos. The amount of data is also
always increasing. Documents are written, cameras record photos and video, media
is purchased and downloaded, and mobile sensors record location and biometric
data. This data is strewn across these devices in an ad-hoc fashion. It often
simply stays where it is produced. Sometimes it is copied elsewhere for access,
sharing, or backup. Sometimes it is moved to free space on a low-capacity
device. Replicated data can also diverge as it is updated in one place, then in
another. When a particular piece of data is needed, the user must either
remember where it is or perform a time-consuming multi-device search.

Cloud computing avoids these issues by centralizing all data in a third-party
service. Centralized data will not diverge and is easy to search. However,
availability is determined by the bandwidth and latency of the connection to the
service. Handing the data to a third-party also raises concerns about privacy,
service longevity, and cost. A distributed filesystem would keep the user's data
on the user's own devices, but traditional DFSs are designed for the data center
rather than the wide variation of consumer devices. Another approach would be to
put everything into a distributed version control system. DVCSs keep writable
copies of a data set an multiple locations, track update history, and allow
merging at a later date. However, version control systems are designed for the
small text files of source code and are less well-suited to varying media types.

In this paper we explore version control as an approach to this problem of data
management across personal devices. We perform experiments to determine the
scalability limits of existing version control systems in terms of file size and
number of files in the set. We find that maximum file size is constrained by
RAM, and that write performance degrades significantly as the number of files
increases into the millions. We describe the architecture, design, and prototype
of a new tool that avoids these limitations. The new tool will allow the user to
shard and replicate data across many devices, over high-latency connections,
while maintaining a unified view of the data set. Data may be updated on any
device, and the tool will track diverging versions and allow them to be merged
later. We find that our early prototype repeats certain design mistakes that
lead to performance degradation when managing many files, and we propose changes
for further work.
