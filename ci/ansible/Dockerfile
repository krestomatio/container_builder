# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/centos:9-base
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=ansible \
    IMAGE_SUMMARY="Ansible image based on CentOS 9 Stream minimal for Continuous Integration" \
    IMAGE_DESCRIPTION="CentOS 9 Stream minimal based image with Ansible and Molecule" \
    IMAGE_TITLE="Ansible image based on CentOS 9 Stream minimal"

# Container variables
ENV ANSIBLE_VERSION="2.18.*" \
    MOLECULE_VERSION="5.1.*" \
    PYTHON_VERSION="3.12" \
    CTR_PIP="pip${PYTHON_VERSION:-3} install --no-cache --upgrade" \
    CTR_PIP_EXTRA="yamllint ansible-lint flake8 cryptography git-semver openshift makejinja"

RUN echo "Build tools..."  && \
    $CTR_PKG_MGM install python${PYTHON_VERSION:-3}-devel gcc libffi-devel && \
    echo "Installing pkgs..."  && \
    python${PYTHON_VERSION:-3} -m ensurepip && \
    $CTR_PIP cffi pip && \
    $CTR_PIP ansible-core==$ANSIBLE_VERSION && \
    $CTR_PIP molecule==$MOLECULE_VERSION && \
    echo "Installing other pip tools..."  && \
    $CTR_PIP $CTR_PIP_EXTRA && \
    echo "Installing ansible collections..."  && \
    mkdir -p /usr/share/ansible/collections && \
    ansible-galaxy collection install -p /usr/share/ansible/collections ansible.posix community.general community.docker && \
    echo "Cleaning..."  && \
    $CTR_PKG_MGM remove -y python${PYTHON_VERSION:-3}-devel gcc libffi-devel && \
    $CTR_PKG_MGM clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.* && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

# Container variables
ENV CTR_PKG_EXTRA="git git-lfs rsync jq openssh-clients sudo sshpass curl sudo make which procps-ng ncurses"

RUN install-pkgs -e $CTR_PKG_EXTRA

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
      io.openshift.tags="${IMAGE_NAME},ansible,ansible2.2"
