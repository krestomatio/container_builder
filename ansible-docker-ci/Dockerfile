# Ansible managed
FROM docker:stable-dind

# General variables
ENV IMAGE_NAME=ansible-docker-ci \
    IMAGE_SUMMARY="Ansible image based on Docker stable-dind for Continuous Integration" \
    IMAGE_DESCRIPTION="Docker stable-dind based image with Ansible and tools like Docker, Skopeo and Molecule, for CI" \
    IMAGE_TITLE="Ansible CI image based on Docker stable-dind"

# Container variables
ENV ANSIBLE_VERSION="2.9.*" \
    MOLECULE_VERSION="3.1.*" \
    CTR_APK="apk add --update --no-cache" \
    CTR_PIP="pip install --no-cache --upgrade" \
    DOCKER_HOST=unix:///var/run/docker.sock \
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
    $CTR_PIP yamllint ansible-lint'<6' pycrypto pywinrm docker git-semver commitizen && \
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
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_amd64.tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    cd /

ENV PUSHRM_VERSION="1.8.0"
RUN echo "Installing pushrm version: ${PUSHRM_VERSION}..."  && \
    curl -L "https://github.com/christian-korneck/docker-pushrm/releases/download/v${PUSHRM_VERSION}/docker-pushrm_linux_amd64" -o /usr/local/bin/docker-pushrm && \
    chmod +x /usr/local/bin/docker-pushrm

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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.9.*,docker,dockerstable-dind"
