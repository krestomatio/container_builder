This container creates a rootfs. It has installed livemedia-creator in a CentOS 8 Stream minimal based image. An example [here](https://github.com/krestomatio/container_builder/tree/master/rootfs-creator)

## How rootfs can be generated using this container
```
# working dir
├── rocky8-minimal.ks
```
```bash
# run
docker run --rm --privileged -v "$PWD:/build:z" \
    -e BUILD_KICKSTART=rocky8-minimal.ks \
    -e BUILD_ROOTFS=rocky8-minimal.tar.xz \
    quay.io/krestomatio/rootfs-creator
```
