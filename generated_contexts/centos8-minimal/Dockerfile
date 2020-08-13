FROM scratch

# General variables
ENV IMAGE_rootfs_pkgs_checksum="6167d5d99004efda65a53a9c98d1e62eb4932d97"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
