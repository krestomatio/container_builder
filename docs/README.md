# Container Image Builder
This project builds containers using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, templates and local connection.

## Container Build Info
| Container Directory  | Container Image  | Version  |
|---|---|---|
| [ansible-docker-ci](ci/ansible-docker-ci/)| [quay.io/krestomatio/ansible-docker-ci](https://quay.io/krestomatio/ansible-docker-ci) | 0.5.10 |
| [ansible-operator-ci](ci/ansible-operator-ci/)| [quay.io/krestomatio/ansible-operator-ci](https://quay.io/krestomatio/ansible-operator-ci) | 0.5.10 |
| [ansible-podman-ci](ci/ansible-podman-ci/)| [quay.io/krestomatio/ansible-podman-ci](https://quay.io/krestomatio/ansible-podman-ci) | 0.5.10 |
| [ansible](ci/ansible/)| [quay.io/krestomatio/ansible](https://quay.io/krestomatio/ansible) | 0.5.10 |
| [centos:9-base](centos/centos9-base/)| [quay.io/krestomatio/centos:9-base](https://quay.io/krestomatio/centos) | 9.0.26 |
| [centos:9-minimal](centos/centos9-minimal/)| [quay.io/krestomatio/centos:9-minimal](https://quay.io/krestomatio/centos) | 9.0.26 |
| [go:1.22-toolset](go/go122-toolset/)| [quay.io/krestomatio/go:1.22-toolset](https://quay.io/krestomatio/go) | 1.22.2 |
| [httpd:2.4](httpd/httpd24/)| [quay.io/krestomatio/httpd:2.4](https://quay.io/krestomatio/httpd) | 2.4.45 |
| [keydb:6.3.4](keydb/keydb63/)| [quay.io/krestomatio/keydb:6.3.4](https://quay.io/krestomatio/keydb) | 6.3.4 |
| [moodle:4.1](moodle/moodle41/)| [quay.io/krestomatio/moodle:4.1](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.1-bundle](moodle/moodle41_bundle/)| [quay.io/krestomatio/moodle:4.1-bundle](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.1-httpd](moodle/moodle41_httpd24/)| [quay.io/krestomatio/moodle:4.1-httpd](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.1-kio](moodle/moodle41_kio/)| [quay.io/krestomatio/moodle:4.1-kio](https://quay.io/krestomatio/moodle) | 4.1.14 |
| [moodle:4.1-nginx](moodle/moodle41_nginx120/)| [quay.io/krestomatio/moodle:4.1-nginx](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.1-nginx_php-fpm](moodle/moodle41_nginx120_php80-fpm/)| [quay.io/krestomatio/moodle:4.1-nginx_php-fpm](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.1-php-fpm](moodle/moodle41_php80-fpm/)| [quay.io/krestomatio/moodle:4.1-php-fpm](https://quay.io/krestomatio/moodle) | 4.1.15 |
| [moodle:4.5](moodle/moodle45/)| [quay.io/krestomatio/moodle:4.5](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [moodle:4.5-bundle](moodle/moodle45_bundle/)| [quay.io/krestomatio/moodle:4.5-bundle](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [moodle:4.5-httpd](moodle/moodle45_httpd24/)| [quay.io/krestomatio/moodle:4.5-httpd](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [moodle:4.5-kio](moodle/moodle45_kio/)| [quay.io/krestomatio/moodle:4.5-kio](https://quay.io/krestomatio/moodle) | 4.5.0 |
| [moodle:4.5-nginx](moodle/moodle45_nginx124/)| [quay.io/krestomatio/moodle:4.5-nginx](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [moodle:4.5-nginx_php-fpm](moodle/moodle45_nginx124_php83-fpm/)| [quay.io/krestomatio/moodle:4.5-nginx_php-fpm](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [moodle:4.5-php-fpm](moodle/moodle45_php83-fpm/)| [quay.io/krestomatio/moodle:4.5-php-fpm](https://quay.io/krestomatio/moodle) | 4.5.1 |
| [nfs-ganesha:5.9](nfs-ganesha/nfs-ganesha5/)| [quay.io/krestomatio/nfs-ganesha:5.9.5](https://quay.io/krestomatio/nfs-ganesha) | 5.9.5 |
| [nginx:1.20](nginx/nginx120/)| [quay.io/krestomatio/nginx:1.20](https://quay.io/krestomatio/nginx) | 1.20.45 |
| [nginx:1.20-php-fpm](nginx/nginx120_php80-fpm/)| [quay.io/krestomatio/nginx:1.20-php-fpm](https://quay.io/krestomatio/nginx) | 1.20.45 |
| [nginx:1.24](nginx/nginx124/)| [quay.io/krestomatio/nginx:1.24](https://quay.io/krestomatio/nginx) | 1.24.3 |
| [nginx:1.24-php-fpm](nginx/nginx124_php83-fpm/)| [quay.io/krestomatio/nginx:1.24-php-fpm](https://quay.io/krestomatio/nginx) | 1.24.3 |
| [node:18-ci](node/node18-ci/)| [quay.io/krestomatio/node:18-ci](https://quay.io/krestomatio/node) | 18.0.29 |
| [node:18](node/node18/)| [quay.io/krestomatio/node:18](https://quay.io/krestomatio/node) | 18.0.28 |
| [node:22-ci](node/node22-ci/)| [quay.io/krestomatio/node:22-ci](https://quay.io/krestomatio/node) | 22.0.3 |
| [node:22](node/node22/)| [quay.io/krestomatio/node:22](https://quay.io/krestomatio/node) | 22.0.3 |
| [pgbouncer](pgbouncer/)| [quay.io/krestomatio/pgbouncer](https://quay.io/krestomatio/pgbouncer) | 0.5.10 |
| [php:8.0](php/php80-fpm/)| [quay.io/krestomatio/php:8.0](https://quay.io/krestomatio/php) | 8.0.45 |
| [php:8.3](php/php83-fpm/)| [quay.io/krestomatio/php:8.3](https://quay.io/krestomatio/php) | 8.3.3 |
| [postgres:13](postgres/postgres13/)| [quay.io/krestomatio/postgres:13](https://quay.io/krestomatio/postgres) | 13.0.46 |
| [postgres:16](postgres/postgres16/)| [quay.io/krestomatio/postgres:16](https://quay.io/krestomatio/postgres) | 16.0.3 |
| [rocky:8-base](rocky/rocky8-base/)| [quay.io/krestomatio/rocky:8-base](https://quay.io/krestomatio/rocky) | 8.10.1 |
| [rocky:8-minimal](rocky/rocky8-minimal/)| [quay.io/krestomatio/rocky:8-minimal](https://quay.io/krestomatio/rocky) | 8.10.1 |
| [rocky:9-base](rocky/rocky9-base/)| [quay.io/krestomatio/rocky:9-base](https://quay.io/krestomatio/rocky) | 9.5.1 |
| [rocky:9-minimal](rocky/rocky9-minimal/)| [quay.io/krestomatio/rocky:9-minimal](https://quay.io/krestomatio/rocky) | 9.5.1 |

## Project Requirements
* ansible-core >= 2.15
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
