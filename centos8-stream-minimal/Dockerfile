FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="842a3993054ac23b4b7f38145481dd37ca69ce0e"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
