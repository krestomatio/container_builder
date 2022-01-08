FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="0a9ebc33ae8eed196fc4f6b4672d57339cba585d"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
