FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="4348ea2982a46ae30a66e4a36f65c56b897fb83d"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
