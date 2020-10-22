# Ansible managed
FROM quay.io/krestomatio/moodle_app AS app
RUN app-git -a -e '.git*'

FROM quay.io/krestomatio/moodle_nginx_web

# General ansible variables
ENV IMAGE_name=moodle_nginx_web \
    IMAGE_summary="PHP $PHP_version and NGINX ${NGINX_version} for Moodle" \
    IMAGE_description="This CentOS 8 minimal based container image runs PHP ${PHP_version} and NGINX ${NGINX_version} for Moodle" \
    IMAGE_title="PHP ${PHP_version} and NGINX ${NGINX_version} for Moodle" \
    IMAGE_oc_tags="${IMAGE_name},php,php-fpm,php${PHP_ver_short},php-${PHP_ver_short},nginx,nginx-${NGINX_ver_short},nginx${NGINX_ver_short},moodle,moodle${MOODLE_ver_short},moodle-${MOODLE_ver_short}" \
    TZ="UTC"

# Component bash variables
ENV MOODLE_version="3.9" \
    MOODLE_ver_short="39" \
    MOODLE_commit="4d9ab4ca4825d689dcd49767c101eb5139705f33" \
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

COPY --from=app /var/www/html /var/www/html

RUN container-setup-php-moodle

USER ${CTR_user_id}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="3.9.2-4d9ab" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_oc_tags}"
