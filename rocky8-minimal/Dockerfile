FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="5de4ab3b8b816a0f8616b6c91b79acde74d00910"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
