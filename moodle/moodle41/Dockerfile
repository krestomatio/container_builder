# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/moodle:4.1-nginx_php-fpm
FROM ${ARG_IMAGE_FROM} AS app-src

# Component bash variables
ENV GIT_DEST="/opt/app/" \
    APP_DEST=/var/www/html

USER 0
WORKDIR ${GIT_DEST}

# Install deps
COPY conf/usr/bin /usr/bin/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/
RUN install-pkgs git rsync php-json unzip tar && \
    mkdir -p ${GIT_DEST} ${APP_DEST}

# Get source code
# Arguments for moodle git remote, branch and commit
# They are also a mechanism to invalidate cache if changed
ARG ARG_MOODLE_REMOTE="https://github.com/moodle/moodle.git"
ARG ARG_MOODLE_BRANCH="MOODLE_401_STABLE"
ARG ARG_MOODLE_COMMIT="94ad185d09030a7b0096acd79c66af52a2b16e26"
ENV GIT_REMOTE=${ARG_MOODLE_REMOTE} \
    GIT_BRANCH=${ARG_MOODLE_BRANCH} \
    GIT_COMMIT=${ARG_MOODLE_COMMIT}
RUN git clone --branch "${GIT_BRANCH}" --depth 1 \
    "${GIT_REMOTE}" "${GIT_DEST}"

# Verify commit, if any
RUN if [ -n "${GIT_COMMIT}" ]; then app-git -v; fi

# Move src to app destination without .git files
RUN app-git -v -a -e '.git*'

COPY conf/usr/libexec /usr/libexec/

# Install additional plugins (a comma separated arg), if any
# Argument is also a mechanism to invalidate cache if changed
ARG ARG_MOODLE_PLUGIN_LIST=""
ARG ARG_MOODLE_PLUGIN_FORCE=""
ENV MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST} \
    MOODLE_PLUGIN_FORCE=${ARG_MOODLE_PLUGIN_FORCE}
RUN if [ -n "${MOODLE_PLUGIN_LIST}" ]; then /usr/libexec/moodle/install-plugin-list ${MOODLE_PLUGIN_FORCE:+-f} -p "${MOODLE_PLUGIN_LIST}"; fi

FROM ${ARG_IMAGE_FROM}

# General ansible variables
ENV IMAGE_NAME=moodle:4.1 \
    IMAGE_SUMMARY="PHP $PHP_VERSION and NGINX ${NGINX_VERSION} for Moodle 4.1" \
    IMAGE_DESCRIPTION="This CentOS 9 Stream minimal based container image runs PHP ${PHP_VERSION} or NGINX ${NGINX_VERSION} for Moodle 4.1" \
    IMAGE_TITLE="PHP ${PHP_VERSION} and NGINX ${NGINX_VERSION} for Moodle 4.1" \
    IMAGE_OC_TAGS="${IMAGE_NAME},php,php-fpm,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},nginx,nginx-${NGINX_VER_SHORT},nginx${NGINX_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT}" \
    TZ="UTC" \
    LANG="en_AU.UTF-8"

# Component bash variables
ENV PHP_MAX_INPUT_VARS=5000 \
    MOODLE_VERSION="4.1" \
    MOODLE_VERSION_SHORT="41" \
    MOODLE_APP=${APP_DEST} \
    MOODLE_DATA=/var/moodledata \
    MOODLE_CLI_TOOLS=/usr/libexec/moodle

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/usr/libexec /usr/libexec/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

# Install all locales and timezones
RUN locale-tz-all

# Install dependencies:
# php-curl included in php-common
# php-zip as php-pecl-zip
# php-xsl as php-xml
# php-fpm php-cli php-opcache already installed in base image
# php-xmlrpc available in pecl after php8.0
ARG ARG_INSTALL_MOODLE_PHP_PKGS="php-gd php-intl php-ldap php-pgsql php-soap php-xml php-pecl-zip php-mbstring php-json"
ENV INSTALL_MOODLE_PHP_PKGS=${ARG_INSTALL_MOODLE_PHP_PKGS}
RUN install-pkgs unzip ${INSTALL_MOODLE_PHP_PKGS}

# Install extra packages (a space separated list)
ARG ARG_INSTALL_EXTRA_PKGS="php-sodium php-pecl-redis5 php-pecl-apcu poppler-utils graphviz aspell"
ENV INSTALL_EXTRA_PKGS=${ARG_INSTALL_EXTRA_PKGS}
RUN if [ -n "${INSTALL_EXTRA_PKGS}" ]; then install-pkgs -n -e -r crb ${INSTALL_EXTRA_PKGS}; fi

# Other OS moodle config
RUN container-setup-php-moodle

USER ${CTR_USER_ID}

ARG ARG_MOODLE_PLUGIN_LIST=""
ARG ARG_MOODLE_REMOTE="https://github.com/moodle/moodle.git"
ARG ARG_MOODLE_BRANCH="MOODLE_401_STABLE"
ARG ARG_MOODLE_COMMIT="94ad185d09030a7b0096acd79c66af52a2b16e26"
ARG ARG_MOODLE_VERSION_NUMBER="2022112806.06"
ENV MOODLE_REMOTE=${ARG_MOODLE_REMOTE} \
    MOODLE_BRANCH=${ARG_MOODLE_BRANCH} \
    MOODLE_COMMIT=${ARG_MOODLE_COMMIT} \
    MOODLE_VERSION_NUMBER=${ARG_MOODLE_VERSION_NUMBER} \
    MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST}

COPY --chown=${CTR_USER_ID}:${CTR_GROUP_ID:-0} --from=app-src /var/www/html/ /var/www/html

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="4.1.6" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_OC_TAGS}"
