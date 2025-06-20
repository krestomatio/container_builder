# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:10-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=pgbouncer \
    IMAGE_SUMMARY="PgBouncer" \
    IMAGE_DESCRIPTION="This CentOS 10 Stream minimal based container image runs PgBouncer" \
    IMAGE_TITLE="PgBouncer" \
    IMAGE_SERVICE_PORT="5432" \
    IMAGE_SERVICE_NAME="postgres" \
    TZ="UTC"

# Container variables
ENV CTR_USER=pgbouncer \
    CTR_USER_ID="1001" \
    CTR_USER_GECOS="PgBouncer Server" \
    CTR_HOME=/opt/pgbouncer \
    CTR_CMD="pgbouncer /etc/pgbouncer/pgbouncer.ini" \
    CTR_SCRIPTS_PATH=/usr/share/container-scripts/postgresql \
    CTR_STOPSIGNAL=SIGINT

# Component bash variables
ENV POSTGRES_VERSION="16" \
    POSTGRES_PORT=${IMAGE_SERVICE_PORT} \
    PGBOUNCER_PORT=${IMAGE_SERVICE_PORT} \
    PGBOUNCER_ADMIN_USER=pgbouncer \
    PGBOUNCER_AUTH_TYPE=md5 \
    PGBOUNCER_LISTEN_ADDR=* \
    PGBOUNCER_STATS_USERS="stats, pgbouncer" \
    PGBOUNCER_RUN_DIR=/var/run/pgbouncer \
    PGBOUNCER_PID_FILE=/var/run/pgbouncer/pgbouncer.pid \
    PGBOUNCER_CONFIG_DIR=/etc/pgbouncer/ \
    PGBOUNCER_CONFIG_FILE=/etc/pgbouncer/pgbouncer.ini \
    PGBOUNCER_EXTRA_CONFIG_FILE=/etc/pgbouncer/pgbouncer-extra.ini \
    PGBOUNCER_EXTRA_USERS_CONFIG_FILE=/etc/pgbouncer/pgbouncer-extra-users.ini \
    PGBOUNCER_EXTRA_DATABASES_CONFIG_FILE=/etc/pgbouncer/pgbouncer-extra-databases.ini \
    PGBOUNCER_USERS_FILE=/etc/pgbouncer/userlist.txt

# Frequent environment variables
ENV HOME="${CTR_HOME}" \
    LANG="en_US.UTF-8"

ENV OS_INSTALL_PKGS="postgresql procps-ng psmisc"

USER 0

COPY conf/usr /usr/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

RUN container-setup && container-setup-pgbouncer

WORKDIR ${CTR_HOME}

USER ${CTR_USER_ID}

STOPSIGNAL ${CTR_STOPSIGNAL}

EXPOSE ${PGBOUNCER_PORT}

CMD ${CTR_CMD}

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="0.5.12" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},postgres,postgres-${POSTGRES_VERSION},postgres${POSTGRES_VERSION}"
