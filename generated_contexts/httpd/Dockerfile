# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=httpd \
    IMAGE_summary="Apache 2.4" \
    IMAGE_description="This CentOS 8 minimal based container image runs Apache 2.4" \
    IMAGE_title="Apache 2.4" \
    IMAGE_service_port="8080" \
    IMAGE_service_name="http"

# Container variables
ENV CTR_user=apache \
    CTR_user_id="48" \
    CTR_cmd="httpd -D FOREGROUND" \
    CTR_stopsignal=SIGWINCH

# Component bash variables
ENV HTTPD_version="2.4" \
    HTTPD_ver_short="24" \
    HTTPD_main_conf_path=/etc/httpd/conf \
    HTTPD_main_conf_file=/etc/httpd/conf/httpd.conf \
    HTTPD_main_conf_d_path=/etc/httpd/conf.d \
    HTTPD_modules_conf_d_path=/etc/httpd/conf.modules.d \
    HTTPD_var_run_path=/var/run/httpd \
    HTTPD_port=${IMAGE_service_port} \
    HTTPD_log_path=/var/log/httpd \
    APP_dest=/var/www/html

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs httpd

RUN container-setup-httpd

WORKDIR ${APP_dest}

USER ${CTR_user_id}

STOPSIGNAL ${CTR_stopsignal}

EXPOSE ${HTTPD_port}

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
      io.openshift.tags="${IMAGE_name},apache,apache-${HTTPD_ver_short},apache${HTTPD_ver_short}"
