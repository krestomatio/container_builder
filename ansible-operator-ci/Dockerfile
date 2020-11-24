# Ansible managed
FROM quay.io/krestomatio/ansible-podman-ci

# General variables
ENV IMAGE_NAME=ansible-operator-ci \
    IMAGE_SUMMARY="Ansible Operator SDK image based on CentOS 8 minimal for Continuous Integration" \
    IMAGE_DESCRIPTION="CentOS 8 minimal based image with Ansible Operator SDK" \
    IMAGE_TITLE="Ansible Operator SDK CI image based on CentOS 8 minimal"

# Container variables
ENV OPERATOR_VERSION="1.1.0"

# Install Operator SDK
COPY --from=quay.io/operator-framework/operator-sdk:v1.1.0 /usr/local/bin/operator-sdk /usr/local/bin/operator-sdk

# Install Ansible Operator
COPY --from=quay.io/operator-framework/ansible-operator:v1.1.0 /usr/local/bin/ansible-operator /usr/local/bin/ansible-operator

# Container variables
ENV KUSTOMIZE_VERSION="3.5.4"

# Install kustomize
RUN echo "Installing kustomize version: ${ORAS_VERSION}..."  && \
    curl -sSLo - https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_amd64.tar.gz | tar xzf - -C /usr/local/bin/

# Container variables
ENV KUBECTL_VERSION="1.19.3"

# Install kubectl.
COPY --from=lachlanevenson/k8s-kubectl:v1.19.3 /usr/local/bin/kubectl /usr/local/bin/kubectl

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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.9.*,ansible-operator,ansible-operator1.1.0"
