FROM debian:jessie

# Get lists of apt packages
RUN apt-get update

# Install essentials for building
RUN apt-get install -y \
            build-essential \
    && echo "ok"

# Create a user
RUN useradd --create-home --shell /bin/bash compile

# Give the user sudo access
RUN \
    apt-get install -y sudo && \
    echo "compile ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/compile-user && \
    chmod 0440 /etc/sudoers.d/compile-user

# Switch to user

USER compile
WORKDIR /home/compile

# Install TeX
# Running as its own step because it's such a huge download.
# This is a good point to cache before fiddling with the other packages.
RUN sudo apt-get install -y texlive

# Install additional TeX packages needed for thesis
RUN sudo apt-get install -y \
            texlive-bibtex-extra \
            texlive-fonts-extra \
            texlive-science \
    && echo "ok"

# Install additional tools needed for thesis
RUN sudo apt-get install -y \
            gnuplot5 \
            graphviz \
            m4 \
    && echo "ok"

# Install handy user tools (what Mike considers essential)
RUN sudo apt-get install -y \
            git \
            psmisc \
            tmux \
            vim \
    && echo "ok"


# Default command: a login shell
# Should be a login shell to source ~/.profile
CMD ["/bin/bash", "-l"]
