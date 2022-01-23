FROM quay.io/krestomatio/base-stream

# General variables
ENV IMAGE_NAME=keydb \
    IMAGE_SUMMARY="KeyDB 6.2.1" \
    IMAGE_DESCRIPTION="This CentOS 8 Stream minimal based container image runs KeyDB 6.2.1" \
    IMAGE_TITLE="KeyDB 6.2.1" \
    IMAGE_SERVICE_PORT="6379" \
    IMAGE_SERVICE_NAME="keydb" \
    TZ="UTC"

# Container variables
ENV CTR_USER=keydb \
    CTR_USER_ID="998" \
    CTR_CMD="keydb-server /etc/keydb/keydb.conf"

# Component bash variables
ENV KEYDB_VERSION="6.2.1" \
    KEYDB_VERSION_PCKG="6.2.1-1" \
    KEYDB_PORT=${IMAGE_SERVICE_PORT} \
    KEYDB_CONF_DIR=/etc/keydb \
    KEYDB_CONF_FILE=/etc/keydb/keydb.conf \
    KEYDB_DATA="/data" \
    KEYDB_FLASH="/flash"


ENV OS_INSTALL_PKGS="initscripts libatomic logrotate"

USER 0

COPY conf/usr /usr/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN install-pkgs ${OS_INSTALL_PKGS}
RUN container-setup && container-setup-keydb

VOLUME ${KEYDB_DATA}
WORKDIR ${KEYDB_DATA}

USER ${CTR_USER_ID}

EXPOSE ${KEYDB_PORT}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="6.2" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},keydb,keydb-${KEYDB_VERSION},keydb${KEYDB_VERSION}"
