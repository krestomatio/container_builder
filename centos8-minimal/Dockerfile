FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="26d80de3e5ba5ff171661564001e54490b860e17"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
