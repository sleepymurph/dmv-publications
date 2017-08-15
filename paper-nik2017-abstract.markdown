Abstract --- Distributed Media Versioning
==================================================

Today's computer user typically has multiple computing devices--- a home
computer/laptop, a mobile phone, probably a work computer, and maybe more. The
user's data will be both sharded and replicated across these devices in an
ad-hoc fashion, according to where the data is produced and where it is
consumed. The task of tracking what data is where typically falls to the users
themselves, who can easily forget. Cloud computing offers a solution by
centralizing all data on a third-party server, but this opens concerns about
privacy, service longevity, and connectivity to the servers. Distributed version
control systems can synchronize a data set amongst an ad-hoc network of
repositories, but they are designed for the small text files of source code, and
are limited by RAM and disk space when working with media files such as photos,
audio, and video that a user might want to manage.

In this paper we perform experiments to explore the scaling limitations of
existing version control and backup systems, and present an architecture,
design, and prototype of a tool that attempts to both avoid those limitations
and provide more flexibility. This tool will track a data set that includes
files in a wide range of sizes--- from kilobyte text files to multi-gigabyte
video files--- shard and replicate this data across devices with varying
resources, and provide a unified view of the data set with version tracking and
synchronization across intermittent networks. We find that our early prototype
repeats certain design mistakes that lead to performance degradation when
managing many files, and propose we changes for further work.
