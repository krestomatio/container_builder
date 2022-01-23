# Ansible managed
FROM quay.io/krestomatio/moodle_app AS app
ENV GIT_COMMIT=3bd1f3824982025b15cdc685a5d1d508a8c811c9
RUN app-git -v -a -e '.git*'

FROM quay.io/krestomatio/moodle_nginx_web

# General ansible variables
ENV IMAGE_NAME=moodle_web \
    IMAGE_SUMMARY="PHP $PHP_VERSION and NGINX ${NGINX_VERSION} for Moodle" \
    IMAGE_DESCRIPTION="This CentOS 8 Stream minimal based container image runs PHP ${PHP_VERSION} and NGINX ${NGINX_VERSION} for Moodle" \
    IMAGE_TITLE="PHP ${PHP_VERSION} and NGINX ${NGINX_VERSION} for Moodle" \
    IMAGE_OC_TAGS="${IMAGE_NAME},php,php-fpm,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},nginx,nginx-${NGINX_VER_SHORT},nginx${NGINX_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT}" \
    TZ="UTC"

# Component bash variables
ENV MOODLE_VERSION="3.9" \
    MOODLE_VERSION_SHORT="39" \
    MOODLE_APP=${APP_DEST} \
    MOODLE_DATA=/var/moodledata \
    MOODLE_CLI_TOOLS=/usr/libexec/moodle

# php-curl included in php-common
# php-zip as php-pecl-zip
# php-xsl as php-xml
# php-fpm php-cli php-opcache already installed in base image
ENV MOODLE_INSTALL_PHP_PKGS="php-gd php-intl php-ldap php-pgsql php-soap php-xmlrpc php-xml php-pecl-zip php-mbstring php-json"

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/usr/libexec /usr/libexec/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup
RUN install-pkgs ${MOODLE_INSTALL_PHP_PKGS}
RUN container-setup-php-moodle

USER ${CTR_USER_ID}

ENV MOODLE_COMMIT="3bd1f3824982025b15cdc685a5d1d508a8c811c9" \
    MOODLE_VERSION_NUMBER="2020061512.01"

COPY --chown=${CTR_USER_ID}:0 --from=app /var/www/html/ /var/www/html

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="3.9" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_OC_TAGS}"
