---
fontsize: 10pt
papersize: a4paper
linestretch: 1.0
...

Distributed Media Versioning: Cross-Device Data Sets
=====================================================

Abstract
--------------------------------------------------

A typical computer user has multiple devices holding an increasing amount of
data. Most users will have at least a computer and a mobile phone. Many will
also have a work computer, tablet, or other device. These devices have varying
resources, including processing, memory, and storage. They may also be in
different locations, on different networks, or turned off at any time. The
user's data will be in files of varying sizes and media types, from kilobyte
text documents to multi-gigabyte videos. The volume of data is also always
increasing, as data is authored, collected from the internet, gathered from
mobile sensors. This data is strewn across these devices in an ad-hoc fashion,
according to where it is produced and consumed. When the user needs a particular
piece of data, must either remember where it is or perform a frustrating,
manual, multi-device search. Copies of data of different devices can diverge if
updates are made separately and not reconciled.

Cloud computing avoids this trouble by centralizing data in a third-party
service. Centralized data will not diverge and is easy to search. However,
availability is determined by the bandwidth and latency of the connection to the
service. Handing the data to a third-party also raises concerns about privacy,
service longevity, and cost.

This paper explores distributed version control systems as an alternative
approach to managing data across a spectrum of devices. A DVCS keeps writable
copies of a data set at multiple locations, tracks update history, and allows
diverging versions to be merged at a later date. However, version control
systems are designed for the small text files of source code and are not suited
to larger binary files.

We describe the architecture, design, and implementation of a new system we call
Distributed Media Versioning (DMV) that will resemble version control but be
more flexible. DMV will allow the user to shard and replicate a data set across
many devices with fine-grained control. It will keep a unified view of the data
set as subsets of the data are copied or moved between devices by user request.
Data may be updated on any device, and DMV will keep a history. It will track
diverging versions and allow them to be merged later.

We perform experiments to explore the scalability limits of selected version
control systems. We find that the maximum file size is limited by available RAM,
and the number of files is limited by they underlying filesystem. DMV avoids the
file-size limitations by using a rolling hash algorithm to break larger files
into smaller chunks. Unfortunately our early DMV prototype suffers the same
problems with numerous files because it uses the underlying filesystem in a
similar way. We conclude that the key to processing large files is to break them
into many smaller chunks, and the key to storing many small files is to
aggregate them into larger packs. We propose corrective changes for future work
on DMV.
