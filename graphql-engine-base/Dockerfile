# Ansible managed
FROM quay.io/krestomatio/base-stream

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 \
    GRAPHQL_ENGINE_VERSION="2.0.9" \
    POSTGRES_MAJOR_VERSION="13"

RUN microdnf module enable postgresql:${POSTGRES_MAJOR_VERSION} && \
    install-pkgs libpq unixODBC mysql-libs
