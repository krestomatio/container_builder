FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="a71876a5bab919883214ff92950bea42793d9375"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
