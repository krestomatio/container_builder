FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="4ec7dce391d1cf50ba7e55baa9e63305afdf6159"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
