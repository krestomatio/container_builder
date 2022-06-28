# Ansible managed
ARG ARG_IMAGE_FROM=docker:20-dind
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=ansible-docker-ci \
    IMAGE_SUMMARY="Ansible image based on Docker 20-dind for Continuous Integration" \
    IMAGE_DESCRIPTION="Docker 20-dind based image with Ansible and tools like Docker, Skopeo and Molecule, for CI" \
    IMAGE_TITLE="Ansible CI image based on Docker 20-dind"

# Container variables
ENV ANSIBLE_VERSION="2.9.*" \
    MOLECULE_VERSION="3.1.*" \
    CTR_APK="apk add --update --no-cache" \
    CTR_PIP="pip install --no-cache --upgrade" \
    CONTAINER_BUILDER=docker

RUN echo "Build tools..."  && \
    $CTR_APK py-pip openssl ca-certificates make && \
    $CTR_APK --virtual build-dependencies python3-dev \
        libffi-dev openssl-dev build-base gcc musl-dev cargo rust && \
    $CTR_PIP cffi wheel && \
    $CTR_PIP pip && \
    $CTR_PIP ansible==$ANSIBLE_VERSION && \
    $CTR_PIP molecule==$MOLECULE_VERSION && \
    echo "Installing aditional python tools..."  && \
    $CTR_PIP yamllint ansible-lint'<6' pycrypto pywinrm docker git-semver commitizen jmespath && \
    echo "Cleaning..."  && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

RUN echo "Installing other tools..."  && \
    $CTR_APK bash xz gzip tar git git-lfs rsync jq sudo sshpass openssh-client skopeo curl coreutils && \
    echo "Cleaning..."  && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache

RUN sed -i "s@bin/ash@bin/bash@" /etc/passwd && \
    ln -svf bash /bin/sh

ENV ORAS_VERSION="0.12.0"
RUN echo "Installing oras version: ${ORAS_VERSION}..."  && \
    cd /tmp && \
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/').tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    cd /

ENV PUSHRM_VERSION="1.8.1"
RUN echo "Installing pushrm version: ${PUSHRM_VERSION}..."  && \
    curl -L "https://github.com/christian-korneck/docker-pushrm/releases/download/v${PUSHRM_VERSION}/docker-pushrm_linux_$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')" -o /usr/local/bin/docker-pushrm && \
    chmod +x /usr/local/bin/docker-pushrm

ENV BUILDX_VERSION="0.8.2"
RUN echo "Installing buildx version: ${BUILDX_VERSION}..."  && \
    mkdir -p /usr/local/lib/docker/cli-plugins && \
    curl -L "https://github.com/docker/buildx/releases/download/v${BUILDX_VERSION}/buildx-v${BUILDX_VERSION}.linux-$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/')" -o /usr/local/lib/docker/cli-plugins/docker-buildx && \
    chmod +x /usr/local/lib/docker/cli-plugins/docker-buildx

ENV TERRAFORM_VERSION="1.2.3"
RUN echo "Installing terraform version: ${TERRAFORM_VERSION}..."  && \
    cd /tmp && \
    curl -L "https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_$(uname -m | sed 's/x86_64/amd64/' | sed 's/aarch64/arm64/').zip" -o /tmp/terraform.zip && \
    unzip -q /tmp/terraform.zip && \
    mv terraform /usr/local/bin/terraform && \
    chmod +x /usr/local/bin/terraform && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    cd /

CMD [ "ansible-playbook", "--version" ]

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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.9.*,docker,docker20-dind"
