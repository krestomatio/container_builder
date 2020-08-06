FROM scratch

# General variables
ENV IMAGE_rootfs_pkgs_checksum="3769776ebe243fcf3dd0058f1dbff834c87eceec"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
