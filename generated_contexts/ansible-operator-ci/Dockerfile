# Ansible managed
FROM quay.io/krestomatio/base

# General variables
ENV IMAGE_name=ansible-operator-ci \
    IMAGE_summary="Ansible Operator SDK image based on CentOS 8 minimal for Continuous Integration" \
    IMAGE_description="CentOS 8 minimal based image with Ansible Operator SDK" \
    IMAGE_title="Ansible Operator SDK CI image based on CentOS 8 minimal"

# Container variables
ENV ANSIBLE_OPERATOR_version="1.1.0"

RUN install-pkgs golang make which

# Install kubectl. It is needed for ansible kubectl inventory.
COPY --from=quay.io/operator-framework/operator-sdk:v1.1.0 /usr/local/bin/operator-sdk /usr/local/bin/operator-sdk

# Container variables
ENV KUBECTL_version="1.19.3"

# Install kubectl. It is needed for ansible kubectl inventory.
COPY --from=lachlanevenson/k8s-kubectl:v1.19.3 /usr/local/bin/kubectl /usr/local/bin/kubectl

CMD [ "ansible-operator", "version" ]

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
      io.openshift.tags="${IMAGE_name},ansible,ansible2.9.*,ansible-operator,ansible-operator1.1.0"
