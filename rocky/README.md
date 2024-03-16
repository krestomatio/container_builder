## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [rocky:8-base](#rocky8-base): `8-base, 8.9-base, 8.9.3-base, rocky8-base-27a644dab1d57434e88641193e1af8791de3bc7f`
- [rocky:8-minimal](#rocky8-minimal): `8-minimal, 8.9-minimal, 8.9.3-minimal, rocky8-minimal-27a644dab1d57434e88641193e1af8791de3bc7f`
- [rocky:9-base](#rocky9-base): `9-base, 9.3-base, 9.3.3-base, rocky9-base-27a644dab1d57434e88641193e1af8791de3bc7f`
- [rocky:9-minimal](#rocky9-minimal): `9-minimal, 9.3-minimal, 9.3.3-minimal, rocky9-minimal-27a644dab1d57434e88641193e1af8791de3bc7f`


## Image Variants
### rocky:8-base
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/rocky/rocky8-base)

A Rocky Linux 8 minimal base image. Its purpose is to be the source image to build from. It contains several binaries to help build new images.

### rocky:8-minimal
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/rocky/rocky8-minimal)

This is a Rocky 8 Linux Minimal Image, similar to Fedora-minimal or UBI.

## How the image is built?
```bash
docker build . -t "quay.io/krestomatio/rocky"
```

### rocky:9-base
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/rocky/rocky9-base)

A Rocky Linux 9 minimal base image. Its purpose is to be the source image to build from. It contains several binaries to help build new images.

### rocky:9-minimal
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/rocky/rocky9-minimal)

This is a Rocky 9 Linux Minimal Image, similar to Fedora-minimal or UBI.

## How the image is built?
```bash
docker build . -t "quay.io/krestomatio/rocky"
```

