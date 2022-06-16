# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/moodle_nginx_php-fpm
FROM ${ARG_IMAGE_FROM} AS app-src

# Component bash variables
ENV GIT_DEST="/opt/app/" \
    APP_DEST=/var/www/html

USER 0
WORKDIR ${GIT_DEST}

# Install deps
COPY conf/usr/bin /usr/bin/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/
RUN install-pkgs git rsync php-json unzip && \
    mkdir -p ${GIT_DEST} ${APP_DEST}

# Get source code
# Arguments for moodle git remote, branch and commit
# They are also a mechanism to invalidate cache if changed
ARG ARG_GIT_REMOTE="https://github.com/moodle/moodle.git"
ARG ARG_GIT_BRANCH="MOODLE_39_STABLE"
ARG ARG_GIT_COMMIT=""
ENV GIT_REMOTE=${ARG_GIT_REMOTE} \
    GIT_BRANCH=${ARG_GIT_BRANCH} \
    GIT_COMMIT=${ARG_GIT_COMMIT}
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
ENV MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST}
RUN if [ -n "${MOODLE_PLUGIN_LIST}" ]; then /usr/libexec/moodle/install-plugin-list -p "${MOODLE_PLUGIN_LIST}"; fi

ARG ARG_IMAGE_FROM=quay.io/krestomatio/moodle_nginx_php-fpm
FROM ${ARG_IMAGE_FROM} AS php-redis-builder

USER 0

RUN install-pkgs php-pear php-devel make libzstd-devel
RUN pecl install -D 'enable-redis-igbinary="yes" enable-redis-lzf="yes" enable-redis-zstd="yes"' igbinary redis
RUN chmod 755 /usr/lib64/php/modules/{redis.so,igbinary.so}

ARG ARG_IMAGE_FROM=quay.io/krestomatio/moodle_nginx_php-fpm
FROM ${ARG_IMAGE_FROM}

# General ansible variables
ENV IMAGE_NAME=moodle \
    IMAGE_SUMMARY="PHP $PHP_VERSION and NGINX ${NGINX_VERSION} for Moodle 3.9" \
    IMAGE_DESCRIPTION="This CentOS 8 Stream minimal based container image runs PHP ${PHP_VERSION} or NGINX ${NGINX_VERSION} for Moodle 3.9" \
    IMAGE_TITLE="PHP ${PHP_VERSION} and NGINX ${NGINX_VERSION} for Moodle 3.9" \
    IMAGE_OC_TAGS="${IMAGE_NAME},php,php-fpm,php${PHP_VER_SHORT},php-${PHP_VER_SHORT},nginx,nginx-${NGINX_VER_SHORT},nginx${NGINX_VER_SHORT},moodle,moodle${MOODLE_VER_SHORT},moodle-${MOODLE_VER_SHORT}" \
    TZ="UTC" \
    LANG="en_AU.UTF-8"

# Component bash variables
ENV MOODLE_VERSION="3.9" \
    MOODLE_VERSION_SHORT="39" \
    MOODLE_APP=${APP_DEST} \
    MOODLE_DATA=/var/moodledata \
    MOODLE_CLI_TOOLS=/usr/libexec/moodle

USER 0

COPY conf/usr/bin /usr/bin/
COPY conf/usr/libexec /usr/libexec/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/
COPY --from=php-redis-builder /usr/lib64/php/modules/redis.so /usr/lib64/php/modules/redis.so
COPY --from=php-redis-builder /usr/lib64/php/modules/igbinary.so /usr/lib64/php/modules/igbinary.so

# Install all locales and timezones
RUN locale-tz-all

# Install dependencies:
# php-curl included in php-common
# php-zip as php-pecl-zip
# php-xsl as php-xml
# php-fpm php-cli php-opcache already installed in base image
ARG ARG_INSTALL_MOODLE_PHP_PKGS="php-gd php-intl php-ldap php-pgsql php-soap php-xmlrpc php-xml php-pecl-zip php-mbstring php-json"
ENV INSTALL_MOODLE_PHP_PKGS=${ARG_INSTALL_MOODLE_PHP_PKGS}
RUN install-pkgs unzip ${INSTALL_MOODLE_PHP_PKGS}

# Install extra packages (a space separated list)
ARG ARG_INSTALL_EXTRA_PKGS=""
ENV INSTALL_EXTRA_PKGS=${ARG_INSTALL_EXTRA_PKGS}
RUN if [ -n "${INSTALL_EXTRA_PKGS}" ]; then install-pkgs "${INSTALL_EXTRA_PKGS}"; fi

# Other OS moodle config
RUN container-setup-php-moodle

USER ${CTR_USER_ID}

ARG ARG_MOODLE_PLUGIN_LIST=""
ARG ARG_MOODLE_COMMIT=""
ENV MOODLE_COMMIT=${ARG_MOODLE_COMMIT} \
    MOODLE_VERSION_NUMBER="2020061514.02" \
    MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST}

COPY --chown=${CTR_USER_ID}:${CTR_GROUP_ID:-0} --from=app-src /var/www/html/ /var/www/html

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
