FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="6b724be2c7f1c39ca51a9089327def6d84fd8a16"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
