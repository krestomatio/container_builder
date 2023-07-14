# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/ansible-podman-ci
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=ansible-operator-ci \
    IMAGE_SUMMARY="Ansible Operator SDK image based on CentOS 8 Stream minimal for Continuous Integration" \
    IMAGE_DESCRIPTION="CentOS 8 Stream minimal based image with Ansible Operator SDK" \
    IMAGE_TITLE="Ansible Operator SDK CI image based on CentOS 8 Stream minimal"

# Container variables
ENV OPERATOR_VERSION="1.21.0"

# Install Operator SDK
COPY --from=quay.io/operator-framework/operator-sdk:v1.21.0 /usr/local/bin/operator-sdk /usr/local/bin/operator-sdk

# Install Ansible Operator
COPY --from=quay.io/operator-framework/ansible-operator:v1.21.0 /usr/local/bin/ansible-operator /usr/local/bin/ansible-operator

# Container variables
ENV KUSTOMIZE_VERSION="4.1.3"

# Install kustomize
RUN echo "Installing kustomize version: ${KUSTOMIZE_VERSION}..."  && \
    curl -sSLo - https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/').tar.gz | tar xzf - -C /usr/local/bin/

# Container variables
ENV KUBECTL_VERSION="1.26.6"

# Install kubectl.
RUN echo "Installing kubectl version: ${KUBECTL_VERSION}..."  && \
    curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')/kubectl -o /usr/local/bin/kubectl && \
    chmod +x /usr/local/bin/kubectl

# Install requirements.
RUN echo "Installing operator sdk version: ${OPERATOR_VERSION}..."  && \
    curl -L https://raw.githubusercontent.com/operator-framework/operator-sdk/v${OPERATOR_VERSION}/testdata/ansible/memcached-operator/requirements.yml -o /tmp/requirements.yml && \
    ansible-galaxy collection install -r /tmp/requirements.yml -p /usr/share/ansible/collections && \
    rm -f /tmp/requirements.yml

CMD [ "/bin/bash" ]

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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.9.*,ansible-operator,ansible-operator1.21.0"
