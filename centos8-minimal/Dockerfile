FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="bef7c576304ef955306990d9dd3ee993f352ec2d"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
