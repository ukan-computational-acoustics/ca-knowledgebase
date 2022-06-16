FROM ubuntu:22.04 as ca-knowledgebase
LABEL maintainer=""
LABEL description="Environment with all dependencies for the CA knowledgebase"

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -qq update && \
    apt-get -yq --with-new-pkgs -o Dpkg::Options::="--force-confold" upgrade && \
    apt-get -y install python3-dev python3-pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN pip3 install jupyter-book>=0.7.0b matplotlib numpy scipy
