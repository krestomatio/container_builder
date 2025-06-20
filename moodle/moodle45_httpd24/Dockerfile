# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/httpd:2.4
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=moodle:4.5-httpd \
    IMAGE_SUMMARY="Apache ${HTTPD_VERSION} for Moodle 4.5" \
    IMAGE_DESCRIPTION="This CentOS 9 Stream minimal based container image runs Apache ${HTTPD_VERSION} for Moodle 4.5" \
    IMAGE_TITLE="Apache ${HTTPD_VERSION} for Moodle4.5 " \
    TZ="UTC"

# Component bash variables
ENV MOODLE_VERSION="4.5" \
    MOODLE_VERSION_SHORT="45" \
    MOODLE_APP=${APP_DEST} \
    MOODLE_DATA=/var/moodledata \
    MOODLE_CHECK_PATH=/login/index.php \
    MOODLE_CHECK_CODE="200" \
    MOODLE_CHECK_HOST=localhost

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/usr/libexec /usr/libexec/

RUN container-setup

RUN container-setup-httpd-moodle

USER ${CTR_USER_ID}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="4.5.5" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_NAME},apache,apache${HTTPD_VER_SHORT},apache-${HTTPD_VER_SHORT},moodle,moodle${MOODLE_VERSION_SHORT},moodle-${MOODLE_VERSION_SHORT}"
