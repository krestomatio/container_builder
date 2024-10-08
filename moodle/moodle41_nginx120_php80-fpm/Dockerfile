# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/nginx:1.20-php-fpm
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=moodle:4.1-nginx_php-fpm \
    IMAGE_SUMMARY="Nginx ${NGINX_VERSION:-1.20} and PHP-FPM ${PHP_VERSION:-8.0} for Moodle 4.1" \
    IMAGE_DESCRIPTION="This CentOS 9 Stream minimal based container image runs Nginx ${NGINX_VERSION:-1.20} or PHP-FPM ${PHP_VERSION:-8.0} for Moodle 4.1" \
    IMAGE_TITLE="Nginx ${NGINX_VERSION:-1.20} for Moodle 4.1" \
    IMAGE_OC_TAGS="${IMAGE_NAME},php,php-fpm,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},nginx,nginx-${NGINX_VER_SHORT},nginx${NGINX_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT}" \
    TZ="UTC"

# Component bash variables
ENV APP_DEST=/var/www/html

ENV MOODLE_VERSION="4.1" \
    MOODLE_VERSION_SHORT="41" \
    MOODLE_APP=${APP_DEST} \
    MOODLE_DATA=/var/moodledata \
    MOODLE_CHECK_PATH=/login/index.php \
    MOODLE_CHECK_CODE="200" \
    MOODLE_CHECK_HOST=localhost

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/usr/libexec /usr/libexec/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup

RUN container-setup-nginx-moodle

USER ${CTR_USER_ID}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="4.1.13" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_OC_TAGS}"
