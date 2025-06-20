# Centos
## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [centos:9-base](#centos9-base): `9-base, 9.0-base, 9.0.28-base, centos9-base-b33b0b1135bff46ec84534fccab021d244edf76c`
- [centos:9-minimal](#centos9-minimal): `9-minimal, 9.0-minimal, 9.0.28-minimal, centos9-minimal-b33b0b1135bff46ec84534fccab021d244edf76c`


## Image Variants
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

