# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:9-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=httpd:2.4 \
    IMAGE_SUMMARY="Apache 2.4" \
    IMAGE_DESCRIPTION="This CentOS 9 Stream minimal based container image runs Apache 2.4" \
    IMAGE_TITLE="Apache 2.4" \
    IMAGE_SERVICE_PORT="8080" \
    IMAGE_SERVICE_NAME="http"

# Container variables
ENV CTR_USER=apache \
    CTR_USER_ID="48" \
    CTR_CMD="httpd -D FOREGROUND" \
    CTR_STOPSIGNAL=SIGWINCH

# Component bash variables
ENV HTTPD_VERSION="2.4" \
    HTTPD_VER_SHORT="24" \
    HTTPD_MAIN_CONF_PATH=/etc/httpd/conf \
    HTTPD_MAIN_CONF_FILE=/etc/httpd/conf/httpd.conf \
    HTTPD_MAIN_CONF_D_PATH=/etc/httpd/conf.d \
    HTTPD_MODULES_CONF_D_PATH=/etc/httpd/conf.modules.d \
    HTTPD_VAR_RUN_PATH=/var/run/httpd \
    HTTPD_PORT=${IMAGE_SERVICE_PORT} \
    HTTPD_LOG_PATH=/var/log/httpd \
    APP_DEST=/var/www/html

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup

RUN container-setup-httpd

WORKDIR ${APP_DEST}

USER ${CTR_USER_ID}

STOPSIGNAL ${CTR_STOPSIGNAL}

EXPOSE ${HTTPD_PORT}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="2.4.40" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},apache,apache-${HTTPD_VER_SHORT},apache${HTTPD_VER_SHORT}"
