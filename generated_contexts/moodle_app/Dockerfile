# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_NAME=moodle_app \
    IMAGE_SUMMARY="Moodle app code $MOODLE_VERSION" \
    IMAGE_DESCRIPTION="This CentOS 8 minimal based container image has Moodle code for ${MOODLE_VERSION}" \
    IMAGE_TITLE="Moodle ${MOODLE_VERSION}" \
    MOODLE_VERSION="3.9" \
    MOODLE_VER_SHORT="39"

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
    GIT_COMMIT="87bcff8c6e75421f87ba46419dcd11206e4688da" \
    GIT_REMOTE="git://github.com/moodle/moodle" \
    GIT_CHK="https://api.github.com/repos/moodle/moodle/git/refs/heads/MOODLE_39_STABLE"

# get source code
RUN git clone --branch "${GIT_BRANCH}" --depth 1 \
    "${GIT_REMOTE}" "${GIT_DEST}"

# verify it has changed
ADD "${GIT_CHK}" /tmp/version.json

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
      io.openshift.tags="${IMAGE_NAME},moodle,moodle-${MOODLE_VER_SHORT},moodle${MOODLE_VERSION}"
