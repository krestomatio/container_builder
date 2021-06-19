FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="44d52d6bf07fae9f5cece18fa120574d751a2ad6"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
