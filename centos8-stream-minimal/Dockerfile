FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="80f4996af1b47ac8bc014cb786663e23972b9b9d"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
