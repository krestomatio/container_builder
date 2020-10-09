# Ansible managed
FROM quay.io/buildah/stable

# General variables
ENV IMAGE_name=ansible-podman-ci \
    IMAGE_summary="Ansible image based on Buildah Stable Image for Continuous Integration" \
    IMAGE_description="Buildah Stable Image based image with Ansible and tools like Buildah, Podman, Skopeo and Molecule, for CI" \
    IMAGE_title="Ansible CI image based on Buildah Stable Image"

# Container variables
ENV ANSIBLE_version="2.9" \
    MOLECULE_version="3.0" \
    CTR_pkg_mgm="dnf install -y" \
    CTR_pip="pip3 install --no-cache --upgrade"

RUN echo "Build tools..."  && \
    $CTR_pkg_mgm python-devel gcc && \
    echo "Installing pkgs..."  && \
    python3 -m ensurepip && \
    $CTR_pip cffi pip && \
    $CTR_pip ansible~=$ANSIBLE_version && \
    $CTR_pip molecule~=$MOLECULE_version && \
    echo "Installing other pip tools..."  && \
    $CTR_pip yamllint ansible-lint pycrypto git-semver commitizen && \
    echo "Cleaning..."  && \
    dnf autoremove -y python-devel gcc && \
    dnf clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.* && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

RUN echo "Installing other tools..."  && \
    $CTR_pkg_mgm xz podman git rsync jq sudo sshpass openssh-clients skopeo curl \
    --exclude container-selinux && \
    echo "Cleaning..." && \
    dnf clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.*

ENV JX3_VERSION="3.0.584"
ENV JX3_HOME=/home/.jx3
RUN echo "Installing jx3 version: ${JX3_VERSION}..."  && \
    pushd /tmp && \
    curl -L https://github.com/jenkins-x/jx-cli/releases/download/v${JX3_VERSION}/jx-cli-linux-amd64.tar.gz | tar xzv && \
    mv jx /usr/bin/jx && \
    echo "Pre-load jx3 plugins..."  && \
    # jx upgrade plugins --mandatory && \
    jx gitops version && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    popd

ENV ORAS_VERSION="0.8.1"
RUN echo "Installing oras version: ${ORAS_VERSION}..."  && \
    pushd /tmp && \
    curl -L https://github.com/deislabs/oras/releases/download/v${ORAS_VERSION}/oras_${ORAS_VERSION}_linux_amd64.tar.gz | tar xzv && \
    mv oras /usr/bin/oras && \
    echo "Cleaning..."  && \
    rm -rf /tmp/* && \
    popd

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
      io.openshift.tags="${IMAGE_name},ansible,ansible2.9,buildah,buildah-stable"
