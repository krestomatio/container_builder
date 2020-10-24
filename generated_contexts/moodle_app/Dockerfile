# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=moodle_app \
    IMAGE_summary="Moodle app code $MOODLE_version" \
    IMAGE_description="This CentOS 8 minimal based container image has Moodle code for ${MOODLE_version}" \
    IMAGE_title="Moodle ${MOODLE_version}" \
    MOODLE_version="3.9" \
    MOODLE_ver_short="39"

# Container variables
ENV CTR_user=apache \
    CTR_user_id="48" \
    CTR_cmd="app-git -s"

# Component bash variables
ENV GIT_dest="/opt/app/" \
    APP_dest=/var/www/html

ENV OS_install_pkgs="git rsync"

USER 0

COPY conf/usr/bin/* /usr/bin/

RUN container-setup
RUN install-pkgs ${OS_install_pkgs}
RUN container-setup-app

USER ${CTR_user_id}
WORKDIR ${GIT_dest}

# source variables
ENV GIT_branch="MOODLE_39_STABLE" \
    GIT_commit="4d9ab4ca4825d689dcd49767c101eb5139705f33" \
    GIT_remote="git://github.com/moodle/moodle" \
    GIT_chk="https://api.github.com/repos/moodle/moodle/git/refs/heads/MOODLE_39_STABLE"

# get source code
RUN git clone --branch "${GIT_branch}" --depth 1 \
    "${GIT_remote}" "${GIT_dest}"

# verify it has changed
ADD "${GIT_chk}" /tmp/version.json

# Pull and verify
RUN app-git -p -v

# Allow pull for other than root
RUN fix-permissions -u ${CTR_user_id} ${GIT_dest}/.git

WORKDIR ${APP_dest}

CMD ${CTR_cmd}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="3.9.2-4d9ab" \
      org.opencontainers.image.revision="${GIT_commit}" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_name},moodle,moodle-${MOODLE_ver_short},moodle${MOODLE_version}"
