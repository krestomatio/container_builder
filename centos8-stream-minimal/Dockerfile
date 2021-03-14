FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="6c0d7ab8d9aa20a79c9890ccd7e1af65f28e377b"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
