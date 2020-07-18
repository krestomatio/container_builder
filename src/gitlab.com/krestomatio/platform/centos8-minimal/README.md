[![Docker Repository on Quay](https://quay.io/repository/krestomatio/centos8-minimal/status "Docker Repository on Quay")](https://quay.io/repository/krestomatio/centos8-minimal)

This is a Centos 8 minimal container image similar to Fedora-minimal or UBI.

## How rootfs is generated for this repo?
```bash
docker run --rm --privileged -v "$PWD:/build:z" \
    quay.io/krestomatio/rootfs-creator \
    centos8-minimal.ks centos8-minimal.tar.xz
```

## How image is built?
```bash
docker build .
```
