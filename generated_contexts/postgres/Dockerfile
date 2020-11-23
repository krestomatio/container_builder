# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_NAME=postgres \
    IMAGE_SUMMARY="Postgres 10" \
    IMAGE_DESCRIPTION="This CentOS 8 minimal based container image runs Postgres 10. \
It follows https://github.com/sclorg/postgresql-container" \
    IMAGE_TITLE="Postgres 10" \
    IMAGE_SERVICE_PORT="5432" \
    IMAGE_SERVICE_NAME="postgres" \
    TZ="UTC"

# Container variables
ENV CTR_USER=postgres \
    CTR_USER_ID="26" \
    CTR_HOME=/var/lib/pgsql \
    CTR_CMD="run-postgresql" \
    CTR_SCRIPTS_PATH=/usr/share/container-scripts/postgresql

# Component bash variables
ENV POSTGRES_VERSION="10" \
    POSTGRES_VER_SHORT="10" \
    POSTGRES_PREV_VERSION="9.6" \
    POSTGRES_PORT=${IMAGE_SERVICE_PORT} \
    POSTGRES_RUN=/var/run/postgresql \
    POSTGRES_HOME=${CTR_HOME} \
    POSTGRES_DATA="${CTR_HOME}/data"

# Frequent environment variables
ENV HOME="${CTR_HOME}" \
    PGUSER="$CTR_USER" \
    LANG="es_CR.UTF-8"

ENV OS_INSTALL_PKGS="postgresql-server postgresql-contrib gettext nss_wrapper"

USER 0

COPY conf/usr /usr/
COPY conf/container-entrypoint.d/* ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup
RUN install-pkgs ${OS_INSTALL_PKGS}

RUN container-setup-postgres

WORKDIR ${CTR_HOME}

USER ${CTR_USER_ID}

EXPOSE ${POSTGRES_PORT}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="0.0.9+5219095" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},postgres,postgres-${POSTGRES_VER_SHORT},postgres${POSTGRES_VER_SHORT}"
