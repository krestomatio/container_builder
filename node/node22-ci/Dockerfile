# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/node:22
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=node:22-ci \
    IMAGE_SUMMARY="Nodejs 22 image based on CentOS 9 Stream minimal for Continuous Integration (CI)" \
    IMAGE_DESCRIPTION="CentOS 9 Stream minimal based image with node 22 javascript runtime for CI" \
    IMAGE_TITLE="Node image based on CentOS 9 Stream minimal for CI"

USER 0

RUN install-pkgs make git curl tar xz unzip procps-ng
RUN npm i -g @nestjs/cli@10 npm-check depcheck && \
    npm cache clean --force && \
    rm -rf ~/.npm

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
    io.openshift.tags="${IMAGE_NAME},node,node22,node-jod,node-ci,ci"
