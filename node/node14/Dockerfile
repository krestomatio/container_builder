# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:8-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=node:14 \
    IMAGE_SUMMARY="Nodejs 14 image based on CentOS 8 Stream minimal" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image with node 14 javascript runtime" \
    IMAGE_TITLE="Node image based on CentOS 8 Stream minimal"

# Component bash variables
ENV NODE_VERSION="14"

# Container variables
ENV CTR_CMD="node" \
    CTR_USER=node \
    CTR_USER_ID="1001" \
    CTR_USER_GECOS="Node user" \
    CTR_HOME="/home/node"

# Frequent environment variables
ENV HOME="${CTR_HOME}"

RUN containeruser-create; ${CTR_PKG_MGM} module enable nodejs:14; install-pkgs nodejs

USER ${CTR_USER_ID}

WORKDIR ${CTR_HOME}

CMD $CTR_CMD

# Labels
LABEL name="${IMAGE_NAME}" \
    summary="${IMAGE_SUMMARY}" \
    maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
    description="${IMAGE_DESCRIPTION}" \
    org.opencontainers.image.title="${IMAGE_TITLE}" \
    org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
    org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
    io.k8s.description="${IMAGE_DESCRIPTION}" \
    io.k8s.display-name="${IMAGE_TITLE}" \
    io.openshift.tags="${IMAGE_NAME},node,node14,node-fermium"
