FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="fb4bd1bb7e3e21e4d32929808a411f055d1c3043"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
