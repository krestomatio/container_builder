FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="9eebc21f45c06c3db9c07b2dfa41396d20d94682"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
