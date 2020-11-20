# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=nginx \
    IMAGE_summary="Nginx 1.14" \
    IMAGE_description="This CentOS 8 minimal based container image runs Nginx 1.14" \
    IMAGE_title="Nginx 1.14" \
    IMAGE_service_port="8080" \
    IMAGE_service_name="http"

# Container variables
ENV CTR_user=nginx \
    CTR_user_id="998" \
    CTR_stopsignal=SIGQUIT

# Component bash variables
ENV NGINX_version="1.14" \
    NGINX_ver_short="114" \
    NGINX_sysconf_path=/etc/nginx \
    NGINX_main_conf_file=/etc/nginx/nginx.conf \
    NGINX_main_conf_d_path=/etc/nginx/conf.d \
    NGINX_default_conf_d_path=/etc/nginx/default.d \
    NGINX_default_conf_root_file="/etc/nginx/default.d/root.conf" \
    NGINX_default_conf_app_file="/etc/nginx/default.d/app.conf" \
    NGINX_var_run_path=/var/run \
    NGINX_lib_path=/var/lib/nginx \
    NGINX_port=${IMAGE_service_port} \
    NGINX_log_path=/var/log/nginx \
    APP_dest=/usr/share/nginx/html

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs nginx

RUN container-setup-nginx

WORKDIR ${APP_dest}

USER ${CTR_user_id}

STOPSIGNAL ${CTR_stopsignal}

EXPOSE ${NGINX_port}

CMD ["nginx", "-g", "daemon off;"]

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="0.0.7" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.expose-services="${IMAGE_service_port}:${IMAGE_service_name}" \
      io.openshift.tags="${IMAGE_name},nginx,nginx-${NGINX_ver_short},nginx${NGINX_ver_short}"
