FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="93adb8a0d58e4ad6a2271a32973771e1945e89c8"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
