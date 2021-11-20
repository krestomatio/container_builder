FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="c887329eacdad981cdec64bf8670e3d9bd6c7ec6"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
