FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="2921bb3aad8e3bca3d3a6bd4681b15f1286a0f0f"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
