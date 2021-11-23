## CONTAINER_BUILDER
This project builds containers using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, templates and local connection.

### Containers build info
| Container Directory  | Container Image  | Version  |
|---|---|---|
| [ansible-docker-ci](ansible-docker-ci/ )| [quay.io/krestomatio/ansible-docker-ci](https://quay.io/krestomatio/ansible-docker-ci) | 0.1.29 |
| [ansible-operator-ci](ansible-operator-ci/ )| [quay.io/krestomatio/ansible-operator-ci](https://quay.io/krestomatio/ansible-operator-ci) | 0.1.30 |
| [ansible-podman-ci](ansible-podman-ci/ )| [quay.io/krestomatio/ansible-podman-ci](https://quay.io/krestomatio/ansible-podman-ci) | 0.1.29 |
| [ansible](ansible/ )| [quay.io/krestomatio/ansible](https://quay.io/krestomatio/ansible) | 0.1.29 |
| [base-stream](base-stream/ )| [quay.io/krestomatio/base-stream](https://quay.io/krestomatio/base-stream) | 0.1.29 |
| [base](base/ )| [quay.io/krestomatio/base](https://quay.io/krestomatio/base) | 0.1.29 |
| [centos8-minimal](centos8-minimal/ )| [quay.io/krestomatio/centos8-minimal](https://quay.io/krestomatio/centos8-minimal) | 8.5.1 |
| [centos8-stream-minimal](centos8-stream-minimal/ )| [quay.io/krestomatio/centos8-stream-minimal](https://quay.io/krestomatio/centos8-stream-minimal) | 8.6.1 |
| [go-toolset](go-toolset/ )| [quay.io/krestomatio/go-toolset](https://quay.io/krestomatio/go-toolset) | 0.0.11 |
| [graphql-engine-base](graphql-engine-base/ )| [quay.io/krestomatio/graphql-engine-base](https://quay.io/krestomatio/graphql-engine-base) | 2.0.9 |
| [graphql-engine-build](graphql-engine-build/ )| [quay.io/krestomatio/graphql-engine-build](https://quay.io/krestomatio/graphql-engine-build) | 2.0.9 |
| [graphql-engine](graphql-engine/ )| [quay.io/krestomatio/graphql-engine](https://quay.io/krestomatio/graphql-engine) | 2.0.9 |
| [httpd](httpd/ )| [quay.io/krestomatio/httpd](https://quay.io/krestomatio/httpd) | 0.1.29 |
| [moodle_app](moodle_app/ )| [quay.io/krestomatio/moodle_app](https://quay.io/krestomatio/moodle_app) | 3.9.11 |
| [moodle_httpd](moodle_httpd/ )| [quay.io/krestomatio/moodle_httpd](https://quay.io/krestomatio/moodle_httpd) | 0.1.29 |
| [moodle_nginx](moodle_nginx/ )| [quay.io/krestomatio/moodle_nginx](https://quay.io/krestomatio/moodle_nginx) | 0.1.29 |
| [moodle_nginx_web](moodle_nginx_web/ )| [quay.io/krestomatio/moodle_nginx_web](https://quay.io/krestomatio/moodle_nginx_web) | 0.1.29 |
| [moodle_php-fpm](moodle_php-fpm/ )| [quay.io/krestomatio/moodle_php-fpm](https://quay.io/krestomatio/moodle_php-fpm) | 0.1.29 |
| [moodle_web](moodle_web/ )| [quay.io/krestomatio/moodle_web](https://quay.io/krestomatio/moodle_web) | 3.9.11 |
| [nginx](nginx/ )| [quay.io/krestomatio/nginx](https://quay.io/krestomatio/nginx) | 0.1.29 |
| [nginx_php-fpm](nginx_php-fpm/ )| [quay.io/krestomatio/nginx_php-fpm](https://quay.io/krestomatio/nginx_php-fpm) | 0.1.29 |
| [php-fpm](php-fpm/ )| [quay.io/krestomatio/php-fpm](https://quay.io/krestomatio/php-fpm) | 0.1.29 |
| [postgres](postgres/ )| [quay.io/krestomatio/postgres](https://quay.io/krestomatio/postgres) | 0.1.29 |
| [rocky8-minimal](rocky8-minimal/ )| [quay.io/krestomatio/rocky8-minimal](https://quay.io/krestomatio/rocky8-minimal) | 8.5.1 |
| [rootfs-creator](rootfs-creator/ )| [quay.io/krestomatio/rootfs-creator](https://quay.io/krestomatio/rootfs-creator) | 0.1.20 |

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
