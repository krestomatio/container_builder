## CONTAINER_BUILDER
This project builds containers using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, templates and local connection.

### Containers build info
| Container Directory  | Container Image  | Version  |
|---|---|---|
| [ansible-docker-ci](ansible-docker-ci/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-docker-ci](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-docker-ci) | 0.1.22-c0ad7c2 |
| [ansible-operator-ci](ansible-operator-ci/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-operator-ci](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-operator-ci) | 0.1.23-412e658 |
| [ansible-podman-ci](ansible-podman-ci/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-podman-ci](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible-podman-ci) | 0.1.22-c0ad7c2 |
| [ansible](ansible/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/ansible) | 0.1.22-80fa514 |
| [base-stream](base-stream/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/base-stream](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/base-stream) | 0.1.22-80fa514 |
| [base](base/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/base](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/base) | 0.1.22-80fa514 |
| [centos8-minimal](centos8-minimal/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/centos8-minimal](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/centos8-minimal) | 8.4.1-80fa514 |
| [centos8-stream-minimal](centos8-stream-minimal/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/centos8-stream-minimal](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/centos8-stream-minimal) | 8.5.3-80fa514 |
| [go-toolset](go-toolset/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/go-toolset](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/go-toolset) | 0.0.4-80fa514 |
| [graphql-engine-base](graphql-engine-base/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/graphql-engine-base](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/graphql-engine-base) | 2.0.7-80fa514 |
| [graphql-engine-build](graphql-engine-build/ )| [quay.io/krestomatio/graphql-engine-build](https://quay.io/krestomatio/graphql-engine-build) | 2.0.7 |
| [graphql-engine](graphql-engine/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/graphql-engine](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/graphql-engine) | 2.0.7-412e658 |
| [httpd](httpd/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/httpd](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/httpd) | 0.1.22-80fa514 |
| [moodle_app](moodle_app/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_app](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_app) | 3.9.9-412e658 |
| [moodle_httpd](moodle_httpd/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_httpd](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_httpd) | 0.1.22-412e658 |
| [moodle_nginx_web](moodle_nginx_web/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_nginx_web](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_nginx_web) | 0.1.22-412e658 |
| [moodle_nginx](moodle_nginx/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_nginx](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_nginx) | 0.1.22-412e658 |
| [moodle_php-fpm](moodle_php-fpm/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_php-fpm](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_php-fpm) | 0.1.22-412e658 |
| [moodle_web](moodle_web/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_web](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/moodle_web) | 3.9.9-412e658 |
| [nginx_php-fpm](nginx_php-fpm/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/nginx_php-fpm](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/nginx_php-fpm) | 0.1.22-c0ad7c2 |
| [nginx](nginx/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/nginx](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/nginx) | 0.1.22-80fa514 |
| [php-fpm](php-fpm/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/php-fpm](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/php-fpm) | 0.1.22-80fa514 |
| [postgres](postgres/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/postgres](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/postgres) | 0.1.22-80fa514 |
| [rocky8-minimal](rocky8-minimal/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/rocky8-minimal](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/rocky8-minimal) | 8.4.32-80fa514 |
| [rootfs-creator](rootfs-creator/ )| [docker-registry.jx.krestomat.io/krestomatio/container_builder/rootfs-creator](https://docker-registry.jx.krestomat.io/krestomatio/container_builder/rootfs-creator) | 0.1.13-80fa514 |

### How to build them?
```bash
ansible-playbook .ansible-ci/build.yml
```

### Requirements
* Ansible >= 2.9
* docker or podman
* python docker
* see [requirements.txt](.ansible-ci/requirements.txt)

### Want to contribute?
* Context and dockerfile templates are inside each container's [directory](.ansible-ci/files/templated_contexts/). Some contexts and templates are reused by more than one container. Their respective variables generate different contexts in each container generated directory
* Variables can be changed inside [the inventory](.ansible-ci/inventory) dir
* Please modify or update only [templated context](.ansible-ci/files/templated_contexts/) or [the inventory](.ansible-ci/inventory)

### Directory layout
```
├── .ansible-ci             # ansible tasks to build and release container images
├── .lighthouse             # jenkins-x pipelines
└── */                      # directories where generated container contexts are saved
```
