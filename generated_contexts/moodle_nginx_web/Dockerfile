# Ansible managed
FROM quay.io/krestomatio/nginx_php-fpm

# General variables
ENV IMAGE_name="moodle_nginx" \
    IMAGE_summary="Nginx ${NGINX_version} for Moodle 3.9" \
    IMAGE_description="This CentOS 8 minimal based container image runs Nginx ${NGINX_version} for Moodle 3.9" \
    IMAGE_title="Nginx ${NGINX_version} for Moodle 3.9" \
    TZ="UTC"

# Component bash variables
ENV APP_dest=/var/www/html

ENV MOODLE_version="3.9" \
    MOODLE_ver_short="39" \
    MOODLE_commit="621cd70b4c5b79c2fa33f7ff84c9b8a435fcabbd" \
    MOODLE_app=${APP_dest} \
    MOODLE_data=/var/moodledata \
    MOODLE_check_path=/login/index.php \
    MOODLE_check_code="200" \
    MOODLE_check_host=localhost

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/usr/libexec/* /usr/libexec/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup

RUN container-setup-nginx-moodle

USER ${CTR_user_id}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="0.0.3" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_name},nginx,nginx${NGINX_ver_short},nginx-${NGINX_ver_short},moodle,moodle${MOODLE_ver_short},moodle-${MOODLE_ver_short}"
