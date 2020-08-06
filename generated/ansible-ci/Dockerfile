# Ansible managed
FROM docker:19

# General variables
ENV IMAGE_name=ansible-ci \
    IMAGE_summary="Ansible image based on Docker 19 for Continuous Integration" \
    IMAGE_description="Docker 19 based image with Ansible with tools like Docker, Skopeo and Molecule, for CI" \
    IMAGE_title="Ansible CI image based on Docker 19"

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
      io.openshift.tags="${IMAGE_name},ansible,ansible2.9,docker,docker19"

# Container variables
ENV ANSIBLE_version="2.9" \
    MOLECULE_version="3.0" \
    CTR_apk="apk add --update --no-cache" \
    CTR_pip="pip install --no-cache --upgrade"

RUN $CTR_apk py-pip openssl ca-certificates && \
    $CTR_apk --virtual build-dependencies python3-dev \
        libffi-dev openssl-dev build-base  && \
    $CTR_pip cffi pip && \
    $CTR_pip ansible~=$ANSIBLE_version && \
    $CTR_pip molecule~=$MOLECULE_version && \
    echo "Installing aditional tools..."  && \
    $CTR_pip yamllint ansible-lint pycrypto pywinrm docker git-semver commitizen && \
    $CTR_apk git rsync jq sudo sshpass openssh-client skopeo && \
    echo "Cleaning..."  && \
    apk del build-dependencies && \
    rm -rf /var/cache/apk/* && \
    rm -rf /tmp/* && \
    rm -rf ~/.cache && \
    echo "Minimal ansible config" && \
    mkdir -p /etc/ansible && \
    echo 'localhost' > /etc/ansible/hosts

CMD [ "ansible-playbook", "--version" ]
