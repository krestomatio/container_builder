FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="eeeddd70a02f924694fe56d249bf8f91d4c04ee5"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
