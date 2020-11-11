FROM scratch

# General variables
ENV IMAGE_rootfs_pkgs_checksum="24a1a42c9b7054df686210bee8f3e2a9f7ee3dad"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
