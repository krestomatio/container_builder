# Ansible managed
FROM registry.access.redhat.com/ubi8/ubi-minimal

ENV PHP_VERSION="7.2" \
    PHP_VER_SHORT="72" \
    APACHE_VERSION="2.4" \
    APACHE_VER_SHORT="24" \
    MOODLE_VERSION="3.5" \
    MOODLE_VER_SHORT="35" \
    IMAGE_AUTHORS="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
    TZ="America/Costa_Rica"

ENV NAME=apache${APACHE_VER_SHORT}_php${PHP_VER_SHORT}_moodle${MOODLE_VER_SHORT} \
    SUMMARY="PHP $PHP_VERSION for Moodle" \
    DESCRIPTION="This UBI based docker image runs \
    PHP $PHP_VERSION for Moodle" \
    TITLE="Apache 2.4 with PHP ${PHP_VERSION} for Moodle" \
    HTTPD_PORT="8080"

LABEL org.opencontainers.image.title="${TITLE}" \
      org.opencontainers.image.authors="${AUTHORS}" \
      org.opencontainers.image.description="${DESCRIPTION}" \
      org.opencontainers.image.version="${MOODLE_VERSION}" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      io.k8s.description="${DESCRIPTION}" \
      io.k8s.display-name="${TITLE}" \
      io.openshift.expose-services="${HTTPD_PORT}:http" \
      io.openshift.tags="builder,apache,apache${APACHE_VER_SHORT},apache-${APACHE_VER_SHORT},php,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT},${NAME}" \
      maintainer="${IMAGE_AUTHORS}"

# php-curl included in php-common
# php-zip as php-pecl-zip
# php-xsl as php-xml
ENV INSTALL_PKGS="httpd php-fpm php-cli php-gd php-intl php-ldap \
                  php-opcache php-pgsql php-soap php-xmlrpc  \
                  php-xml php-pecl-zip php-mbstring"

# Update
# Reconfig timezone
# Install php dependencies
# `mkdir -p /run/user/$(id -u)` for
# https://github.com/rpm-software-management/microdnf/issues/50
RUN microdnf update -y && \
	rpm -e --nodeps tzdata && \
    mkdir -p /run/user/$(id -u) && \
    microdnf --setopt=tsflags=nodocs -y install tzdata \
    $INSTALL_PKGS && \
    rpm -V $INSTALL_PKGS && \
    microdnf clean all

ENV PHP_SYSCONF_PATH=/etc \
    PHP_HTTPD_CONF_FILE=php.conf \
    PHP_RUN=/run/php-fpm \
    HTTPD_MAIN_CONF_PATH=/etc/httpd/conf \
    HTTPD_MAIN_CONF_D_PATH=/etc/httpd/conf.d \
    HTTPD_MODULES_CONF_D_PATH=/etc/httpd/conf.modules.d \
    HTTPD_VAR_RUN=/run/httpd \
    HTTPD_PUBLIC_PATH=/var/www/html \
    HTTPD_DATA_ORIG_PATH=/var/www \
    HTTPD_LOG_PATH=/var/log/httpd \
    HTTPD_VAR_PATH=/var

ENV CUSER=apache \
    CUSER_ID="48" \
    CGROUP=root \
    CGROUP_ID="0"

COPY conf/usr/bin/* /usr/bin/

COPY conf/etc/php.d/* /etc/php.d/

RUN container-setup && rpm-file-permissions

WORKDIR ${HTTPD_PUBLIC_PATH}

USER ${CUSER_ID}

EXPOSE ${HTTPD_PORT}

ENTRYPOINT ["container-entrypoint"]

CMD php-fpm & httpd -D FOREGROUND
