# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_NAME=nginx \
    IMAGE_SUMMARY="Nginx 1.14" \
    IMAGE_DESCRIPTION="This CentOS 8 minimal based container image runs Nginx 1.14" \
    IMAGE_TITLE="Nginx 1.14" \
    IMAGE_SERVICE_PORT="8080" \
    IMAGE_SERVICE_NAME="http"

# Container variables
ENV CTR_USER=nginx \
    CTR_USER_ID="998" \
    CTR_STOPSIGNAL=SIGQUIT

# Component bash variables
ENV NGINX_VERSION="1.14" \
    NGINX_VER_SHORT="114" \
    NGINX_SYSCONF_PATH=/etc/nginx \
    NGINX_MAIN_CONF_FILE=/etc/nginx/nginx.conf \
    NGINX_MAIN_CONF_D_PATH=/etc/nginx/conf.d \
    NGINX_DEFAULT_CONF_D_PATH=/etc/nginx/default.d \
    NGINX_DEFAULT_CONF_ROOT_FILE="/etc/nginx/default.d/root.conf" \
    NGINX_DEFAULT_CONF_APP_FILE="/etc/nginx/default.d/app.conf" \
    NGINX_VAR_RUN_PATH=/var/run \
    NGINX_LIB_PATH=/var/lib/nginx \
    NGINX_PORT=${IMAGE_SERVICE_PORT} \
    NGINX_LOG_PATH=/var/log/nginx \
    APP_DEST=/usr/share/nginx/html

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup
RUN install-pkgs nginx

RUN container-setup-nginx

WORKDIR ${APP_DEST}

USER ${CTR_USER_ID}

STOPSIGNAL ${CTR_STOPSIGNAL}

EXPOSE ${NGINX_PORT}

CMD ["nginx", "-g", "daemon off;"]

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="0.1" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},nginx,nginx-${NGINX_VER_SHORT},nginx${NGINX_VER_SHORT}"
