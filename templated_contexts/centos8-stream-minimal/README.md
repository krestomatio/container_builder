[![Docker Repository on Quay](https://quay.io/repository/krestomatio/centos8-stream-minimal/status "Docker Repository on Quay")](https://quay.io/repository/krestomatio/centos8-stream-minimal)

This is a Centos 8 minimal container image similar to Fedora-minimal or UBI.

## How rootfs is generated for this repo?
```bash
docker run --rm --privileged -v "$PWD:/build:z" \
    quay.io/krestomatio/rootfs-creator \
    centos8-stream-minimal.ks centos8-stream-minimal.tar.xz
```

## How image is built?
```bash
docker build .
```
