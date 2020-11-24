This container creates a rootfs. It has installed livemedia-creator in a Centos 8 minimal based image.
An example [here](https://github.com/krestomatio/centos8-minimal)

## How rootfs can be generated using this container
```
# working dir
├── centos8-minimal.ks
```
```bash
# run
docker run --rm --privileged -v "$PWD:/build:z" \
    quay.io/krestomatio/rootfs-creator \
    centos8-minimal.ks centos8-minimal.tar.xz
```
