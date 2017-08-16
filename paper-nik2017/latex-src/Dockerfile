FROM debian:stretch

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
    && rm -r /var/lib/apt/lists/* /var/cache/apt/*

RUN mkdir /root/latex
WORKDIR /root/latex

CMD ["make"]
