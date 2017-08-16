DMV Paper for NIK 2017
==================================================

This is the LaTeX source for the DMV paper we submitted to NIK 2017
(<http://nikt2017.no/>).

To build the PDF:

    make

Requires a TeX Live installation and a few other packages. If you do not want to
deal with dependencies, there is also a Docker container that creates a build
environment:

To build with Docker:

    docker build -t dmv-nik-compile . && \
    docker run --rm --name dmv-nik-compile \
        -e UID=$(id -u) \
        -v $(readlink -f .):/home/compile/src \
        dmv-nik-compile

Note: A fresh installation of TeX Live is a very big install. It will take a
while to initially build the container, and the container will take up over 3 GB
of space in `/var`. But once the container is created, running the LaTeX build
inside of it is quick and painless.
