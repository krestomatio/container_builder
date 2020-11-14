# Ansible managed
FROM quay.io/krestomatio/nginx

# General variables
ENV IMAGE_name=php-fpm \
    IMAGE_summary="PHP 7.2" \
    IMAGE_description="This CentOS 8 minimal based container image runs PHP 7.2" \
    IMAGE_title="PHP 7.2" \
    IMAGE_service_port="9000" \
    IMAGE_service_name="php-fpm"

# Container variables
ENV CTR_user=apache \
    CTR_user_id="48" \
    CTR_cmd="php-fpm" \
    CTR_stopsignal=SIGQUIT

# Component bash variables
ENV PHP_version="7.2" \
    PHP_ver_short="72" \
    PHP_run=/var/run/php-fpm \
    PHP_conf_dir=/etc/php.d \
    PHP_conf_file=/etc/php.ini \
    PHP_module_dir=/usr/lib64/php/modules/ \
    PHP_FPM_conf_dir=/etc/php-fpm.d \
    PHP_FPM_conf_file=/etc/php-fpm.conf \
    PHP_FPM_pool_file=/etc/php-fpm.d/www.conf \
    PHP_FPM_port=${IMAGE_service_port} \
    APP_dest=/var/www/html

ENV OS_install_pkgs="php-fpm php-cli php-opcache php-soap"

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs ${OS_install_pkgs}

RUN container-setup-php

WORKDIR ${APP_dest}

USER ${CTR_user_id}

STOPSIGNAL ${CTR_stopsignal}

EXPOSE ${PHP_FPM_port}

CMD ${CTR_cmd}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="0.0.5" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.expose-services="${IMAGE_service_port}:${IMAGE_service_name}" \
      io.openshift.tags="${IMAGE_name},php,php${PHP_ver_short},php-${PHP_ver_short}"
