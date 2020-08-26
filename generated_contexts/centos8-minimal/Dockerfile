FROM scratch

# General variables
ENV IMAGE_rootfs_pkgs_checksum="5e29edf86ce87857d52cb6d647aa039766d0b61b"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
