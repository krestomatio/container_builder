# Ansible managed
FROM quay.io/krestomatio/ansible

# General variables
ENV IMAGE_name=ansible-podman-ci \
    IMAGE_summary="Podman image based on CentOS 8 minimal for Continuous Integration" \
    IMAGE_description="CentOS 8 minimal based image with tools like Buildah and Skopeo, for CI" \
    IMAGE_title="Ansible CI image based on CentOS 8 minimal"

ENV BUILDAH_ISOLATION chroot

RUN echo "Installing podman..."  && \
    $CTR_pkg_mgm install xz gzip tar podman skopeo buildah && \
    rpm -e --nodeps container-selinux && \
    echo "Cleaning..."  && \
    $CTR_pkg_mgm clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.*

COPY conf/etc/containers/containers.conf /etc/containers/containers.conf

ENV ORAS_VERSION="0.8.1"
RUN echo "Installing oras version: ${ORAS_VERSION}..."  && \
    pushd /tmp && \
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_amd64.tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    popd

CMD [ "/bin/bash" ]

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      description="${IMAGE_description}" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_description}" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_name},ansible,ansible2.9.*,podman"
