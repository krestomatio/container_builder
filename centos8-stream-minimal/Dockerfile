FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="49719604bdce78a77276e6c9746b21b831889fd9"

ADD centos8-stream-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
