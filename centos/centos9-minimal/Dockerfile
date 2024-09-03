# builder
ARG ROOTFS_IMAGE_BASE=quay.io/fedora/fedora-minimal:34
FROM ${ROOTFS_IMAGE_BASE} as builder

ARG TARGETOS
ARG TARGETARCH
ARG ARG_ROOTFS_INSTALL_DIR='/mnt/rootfs'
ARG ARG_ROOTFS_EXTRA_REMOVAL='True'
ARG ARG_ROOTFS_REPO_CONTENTDIR='centos'
ARG ARG_ROOTFS_REPO_RELEASEVER='9'
ARG ARG_ROOTFS_REPO_BASEOS_NAME='CentOS Stream $releasever - BaseOS'
ARG ARG_ROOTFS_REPO_BASEOS_MIRRORLIST=''
ARG ARG_ROOTFS_REPO_BASEOS_METALINK='https://mirrors.centos.org/metalink?repo=centos-baseos-$stream&arch=$basearch&protocol=https,http'
ARG ARG_ROOTFS_REPO_BASEOS_GPGKEY='https://www.centos.org/keys/RPM-GPG-KEY-CentOS-Official'
ARG ARG_ROOTFS_DNF_VARS='contentdir=centos stream=9-stream infra=container'
ARG ARG_ROOTFS_EXTRA_PKGS='bash coreutils-single glibc-minimal-langpack microdnf rootfiles'
ARG ARG_ROOTFS_RELEASE_PKG='centos-stream-release'

ENV TARGETOS=${TARGETOS} \
    TARGETARCH=${TARGETARCH} \
    ROOTFS_INSTALL_DIR="${ARG_ROOTFS_INSTALL_DIR}" \
    ROOTFS_EXTRA_REMOVAL="${ARG_ROOTFS_EXTRA_REMOVAL}" \
    ROOTFS_REPO_CONTENTDIR="${ARG_ROOTFS_REPO_CONTENTDIR}" \
    ROOTFS_REPO_RELEASEVER="${ARG_ROOTFS_REPO_RELEASEVER}" \
    ROOTFS_REPO_BASEOS_NAME="${ARG_ROOTFS_REPO_BASEOS_NAME}" \
    ROOTFS_REPO_BASEOS_MIRRORLIST="${ARG_ROOTFS_REPO_BASEOS_MIRRORLIST}" \
    ROOTFS_REPO_BASEOS_METALINK="${ARG_ROOTFS_REPO_BASEOS_METALINK}" \
    ROOTFS_REPO_BASEOS_GPGKEY="${ARG_ROOTFS_REPO_BASEOS_GPGKEY}" \
    ROOTFS_DNF_VARS="${ARG_ROOTFS_DNF_VARS}" \
    ROOTFS_EXTRA_PKGS="${ARG_ROOTFS_EXTRA_PKGS}" \
    ROOTFS_RELEASE_PKG="${ARG_ROOTFS_RELEASE_PKG}"

COPY conf/usr/bin /usr/bin

RUN rootfs


# pkg list
FROM scratch AS pkg_list

ARG TARGETOS
ARG TARGETARCH

COPY --from=builder /pkg_list_${TARGETOS}_${TARGETARCH} /


# image
FROM scratch

ARG ARG_ROOTFS_INSTALL_DIR='/mnt/rootfs'

COPY --from=builder "${ARG_ROOTFS_INSTALL_DIR}" /

CMD ["/bin/bash"]

ENV IMAGE_VERSION=9.0.26

# Labels
LABEL org.opencontainers.image.title="CentOS 9 Stream Minimal Image" \
      org.opencontainers.image.version="9.0.26"
