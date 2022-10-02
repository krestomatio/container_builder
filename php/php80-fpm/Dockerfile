# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:9-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=php:8.0 \
    IMAGE_SUMMARY="PHP 8.0 FPM" \
    IMAGE_DESCRIPTION="This CentOS 9 Stream minimal based container image runs PHP 8.0 FPM" \
    IMAGE_TITLE="PHP 8.0" \
    IMAGE_OC_TAGS="${IMAGE_NAME},php,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},php-fpm" \
    IMAGE_SERVICE_PORT="9000" \
    IMAGE_SERVICE_NAME="php-fpm"

# Container variables
ENV CTR_USER=apache \
    CTR_USER_ID="48" \
    CTR_CMD="php-fpm" \
    CTR_STOPSIGNAL=SIGQUIT

# Component bash variables
ENV PHP_VERSION="8.0" \
    PHP_VER_SHORT="80" \
    PHP_RUN=/var/run/php-fpm \
    PHP_CONF_DIR=/etc/php.d \
    PHP_CONF_FILE=/etc/php.ini \
    PHP_MODULE_DIR=/usr/lib64/php/modules/ \
    PHP_FPM_CONF_DIR=/etc/php-fpm.d \
    PHP_FPM_CONF_FILE=/etc/php-fpm.conf \
    PHP_FPM_POOL_FILE=/etc/php-fpm.d/www.conf \
    PHP_FPM_PORT=${IMAGE_SERVICE_PORT} \
    APP_DEST=/var/www/html

ENV OS_INSTALL_PKGS="php-fpm php-cli php-opcache php-soap"

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup && container-setup-php

WORKDIR ${APP_DEST}

USER ${CTR_USER_ID}

STOPSIGNAL ${CTR_STOPSIGNAL}

EXPOSE ${PHP_FPM_PORT}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="8.0.3" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_OC_TAGS}"
