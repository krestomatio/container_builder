FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="790c89e9dfd51062dae02efd284bde6ca52c050a"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
