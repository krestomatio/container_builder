FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="a4a96706bec55fac00ae8362459ce47f0841244a"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
