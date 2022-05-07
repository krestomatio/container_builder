FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="5f9252e862eae72148f083fcb5fdf97e7abaf81d"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
