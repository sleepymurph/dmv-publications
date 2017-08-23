FROM debian:jessie

RUN apt-get update \
    && apt-get install -y \
            build-essential \
            texlive \
            texlive-bibtex-extra \
            texlive-fonts-extra \
            texlive-science \
            gnuplot5 \
            graphviz \
            m4 \
            git \
    && rm -r /var/lib/apt/lists/* /var/cache/apt/*

ENV UID 1000
RUN useradd --uid $UID --create-home --shell /bin/bash compile
USER compile
RUN mkdir /home/compile/dmv-publications
WORKDIR /home/compile/dmv-publications/thesis-src

CMD ["make"]
