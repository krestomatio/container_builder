# Ansible managed
FROM docker.io/centos:8

# General variables
ENV IMAGE_NAME=rootfs-creator \
    IMAGE_SUMMARY="CentOS 8 based image" \
    IMAGE_DESCRIPTION="CentOS 8 based for building rootfs" \
    IMAGE_TITLE="CentOS 8 based image"

# Container variables
ENV CTR_WORKING_DIR=/build

RUN dnf install -y anaconda-tui lorax jq
RUN mkdir $CTR_WORKING_DIR

COPY conf/usr/bin/* /usr/bin/

WORKDIR $CTR_WORKING_DIR

ENTRYPOINT ["/usr/bin/rootfs-creator"]

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_NAME},centos,centos8,rootfs-creator"
