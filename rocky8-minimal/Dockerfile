FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="5828d85e871e79dfb9c49bafd9af4ba4fcc4d626"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
