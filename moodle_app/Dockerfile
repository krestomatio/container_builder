# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_NAME=moodle_app \
    IMAGE_SUMMARY="Moodle app code $MOODLE_VERSION" \
    IMAGE_DESCRIPTION="This CentOS 8 Stream minimal based container image has Moodle code for ${MOODLE_VERSION}" \
    IMAGE_TITLE="Moodle ${MOODLE_VERSION}" \
    MOODLE_VERSION="3.9" \
    MOODLE_VERSION_SHORT="39" \
    MOODLE_VERSION_NUMBER="2020061507.02"

# Container variables
ENV CTR_USER=apache \
    CTR_USER_ID="48" \
    CTR_CMD="app-git -s"

# Component bash variables
ENV GIT_DEST="/opt/app/" \
    APP_DEST=/var/www/html

ENV OS_INSTALL_PKGS="git rsync"

USER 0

COPY conf/usr/bin/* /usr/bin/

RUN container-setup
RUN install-pkgs ${OS_INSTALL_PKGS}
RUN container-setup-app

USER ${CTR_USER_ID}
WORKDIR ${GIT_DEST}

# source variables
ENV GIT_BRANCH="MOODLE_39_STABLE" \
    GIT_COMMIT="8dea153c6b6d50ec8a00979b53a1eb4decb65589" \
    GIT_REMOTE="git://github.com/moodle/moodle"

# verify it has changed
ADD version.json /tmp/version.json

# get source code
RUN git clone --branch "${GIT_BRANCH}" --depth 1 \
    "${GIT_REMOTE}" "${GIT_DEST}"

# Pull and verify
RUN app-git -p -v

# Allow pull for other than root
RUN fix-permissions -u ${CTR_USER_ID} ${GIT_DEST}/.git

WORKDIR ${APP_DEST}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="3.9" \
      org.opencontainers.image.revision="${GIT_COMMIT}" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_NAME},moodle,moodle-${MOODLE_VERSION_SHORT},moodle${MOODLE_VERSION}"
