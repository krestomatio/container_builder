FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="6dc41d0a424c18aeed9e965c2475cea95efd2d9f"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
