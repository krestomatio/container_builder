# Ansible managed
FROM quay.io/buildah/stable

# General variables
ENV IMAGE_name=ansible-ci \
    IMAGE_summary="Ansible image based on Buildah Stable Image for Continuous Integration" \
    IMAGE_description="Buildah Stable Image based image with Ansible with tools like Buildah, Podman, Skopeo and Molecule, for CI" \
    IMAGE_title="Ansible CI image based on Buildah Stable Image"

# Container variables
ENV ANSIBLE_version="2.9" \
    MOLECULE_version="3.0" \
    CTR_pkg_mgm="dnf install -y" \
    CTR_pip="pip install --no-cache --upgrade"

RUN echo "Build tools..."  && \
    $CTR_pkg_mgm python-devel gcc && \
    echo "Installing pkgs..."  && \
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
    $CTR_pkg_mgm podman git rsync jq sudo sshpass openssh-clients skopeo \
    --exclude container-selinux && \
    echo "Cleaning..." && \
    dnf clean all && \
    rm -rf /var/cache /var/log/dnf* /var/log/yum.*

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
