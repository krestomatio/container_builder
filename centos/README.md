# Centos
## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [centos:10-base](#centos10-base): `10-base, 10.0-base, 10.0.20-base, centos10-base-0dc932119c2355f7237bc07be799bbbd610fd537`
- [centos:10-minimal](#centos10-minimal): `10-minimal, 10.0-minimal, 10.0.20-minimal, centos10-minimal-0dc932119c2355f7237bc07be799bbbd610fd537`
- [centos:9-base](#centos9-base): `9-base, 9.0-base, 9.0.35-base, centos9-base-0dc932119c2355f7237bc07be799bbbd610fd537`
- [centos:9-minimal](#centos9-minimal): `9-minimal, 9.0-minimal, 9.0.35-minimal, centos9-minimal-0dc932119c2355f7237bc07be799bbbd610fd537`


## Image Variants
### centos:10-base
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos10-base)

A CentOS 10 Stream minimal base image. Its purpose is to be the source image to build from. It contains several binaries to help build new images.

### centos:10-minimal
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/centos/centos10-minimal)

This is a CentOS 10 Stream Minimal Image, similar to Fedora-minimal or UBI.

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

