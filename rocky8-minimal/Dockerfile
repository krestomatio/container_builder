FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="1ece9dd9b95d4aab76ef3914581433bc5763a029"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
