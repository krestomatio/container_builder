# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/base-stream
FROM ${ARG_IMAGE_FROM} AS nfs-ganesha-builder

USER 0

RUN install-pkgs epel-release

# Container variables
ENV CTR_PKG_MGM="microdnf --setopt=tsflags=nodocs --enablerepo=powertools --enablerepo=epel -y" \
    CTR_USER_ID="998"

# Component bash variables
ENV NFS_GANESHA_EXPORT_DIR=/export

# Build deps
RUN install-pkgs \
        bison \
        cmake \
        dbus-devel \
        flex \
        gcc \
        gcc-c++ \
        git \
        jemalloc-devel \
        krb5-devel \
        libblkid-devel \
        libcap-devel \
        libnfsidmap-devel \
        libnsl2-devel \
        libuuid-devel \
        ninja-build \
        userspace-rcu-devel \
        xfsprogs-devel

# Other req
RUN install-pkgs \
        graphviz \
        doxygen \
        redhat-lsb-core

ENV NFS_GANESHA_VERSION="4.0.5" \
    DESTDIR=/build

# invalidate cache if new version
ADD https://api.github.com/repos/nfs-ganesha/nfs-ganesha/git/refs/tags/V${NFS_GANESHA_VERSION} /tmp/version.json

RUN git clone --branch V${NFS_GANESHA_VERSION} --recursive \
    https://github.com/nfs-ganesha/nfs-ganesha /nfs-ganesha

WORKDIR /nfs-ganesha

RUN mkdir -p ${DESTDIR} \
    && cmake -DCMAKE_BUILD_TYPE=Release \
          -DCMAKE_INSTALL_PREFIX=/usr/local \
          -DRADOS_URLS=OFF \
          -DRPCBIND=OFF \
          -DUSE_DBUS=ON \
          -DUSE_NFS3=OFF \
          -DUSE_NLM=OFF \
          -DUSE_9P=OFF \
          -DUSE_9P_RDMA=OFF \
          -DUSE_RQUOTA=ON \
          -DUSE_FSAL_CEPH=OFF \
          -DUSE_FSAL_GLUSTER=OFF \
          -DUSE_FSAL_GPFS=OFF \
          -DUSE_FSAL_KVSFS=OFF \
          -DUSE_FSAL_LIZARDFS=OFF \
          -DUSE_FSAL_LUSTRE=OFF \
          -DUSE_FSAL_PROXY_V3=OFF \
          -DUSE_FSAL_PROXY_V4=OFF \
          -DUSE_FSAL_RGW=OFF \
          -DUSE_FSAL_VFS=ON \
          -DUSE_FSAL_XFS=ON \
          -DUSE_GSS=OFF \
          -DUSE_RADOS_RECOV=OFF \
          -DUSE_SYSTEM_NTIRPC=OFF \
          -D_MSPAC_SUPPORT=OFF \
          -G Ninja src/ \
          src/ \
    && ninja \
	&& ninja install \
    && mkdir -p ${DESTDIR}/usr/local/var/lib/nfs/ganesha \
    && mkdir -p ${DESTDIR}/usr/local/opt/ganesha \
    && /bin/cp CMakeCache.txt install_manifest.txt ${DESTDIR}/usr/local/opt/ganesha \
    && fix-permissions -u ${CTR_USER_ID} ${DESTDIR}

ARG ARG_IMAGE_FROM=quay.io/krestomatio/base-stream
FROM ${ARG_IMAGE_FROM}

# General variables
ENV IMAGE_NAME=nfs-ganesha \
    IMAGE_SUMMARY="NFSv4 Ganesha server 4.0.5" \
    IMAGE_DESCRIPTION="This CentOS 8 Stream minimal based container image runs a NFSv4 Ganesha server." \
    IMAGE_TITLE="NFSv4 Ganesha server 4.0.5" \
    IMAGE_SERVICE_PORT="2049" \
    IMAGE_SERVICE_NAME="nfs" \
    TZ="UTC"

# Container variables
ENV CTR_USER=ganesha \
    CTR_USER_ID="998" \
    CTR_HOME=/usr/local/var/run/ganesha \
    CTR_CMD="ganesha.nfsd"

# Component bash variables
ENV DBUS_RUN_DIR=/var/run/dbus \
    DBUS_RUN_WAIT=false \
    NFS_GANESHA_VERSION="4.0.5" \
    NFS_GANESHA_PORT=${IMAGE_SERVICE_PORT} \
    NFS_GANESHA_RQUOTA_PORT=875 \
    NFS_GANESHA_CONF_FILE=/usr/local/etc/ganesha/ganesha.conf \
    NFS_GANESHA_CONF_DIR=/usr/local/etc/ganesha/ \
    NFS_GANESHA_CONF_EXTRA_FILE=/usr/local/etc/ganesha/ganesha-extra.conf \
    NFS_GANESHA_GRACE_PERIOD=90 \
    NFS_GANESHA_EXPORT_DIR=/export \
    NFS_GANESHA_EXPORT_ID=1 \
    NFS_GANESHA_EXPORT_SQUASH=root_squash \
    NFS_GANESHA_LOG_LEVEL=EVENT \
    NFS_GANESHA_EXPORT_HWMARK=100000 \
    NFS_GANESHA_RUN_DIR=${CTR_HOME} \
    NFS_GANESHA_HOME=${CTR_HOME} \
    NFS_GANESHA_RUN_DIR=/usr/local/var/run/ganesha \
    NFS_GANESHA_PID=/usr/local/var/run/ganesha/ganesha.pid

# Frequent environment variables
ENV HOME="${CTR_HOME}"

USER 0

COPY conf/usr /usr/
COPY conf/container-entrypoint.d ${CTR_ENTRYPOINT_OPT_PATH}/

COPY --chown=${CTR_USER_ID}:${CTR_GROUP_ID:-0} --from=nfs-ganesha-builder /build/usr/local /usr/local/
COPY --chown=${CTR_USER_ID}:${CTR_GROUP_ID:-0} --from=nfs-ganesha-builder /nfs-ganesha/src/scripts/ganeshactl/org.ganesha.nfsd.conf /etc/dbus-1/system.d/org.ganesha.nfsd.conf

RUN container-setup

RUN container-setup-nfs-ganesha

WORKDIR ${CTR_HOME}

EXPOSE ${NFS_GANESHA_PORT}/tcp
EXPOSE ${NFS_GANESHA_PORT}/udp

CMD ["ganesha.nfsd", "-F", "-L", "STDOUT", "-p", "/usr/local/var/run/ganesha/ganesha.pid", "-f", "/usr/local/etc/ganesha/ganesha.conf"]

# Labels
LABEL name="${IMAGE_NAME}" \
      summary="${IMAGE_SUMMARY}" \
      description="${IMAGE_DESCRIPTION}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.title="${IMAGE_TITLE}" \
      org.opencontainers.image.authors="Job Céspedes Ortiz <jobcespedes@krestomatio.com>" \
      org.opencontainers.image.description="${IMAGE_DESCRIPTION}" \
      org.opencontainers.image.version="0.0" \
      io.k8s.description="${IMAGE_DESCRIPTION}" \
      io.k8s.display-name="${IMAGE_TITLE}" \
      io.openshift.expose-services="${IMAGE_SERVICE_PORT}:${IMAGE_SERVICE_NAME}" \
      io.openshift.tags="${IMAGE_NAME},nfs,nfs-ganesha"
