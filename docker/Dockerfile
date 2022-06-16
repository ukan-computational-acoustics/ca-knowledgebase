FROM ubuntu:22.04 as ca-knowledgebase
LABEL maintainer=""
LABEL description="Environment with all dependencies for the CA knowledgebase"

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -qq update && \
    apt-get -yq --with-new-pkgs -o Dpkg::Options::="--force-confold" upgrade && \
    apt-get -y install \
    sl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
