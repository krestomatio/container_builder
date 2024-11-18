# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:9-minimal
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=centos:9-base \
    IMAGE_SUMMARY="CentOS 9 Stream minimal based image" \
    IMAGE_DESCRIPTION="CentOS 9 Stream minimal based for building other images" \
    IMAGE_TITLE="CentOS 9 Stream minimal based image"

# Container variables
ENV CTR_PKG_MGM="microdnf --setopt=tsflags=nodocs -y" \
    CTR_USER=default \
    CTR_USER_ID="1001" \
    CTR_USER_GECOS="Default Application User" \
    CTR_GROUP=root \
    CTR_GROUP_ID="0" \
    CTR_APP="/opt/default" \
    CTR_ENTRYPOINT_OPT_PATH=/opt/container-entrypoint.d

ENV OS_INSTALL_PKGS="findutils gzip platform-python"

COPY conf/usr/bin /usr/bin/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup
RUN install-pkgs -n ${OS_INSTALL_PKGS}

ENTRYPOINT ["container-entrypoint"]

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_NAME},centos,centos9-stream"
