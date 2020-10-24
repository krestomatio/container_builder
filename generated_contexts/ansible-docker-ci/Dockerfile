# Ansible managed
FROM docker:stable-dind

# General variables
ENV IMAGE_name=ansible-docker-ci \
    IMAGE_summary="Ansible image based on Docker stable-dind for Continuous Integration" \
    IMAGE_description="Docker stable-dind based image with Ansible and tools like Docker, Skopeo and Molecule, for CI" \
    IMAGE_title="Ansible CI image based on Docker stable-dind"

# Container variables
ENV ANSIBLE_version="2.9" \
    MOLECULE_version="3.0" \
    CTR_apk="apk add --update --no-cache" \
    CTR_pip="pip install --no-cache --upgrade" \
    DOCKER_HOST=unix:///var/run/docker.sock

RUN echo "Build tools..."  && \
    $CTR_apk py-pip openssl ca-certificates && \
    $CTR_apk --virtual build-dependencies python3-dev \
        libffi-dev openssl-dev build-base  && \
    $CTR_pip cffi pip && \
    $CTR_pip ansible~=$ANSIBLE_version && \
    $CTR_pip molecule~=$MOLECULE_version && \
    echo "Installing aditional python tools..."  && \
    $CTR_pip yamllint ansible-lint pycrypto pywinrm docker git-semver commitizen && \
    echo "Cleaning..."  && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

RUN echo "Installing other tools..."  && \
    $CTR_apk bash xz git rsync jq sudo sshpass openssh-client skopeo curl && \
    echo "Cleaning..."  && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache

RUN sed -i "s@bin/ash@bin/bash@" /etc/passwd && \
    ln -svf bash /bin/sh

ENV JX3_VERSION="3.0.651"
ENV JX3_HOME=/home/.jx3
RUN echo "Installing jx3 version: ${JX3_VERSION}..."  && \
    cd /tmp && \
    curl -L https://github.com/jenkins-x/jx-cli/releases/download/v${JX3_VERSION}/jx-cli-linux-amd64.tar.gz | tar xzv && \
    mv jx /usr/bin/jx && \
    echo "Pre-load jx3 plugins..."  && \
    # jx upgrade plugins --mandatory && \
    jx gitops version && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    cd /

ENV ORAS_VERSION="0.8.1"
RUN echo "Installing oras version: ${ORAS_VERSION}..."  && \
    cd /tmp && \
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_amd64.tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    cd /

CMD [ "ansible-playbook", "--version" ]

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
      io.openshift.tags="${IMAGE_name},ansible,ansible2.9,docker,dockerstable-dind"
