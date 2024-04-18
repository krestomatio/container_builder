# Centos
## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [centos:9-base](#centos9-base): `9-base, 9.0-base, 9.0.24-base, centos9-base-640087a23e7db38d8a27c2b04c408e564397d961`
- [centos:9-minimal](#centos9-minimal): `9-minimal, 9.0-minimal, 9.0.24-minimal, centos9-minimal-640087a23e7db38d8a27c2b04c408e564397d961`


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

