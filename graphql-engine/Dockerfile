# Ansible managed
FROM quay.io/krestomatio/graphql-engine-base

# General variables
ENV IMAGE_NAME=graphql-engine \
    IMAGE_SUMMARY="Graphql-engine image based on CentOS 8 Stream minimal" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image" \
    IMAGE_TITLE="Graphql-engine image based on CentOS 8 Stream minimal"

# Container variables
ENV CTR_USER=hasura \
    CTR_USER_ID="1001"

COPY --from=quay.io/krestomatio/graphql-engine-build:2.0.9 /bin/graphql-engine /bin/graphql-engine

COPY --from=quay.io/krestomatio/graphql-engine-build:2.0.9 /usr/bin/pg_dump /usr/bin/pg_dump

COPY --from=hasura/graphql-engine:v2.0.9 /srv/ /srv

RUN containeruser-create

USER ${CTR_USER_ID}

CMD ["graphql-engine", "serve"]

# Labels
LABEL name="${IMAGE_NAME}" \
    summary="${IMAGE_SUMMARY}" \
    maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
    description="${IMAGE_DESCRIPTION}" \
    org.opencontainers.image.title="${IMAGE_TITLE}" \
    org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
    org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
    io.k8s.description="${IMAGE_DESCRIPTION}" \
    io.k8s.display-name="${IMAGE_TITLE}" \
    io.openshift.tags="${IMAGE_NAME},graphql-engine,graphql-engine-2.0.9"
