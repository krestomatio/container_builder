FROM scratch

# General variables
ENV IMAGE_ROOTFS_PKGS_CHECKSUM="f7dabb117ba3ac4df57e248268123cfc3020fa35"

ADD centos8-minimal.tar.xz /

# Labels
LABEL org.opencontainers.image.title="CentOS Minimal Image" \
      org.opencontainers.image.licenses="GPLv2"

CMD ["/bin/bash"]
