# Rocky
## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [rocky:8-base](#rocky8-base): `8-base, 8.10-base, 8.10.1-base, rocky8-base-e27d033856df93b51733282c18c62afafb986687`
- [rocky:8-minimal](#rocky8-minimal): `8-minimal, 8.10-minimal, 8.10.1-minimal, rocky8-minimal-b33b0b1135bff46ec84534fccab021d244edf76c`
- [rocky:9-base](#rocky9-base): `9-base, 9.6-base, 9.6.1-base, rocky9-base-e27d033856df93b51733282c18c62afafb986687`
- [rocky:9-minimal](#rocky9-minimal): `9-minimal, 9.6-minimal, 9.6.1-minimal, rocky9-minimal-b33b0b1135bff46ec84534fccab021d244edf76c`


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

