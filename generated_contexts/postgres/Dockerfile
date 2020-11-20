# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=postgres \
    IMAGE_summary="Postgres 10" \
    IMAGE_description="This CentOS 8 minimal based container image runs Postgres 10. \
It follows https://github.com/sclorg/postgresql-container" \
    IMAGE_title="Postgres 10" \
    IMAGE_service_port="5432" \
    IMAGE_service_name="postgres" \
    TZ="UTC"

# Container variables
ENV CTR_locale_id=${IMAGE_locale_id} \
    CTR_user=postgres \
    CTR_user_id="26" \
    CTR_home=/var/lib/pgsql \
    CTR_cmd="run-postgresql" \
    CTR_scripts_path=/usr/share/container-scripts/postgresql

# Component bash variables
ENV POSTGRES_version="10" \
    POSTGRES_ver_short="10" \
    POSTGRES_prev_version="9.6" \
    POSTGRES_port=${IMAGE_service_port} \
    POSTGRES_run=/var/run/postgresql \
    POSTGRES_home=${CTR_home} \
    POSTGRES_data="${CTR_home}/data"

# Frequent environment variables
ENV HOME="${CTR_home}" \
    PGUSER="$CTR_user" \
    LANG="es_CR.UTF-8"

ENV OS_install_pkgs="postgresql-server postgresql-contrib gettext nss_wrapper"

USER 0

COPY conf/usr /usr/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs ${OS_install_pkgs}

RUN container-setup-postgres

WORKDIR ${CTR_home}

USER ${CTR_user_id}

EXPOSE ${POSTGRES_port}

CMD ${CTR_cmd}

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
      io.openshift.tags="${IMAGE_name},postgres,postgres-${POSTGRES_ver_short},postgres${POSTGRES_ver_short}"
