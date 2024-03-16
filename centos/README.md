## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [centos:8-base](#centos8-base): `8-base, 8.6-base, 8.6.3-base, centos8-base-27a644dab1d57434e88641193e1af8791de3bc7f`
- [centos:8-minimal](#centos8-minimal): `8-minimal, 8.6-minimal, 8.6.3-minimal, centos8-minimal-27a644dab1d57434e88641193e1af8791de3bc7f`
- [centos:9-base](#centos9-base): `9-base, 9.0-base, 9.0.25-base, centos9-base-27a644dab1d57434e88641193e1af8791de3bc7f`
- [centos:9-minimal](#centos9-minimal): `9-minimal, 9.0-minimal, 9.0.25-minimal, centos9-minimal-27a644dab1d57434e88641193e1af8791de3bc7f`


## Image Variants
### centos:8-base
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos8-base)

A CentOS 8 Stream minimal base image. Its purpose is to be the source image to build from. It contains several binaries to help build new images.

### centos:8-minimal
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos8-minimal)

This is a CentOS 8 Stream Minimal Image, similar to Fedora-minimal or UBI.

## How the image is built?
```bash
docker build . -t "quay.io/krestomatio/centos"
```

### centos:9-base
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos9-base)

A CentOS 9 Stream minimal base image. Its purpose is to be the source image to build from. It contains several binaries to help build new images.

### centos:9-minimal
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos9-minimal)

This is a CentOS 9 Stream Minimal Image, similar to Fedora-minimal or UBI.

## How the image is built?
```bash
docker build . -t "quay.io/krestomatio/centos"
```

