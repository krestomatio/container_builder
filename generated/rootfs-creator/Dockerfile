# Ansible managed
FROM centos:8

# General variables
ENV IMAGE_name=rootfs-creator \
    IMAGE_summary="CentOS 8 based image" \
    IMAGE_description="CentOS 8 based for building rootfs" \
    IMAGE_title="CentOS 8 based image"

# Container variables
ENV CTR_working_dir=/build

RUN dnf install -y anaconda-tui lorax jq
RUN mkdir $CTR_working_dir

COPY conf/usr/bin/* /usr/bin/

WORKDIR $CTR_working_dir

ENTRYPOINT ["/usr/bin/rootfs-creator"]

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.description="${IMAGE_description}" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_name},centos,centos8,rootfs-creator"
