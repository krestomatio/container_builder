# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=ansible \
    IMAGE_summary="Ansible image based on CentOS 8 minimal for Continuous Integration" \
    IMAGE_description="CentOS 8 minimal based image with Ansible and Molecule" \
    IMAGE_title="Ansible image based on CentOS 8 minimal"

# Container variables
ENV ANSIBLE_version="2.9.*" \
    MOLECULE_version="3.1.*" \
    CTR_pip="pip3 install --no-cache --upgrade" \
    CTR_pip_extra="yamllint ansible-lint flake8 pycrypto git-semver"

RUN echo "Build tools..."  && \
    $CTR_pkg_mgm install python3-devel gcc && \
    echo "Installing pkgs..."  && \
    python3 -m ensurepip && \
    $CTR_pip cffi pip && \
    $CTR_pip ansible==$ANSIBLE_version && \
    $CTR_pip molecule==$MOLECULE_version && \
    echo "Installing other pip tools..."  && \
    $CTR_pip $CTR_pip_extra && \
    echo "Cleaning..."  && \
    $CTR_pkg_mgm remove -y python3-devel gcc && \
    $CTR_pkg_mgm clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.* && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

# Container variables
ENV CTR_pkg_extra="git rsync jq openssh-clients sudo sshpass curl sudo make"

RUN install-pkgs -e $CTR_pkg_extra

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
      io.openshift.tags="${IMAGE_name},ansible,ansible2.2"
