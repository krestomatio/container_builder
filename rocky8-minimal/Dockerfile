FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="cf1ad82509feeb32987f3260b39adaa91d657f4d"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
