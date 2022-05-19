FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="8b61bda709a035ad93ded2039f0f326f875304cb"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
