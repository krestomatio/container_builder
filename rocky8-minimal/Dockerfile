FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="24004921599431ca4ef46014d6cc87299f036bea"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
