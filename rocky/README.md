## Quick reference
- **Maintained by**:
[Krestomatio](https://github.com/krestomatio)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [rocky:8-base](#rocky8-base): `8-base, 8.8-base, 8.8.2-base, rocky8-base-e020b5c2206002f76ad5c48f9ae0f7041e484c74`
- [rocky:8-minimal](#rocky8-minimal): `8-minimal, 8.8-minimal, 8.8.2-minimal, rocky8-minimal-e020b5c2206002f76ad5c48f9ae0f7041e484c74`
- [rocky:9-base](#rocky9-base): `9-base, 9.2-base, 9.2.2-base, rocky9-base-e020b5c2206002f76ad5c48f9ae0f7041e484c74`
- [rocky:9-minimal](#rocky9-minimal): `9-minimal, 9.2-minimal, 9.2.2-minimal, rocky9-minimal-e020b5c2206002f76ad5c48f9ae0f7041e484c74`


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

