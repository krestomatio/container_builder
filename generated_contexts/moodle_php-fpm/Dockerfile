# Ansible managed
FROM quay.io/krestomatio/php-fpm

# General ansible variables
ENV IMAGE_name=moodle_php-fpm \
    IMAGE_summary="PHP $PHP_version for Moodle" \
    IMAGE_description="This CentOS 8 minimal based container image runs PHP ${PHP_version} for Moodle" \
    IMAGE_title="PHP ${PHP_version} for Moodle" \
    IMAGE_oc_tags="${IMAGE_name},php,php-fpm,php${PHP_ver_short},php-${PHP_ver_short},moodle,moodle${MOODLE_ver_short},moodle-${MOODLE_ver_short}" \
    TZ="UTC"

# Component bash variables
ENV MOODLE_version="3.9" \
    MOODLE_ver_short="39" \
    MOODLE_commit="5ea37637b7c0ac4f3c7ccddccd4f82ba9a1b86bd" \
    MOODLE_app=${APP_dest} \
    MOODLE_data=/var/moodledata

# php-curl included in php-common
# php-zip as php-pecl-zip
# php-xsl as php-xml
# php-fpm php-cli php-opcache already installed in base image
ENV MOODLE_install_php_pkgs="php-gd php-intl php-ldap php-pgsql php-soap php-xmlrpc php-xml php-pecl-zip php-mbstring php-json"

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/usr/libexec/* /usr/libexec/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs ${MOODLE_install_php_pkgs}

RUN container-setup-php-moodle

USER ${CTR_user_id}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="0.0.1" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_oc_tags}"
