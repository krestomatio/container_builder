# Ansible managed
FROM quay.io/krestomatio/rocky8-minimal

# General variables
ENV IMAGE_NAME=base \
    IMAGE_SUMMARY="Rocky Linux 8 minimal based image" \
    IMAGE_DESCRIPTION="Rocky Linux 8 minimal based for building other images" \
    IMAGE_TITLE="Rocky Linux 8 minimal based image"

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

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup
RUN install-pkgs ${OS_INSTALL_PKGS}

ENTRYPOINT ["container-entrypoint"]

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
      io.openshift.tags="${IMAGE_NAME},rocky,rocky8"
