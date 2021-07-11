FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="68463b6524d356034a386b78ac325260430c193c"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
