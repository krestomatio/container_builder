FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="53f9ac27d9a587903421f3c3ab6992415e8ad5a2"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
