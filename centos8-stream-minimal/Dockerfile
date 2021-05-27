FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="73ad208161a876a0c4f4365831c07237ee974f25"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
