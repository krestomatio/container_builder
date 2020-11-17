# Ansible managed
FROM quay.io/krestomatio/centos8-stream-minimal

# General variables
ENV IMAGE_name=base \
    IMAGE_summary="CentOS 8 Stream minimal based image" \
    IMAGE_description="CentOS 8 Stream minimal based for building other images" \
    IMAGE_title="CentOS 8 Stream minimal based image"

# Container variables
ENV CTR_pkg_mgm="microdnf --setopt=tsflags=nodocs -y" \
    CTR_user=default \
    CTR_user_id="1001" \
    CTR_user_gecos="Default Application User" \
    CTR_group=root \
    CTR_group_id="0" \
    CTR_app="/opt/default" \
    CTR_entrypoint_opt_path=/opt/container-entrypoint.d

ENV OS_install_pkgs="findutils gzip platform-python"

COPY conf/usr/bin/* /usr/bin/
COPY conf/container-entrypoint.d/* ${CTR_entrypoint_opt_path}/

RUN container-setup
RUN install-pkgs ${OS_install_pkgs}

ENTRYPOINT ["container-entrypoint"]

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
      io.openshift.tags="${IMAGE_name},centos,centos8-stream"
