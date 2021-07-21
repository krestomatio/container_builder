# Ansible managed
FROM quay.io/krestomatio/base-stream

# General variables
ENV IMAGE_NAME=go-toolset \
    IMAGE_SUMMARY="Go-toolset image based on CentOS 8 Stream minimal" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image with go-toolset" \
    IMAGE_TITLE="Go-toolset image based on CentOS 8 Stream minimal"

# Component bash variables
ENV GO_VERSION_MAJOR_MINOR="1.16"

# Container variables
ENV CTR_CMD="go version"

RUN install-pkgs go-toolset git make tar which curl; \
    v=$(go version | { read _ _ v _; echo ${v#go}; }); \
    [ "$GO_VERSION_MAJOR_MINOR" == "${v%.*}" ] || "error: major version differs from env var"

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
    io.openshift.tags="${IMAGE_NAME},go,go-toolset,go-toolset1.16"
