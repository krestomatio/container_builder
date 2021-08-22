FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="d8e1944830b254edd57700ff1162fe29755e7a40"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
