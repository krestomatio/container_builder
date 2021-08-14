FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="4b32b27ef74ddaf319472f5922e7f362f11d242c"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
