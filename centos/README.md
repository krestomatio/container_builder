## Quick reference
- **Maintained by**:
[Krestomatio](https://github.com/krestomatio)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [centos:8-base](#centos8-base): `8-base, 8.6-base, 8.6.2-base, centos8-base-f9c4476b318b1ebb0eb553c1df968183541de018`
- [centos:8-minimal](#centos8-minimal): `8-minimal, 8.6-minimal, 8.6.2-minimal, centos8-minimal-e020b5c2206002f76ad5c48f9ae0f7041e484c74`
- [centos:9-base](#centos9-base): `9-base, 9.0-base, 9.0.21-base, centos9-base-f9c4476b318b1ebb0eb553c1df968183541de018`
- [centos:9-minimal](#centos9-minimal): `9-minimal, 9.0-minimal, 9.0.21-minimal, centos9-minimal-d01dee74483498a371765dc71ec9a201869bb597`


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

