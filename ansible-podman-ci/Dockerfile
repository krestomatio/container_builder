# Ansible managed
FROM quay.io/krestomatio/ansible

# General variables
ENV IMAGE_NAME=ansible-podman-ci \
    IMAGE_SUMMARY="Podman image based on CentOS 8 Stream minimal for Continuous Integration" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image with tools like Buildah and Skopeo, for CI" \
    IMAGE_TITLE="Ansible CI image based on CentOS 8 Stream minimal"

ENV BUILDAH_ISOLATION=chroot \
    BUILDAH_LAYERS=true \
    CONTAINER_BUILDER=podman

RUN echo "Installing podman..."  && \
    $CTR_PKG_MGM install xz gzip tar podman skopeo buildah && \
    rpm -e --nodeps container-selinux && \
    echo "Cleaning..."  && \
    $CTR_PKG_MGM clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.*

COPY conf/etc/containers/containers.conf /etc/containers/containers.conf

ENV ORAS_VERSION="0.10.0"
RUN echo "Installing oras version: ${ORAS_VERSION}..."  && \
    pushd /tmp && \
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_amd64.tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    popd

ENV PUSHRM_VERSION="1.7.0"
RUN echo "Installing pushrm version: ${PUSHRM_VERSION}..."  && \
    curl -L "https://github.com/christian-korneck/docker-pushrm/releases/download/v${PUSHRM_VERSION}/docker-pushrm_linux_amd64" -o /usr/local/bin/docker-pushrm && \
    chmod +x /usr/local/bin/docker-pushrm

CMD [ "/bin/bash" ]

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.9.*,podman"
