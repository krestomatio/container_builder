FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="ea2d24b86746ea63e21046661553d1e5704fb822"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
