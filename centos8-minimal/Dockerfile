FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="7d3bf8a47ffbcdfcc96f8c63fd16d2b856ef4140"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
