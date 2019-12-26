# Ansible managed

# first stage
FROM registry.access.redhat.com/ubi8/php-72 AS build

ENV PHP_VERSION="7.2" \
    PHP_VER_SHORT="72" \
    APACHE_VERSION="2.4" \
    APACHE_VER_SHORT="24" \
    MOODLE_VERSION="3.5" \
    MOODLE_VER_SHORT="35" \
    IMAGE_AUTHORS="Job Céspedes Ortiz <jobcespedes@gmail.com>"
    TZ="America/Costa_Rica"

ENV NAME=apache${APACHE_VER_SHORT}_php${PHP_VER_SHORT}_moodle${MOODLE_VER_SHORT} \
    SUMMARY="PHP $PHP_VERSION for Moodle" \
    DESCRIPTION="This UBI based docker image runs \
    PHP $PHP_VERSION for Moodle" \
    TITLE="Apache 2.4 with PHP ${PHP_VERSION} for Moodle"

LABEL org.opencontainers.image.title="${TITLE}" \
      org.opencontainers.image.authors="${AUTHORS}" \
      org.opencontainers.image.description="${DESCRIPTION}" \
      org.opencontainers.image.version="${MOODLE_VERSION}" \
      summary="${SUMMARY}" \
      description="${DESCRIPTION}" \
      io.k8s.description="${DESCRIPTION}" \
      io.k8s.display-name="${TITLE}" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,apache,apache${APACHE_VER_SHORT},apache-${APACHE_VER_SHORT},php,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT},${NAME}" \
      io.openshift.s2i.scripts-url="image:///usr/libexec/s2i" \
      io.s2i.scripts-url="image:///usr/libexec/s2i" \
      name="ubi8/${NAME}" \
      maintainer="${IMAGE_AUTHORS}"
