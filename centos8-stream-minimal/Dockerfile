FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="64e27985a0cf700eb0308eea3d77710702e0bd64"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
