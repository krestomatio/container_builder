FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="5d2d0e666ed914183dcde1ecfb38d957c39a7ed8"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
