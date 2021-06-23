FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="d38910e1828175db3a55f1878ed90c4a25d55ea7"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
