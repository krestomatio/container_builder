FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="b6b0798312319684f3dd3bbcacc4f0e3a59dc655"

ADD rocky8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="Rocky Linux Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
