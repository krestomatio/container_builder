FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="3975068270365a966efbae6030de3c97608fcbdb"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
