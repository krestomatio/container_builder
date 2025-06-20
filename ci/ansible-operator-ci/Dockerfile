# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/ansible-podman-ci
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=ansible-operator-ci \
    IMAGE_SUMMARY="Ansible Operator SDK image based on CentOS 9 Stream minimal for Continuous Integration" \
    IMAGE_DESCRIPTION="CentOS 9 Stream minimal based image with Ansible Operator SDK" \
    IMAGE_TITLE="Ansible Operator SDK CI image based on CentOS 9 Stream minimal"

# Container variables
ENV LOCALBIN=/usr/local/bin \
    GOBIN=/usr/local/bin \
    GO_VERSION="1.22" \
    OPERATOR_VERSION="1.39.1" \
    ANSIBLE_OPERATOR_VERSION="1.37.1" \
    SETUP_ENVTEST_VERSION="0.19" \
    CONTROLLER_TOOLS_VERSION="0.16.1" \
    GO_LINT_VERSION="1.57.2" \
    CRD_REF_DOCS_VERSION="0.0.12"

# Install Go
RUN install-pkgs go-toolset git make tar which curl; \
    [[ "$(go version | { read _ _ v _; echo ${v#go}; })" == "${GO_VERSION}".* ]] || echo "error: version differs from env var"; \
    go install sigs.k8s.io/controller-runtime/tools/setup-envtest@release-${SETUP_ENVTEST_VERSION}; \
    go install sigs.k8s.io/controller-tools/cmd/controller-gen@v${CONTROLLER_TOOLS_VERSION}; \
    go install github.com/golangci/golangci-lint/cmd/golangci-lint@v${GO_LINT_VERSION}; \
    go install github.com/elastic/crd-ref-docs@v${CRD_REF_DOCS_VERSION}

# Container variables
ENV OPM_VERSION="1.23.0"

# Install opm
RUN echo "Installing opm version: ${OPM_VERSION}..."; \
    curl -sSLo ${LOCALBIN}/opm https://github.com/operator-framework/operator-registry/releases/download/v${OPM_VERSION}/linux-$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')-opm; \
    chmod +x ${LOCALBIN}/opm

# Install docker cli
RUN echo "Installing docker repo..."  && \
    curl -o /etc/yum.repos.d/docker-ce.repo https://download.docker.com/linux/centos/docker-ce.repo && \
    $CTR_PKG_MGM install docker-ce-cli docker-buildx-plugin docker-compose-plugin

# Install Operator SDK
COPY --from=quay.io/operator-framework/operator-sdk:v1.39.1 ${LOCALBIN}/operator-sdk ${LOCALBIN}/operator-sdk

# Install Ansible Operator
COPY --from=quay.io/operator-framework/ansible-operator:v1.37.1 ${LOCALBIN}/ansible-operator ${LOCALBIN}/ansible-operator

# Container variables
ENV KUSTOMIZE_VERSION="5.4.3"

# Install kustomize
RUN echo "Installing kustomize version: ${KUSTOMIZE_VERSION}..."  && \
    curl -sSLo - https://github.com/kubernetes-sigs/kustomize/releases/download/kustomize/v${KUSTOMIZE_VERSION}/kustomize_v${KUSTOMIZE_VERSION}_linux_$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/').tar.gz | tar xzf - -C ${LOCALBIN}/

# Container variables
ENV KUBECTL_VERSION="1.29.3"

# Install kubectl.
RUN echo "Installing kubectl version: ${KUBECTL_VERSION}..."  && \
    curl -L https://storage.googleapis.com/kubernetes-release/release/v${KUBECTL_VERSION}/bin/linux/$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')/kubectl -o ${LOCALBIN}/kubectl && \
    chmod +x ${LOCALBIN}/kubectl

# Install requirements.
RUN echo "Installing ansible operator plugin version: ${ANSIBLE_OPERATOR_VERSION} requirements..."  && \
    curl -L https://raw.githubusercontent.com/operator-framework/ansible-operator-plugins/v${ANSIBLE_OPERATOR_VERSION}/testdata/memcached-molecule-operator/requirements.yml -o /tmp/requirements.yml && \
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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.18.*,ansible-operator,ansible-operator1.37.1,operator-version1.39.1"
