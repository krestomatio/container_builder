## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [rocky:8-base](#rocky8-base): `8-base, 8.9-base, 8.9.1-base, rocky8-base-c4faa91d52eabbf101b6e722205f34d5f3f95f08`
- [rocky:8-minimal](#rocky8-minimal): `8-minimal, 8.9-minimal, 8.9.1-minimal, rocky8-minimal-7ca2aba79bd6847c7498c733c91aafe531abf34c`
- [rocky:9-base](#rocky9-base): `9-base, 9.3-base, 9.3.1-base, rocky9-base-c4faa91d52eabbf101b6e722205f34d5f3f95f08`
- [rocky:9-minimal](#rocky9-minimal): `9-minimal, 9.3-minimal, 9.3.1-minimal, rocky9-minimal-2250d9d17d410837907f46969719f3803f8d6caf`


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

