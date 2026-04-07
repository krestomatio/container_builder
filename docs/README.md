# Container Image Builder
This project builds containers using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, templates and local connection.

## Container Build Info
| Container Directory  | Container Image  | Version  |
|---|---|---|
| [ansible-docker-ci](ci/ansible-docker-ci/)| [quay.io/krestomatio/ansible-docker-ci](https://quay.io/krestomatio/ansible-docker-ci) | 0.5.15 |
| [ansible-operator-ci](ci/ansible-operator-ci/)| [quay.io/krestomatio/ansible-operator-ci](https://quay.io/krestomatio/ansible-operator-ci) | 0.5.15 |
| [ansible-podman-ci](ci/ansible-podman-ci/)| [quay.io/krestomatio/ansible-podman-ci](https://quay.io/krestomatio/ansible-podman-ci) | 0.5.15 |
| [ansible](ci/ansible/)| [quay.io/krestomatio/ansible](https://quay.io/krestomatio/ansible) | 0.5.15 |
| [centos:10-base](centos/centos10-base/)| [quay.io/krestomatio/centos:10-base](https://quay.io/krestomatio/centos) | 10.0.20 |
| [centos:10-minimal](centos/centos10-minimal/)| [quay.io/krestomatio/centos:10-minimal](https://quay.io/krestomatio/centos) | 10.0.20 |
| [centos:9-base](centos/centos9-base/)| [quay.io/krestomatio/centos:9-base](https://quay.io/krestomatio/centos) | 9.0.35 |
| [centos:9-minimal](centos/centos9-minimal/)| [quay.io/krestomatio/centos:9-minimal](https://quay.io/krestomatio/centos) | 9.0.35 |
| [go:1.26-toolset](go/go126-toolset/)| [quay.io/krestomatio/go:1.26-toolset](https://quay.io/krestomatio/go) | 1.26.2 |
| [httpd:2.4](httpd/httpd24/)| [quay.io/krestomatio/httpd:2.4](https://quay.io/krestomatio/httpd) | 2.4.50 |
| [keydb:6.3.4](keydb/keydb63/)| [quay.io/krestomatio/keydb:6.3.4](https://quay.io/krestomatio/keydb) | 6.3.4 |
| [moodle:4.5](moodle/moodle45/)| [quay.io/krestomatio/moodle:4.5](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-bundle](moodle/moodle45_bundle/)| [quay.io/krestomatio/moodle:4.5-bundle](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-httpd](moodle/moodle45_httpd24/)| [quay.io/krestomatio/moodle:4.5-httpd](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-kio](moodle/moodle45_kio/)| [quay.io/krestomatio/moodle:4.5-kio](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-nginx](moodle/moodle45_nginx126/)| [quay.io/krestomatio/moodle:4.5-nginx](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-nginx_php-fpm](moodle/moodle45_nginx126_php83-fpm/)| [quay.io/krestomatio/moodle:4.5-nginx_php-fpm](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [moodle:4.5-php-fpm](moodle/moodle45_php83-fpm/)| [quay.io/krestomatio/moodle:4.5-php-fpm](https://quay.io/krestomatio/moodle) | 4.5.10 |
| [nfs-ganesha:5.9](nfs-ganesha/nfs-ganesha5/)| [quay.io/krestomatio/nfs-ganesha:5.9.10](https://quay.io/krestomatio/nfs-ganesha) | 5.9.10 |
| [nginx:1.20](nginx/nginx120/)| [quay.io/krestomatio/nginx:1.20](https://quay.io/krestomatio/nginx) | 1.20.50 |
| [nginx:1.20-php-fpm](nginx/nginx120_php80-fpm/)| [quay.io/krestomatio/nginx:1.20-php-fpm](https://quay.io/krestomatio/nginx) | 1.20.50 |
| [nginx:1.26](nginx/nginx126/)| [quay.io/krestomatio/nginx:1.26](https://quay.io/krestomatio/nginx) | 1.26.5 |
| [nginx:1.26-php-fpm](nginx/nginx126_php83-fpm/)| [quay.io/krestomatio/nginx:1.26-php-fpm](https://quay.io/krestomatio/nginx) | 1.26.5 |
| [node:18-ci](node/node18-ci/)| [quay.io/krestomatio/node:18-ci](https://quay.io/krestomatio/node) | 18.0.34 |
| [node:18](node/node18/)| [quay.io/krestomatio/node:18](https://quay.io/krestomatio/node) | 18.0.33 |
| [node:22-ci](node/node22-ci/)| [quay.io/krestomatio/node:22-ci](https://quay.io/krestomatio/node) | 22.0.8 |
| [node:22](node/node22/)| [quay.io/krestomatio/node:22](https://quay.io/krestomatio/node) | 22.0.8 |
| [pgbouncer](pgbouncer/)| [quay.io/krestomatio/pgbouncer](https://quay.io/krestomatio/pgbouncer) | 0.5.15 |
| [php:8.0](php/php80-fpm/)| [quay.io/krestomatio/php:8.0](https://quay.io/krestomatio/php) | 8.0.50 |
| [php:8.3](php/php83-fpm/)| [quay.io/krestomatio/php:8.3](https://quay.io/krestomatio/php) | 8.3.8 |
| [postgres:13](postgres/postgres13/)| [quay.io/krestomatio/postgres:13](https://quay.io/krestomatio/postgres) | 13.0.51 |
| [postgres:15](postgres/postgres15/)| [quay.io/krestomatio/postgres:15](https://quay.io/krestomatio/postgres) | 15.0.4 |
| [postgres:16](postgres/postgres16/)| [quay.io/krestomatio/postgres:16](https://quay.io/krestomatio/postgres) | 16.0.8 |
| [rocky:8-base](rocky/rocky8-base/)| [quay.io/krestomatio/rocky:8-base](https://quay.io/krestomatio/rocky) | 8.10.1 |
| [rocky:8-minimal](rocky/rocky8-minimal/)| [quay.io/krestomatio/rocky:8-minimal](https://quay.io/krestomatio/rocky) | 8.10.1 |
| [rocky:9-base](rocky/rocky9-base/)| [quay.io/krestomatio/rocky:9-base](https://quay.io/krestomatio/rocky) | 9.7.1 |
| [rocky:9-minimal](rocky/rocky9-minimal/)| [quay.io/krestomatio/rocky:9-minimal](https://quay.io/krestomatio/rocky) | 9.7.1 |

## Project Requirements
* ansible-core >= 2.18
* docker or podman
* python docker
* [buildx](https://github.com/docker/buildx)
* see [requirements.txt](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/requirements.txt)
* see [requirements.yml](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/requirements.yml)

## Building Containers with Ansible Playbook
```bash
ansible-playbook .ansible-ci/build.yml
```

## Project Directory Structure
```
├── .ansible-ci             # ansible tasks to build and release container images
├── .lighthouse             # jenkins-x pipelines
└── */                      # directories where generated container contexts are saved
```

## Contributing to the Project
* Context and dockerfile templates are inside each container's [directory](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/files/templated_contexts/). Some contexts and templates are reused by more than one container. Their respective variables generate different contexts in each container generated directory
* Variables can be changed inside [the inventory](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/inventory/) dir
* Please modify or update only [templated context](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/files/templated_contexts/) or [the inventory](https://github.com/krestomatio/container_builder/tree/master/.ansible-ci/inventory/)
