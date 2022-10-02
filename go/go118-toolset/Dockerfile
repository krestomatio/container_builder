# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:9-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=go:1.18-toolset \
    IMAGE_SUMMARY="Go-toolset 1.18 image based on CentOS 9 Stream minimal" \
    IMAGE_DESCRIPTION="CentOS 9 Stream minimal based image with go-toolset 1.18" \
    IMAGE_TITLE="Go-toolset 1.18 image based on CentOS 9 Stream minimal"

# Component bash variables
ENV GO_VERSION="1.18"

# Container variables
ENV CTR_CMD="go version"

RUN install-pkgs go-toolset git make tar which curl; \
    [[ "$(go version | { read _ _ v _; echo ${v#go}; })" == "${GO_VERSION}".* ]] || echo "error: version differs from env var"

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
    io.openshift.tags="${IMAGE_NAME},go,go-toolset,go1.18-toolset"
