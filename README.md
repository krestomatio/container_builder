# CONTAINER_BUILDER
Containers are built from this project. It is done using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, templates and local connection.

## Requirements
* Ansible >= 2.9
* docker or podman
* python docker

## Build
Run it with:
```bash
ansible-playbook .ansible-ci/build.yml
```
## Directory layout
```
├── .ansible-ci             # ansible tasks to build and release container images
├── .lighthouse             # jenkins-x pipelines
└── */                      # directories where generated container contexts are saved
```
## Contribute
* Context and dockerfile templates are inside each container's [directory](.ansible-ci/templated_contexts/). Some contexts and templates are reused by more than one container. Their respective variables generate different contexts in each container generated directory
* Variables can be changed inside [the inventory](.ansible-ci/inventory) dir
* Please modify or update only [templated context](.ansible-ci/templated_contexts/) or [the inventory](.ansible-ci/inventory)
## Container info
| Container Directory  | Container Image  | Version  |
|---|---|---|
| [centos8-minimal](centos8-minimal/ )| [quay.io/krestomatio/centos8-minimal](quay.io/krestomatio/centos8-minimal@sha256:822b435e4c88eb1ada9c704a3051174fe63cbd397d3d492bb08aee4ef5ed058f) | 8.2.2 |
| [centos8-stream-minimal](centos8-stream-minimal/ )| [quay.io/krestomatio/centos8-stream-minimal](quay.io/krestomatio/centos8-stream-minimal@sha256:b5a504aa70b7ddb4f9b5855e6dca79baa4355e29f2e459dcd645ce0672443440) | 8.4.1 |
| [base](base/ )| [quay.io/krestomatio/base](quay.io/krestomatio/base@sha256:353b33e13e48ae2710740deca5807d663d01fb0a468149cdaa1b8bf7b141ee6d) | 0.1.0 |
| [base-stream](base-stream/ )| [quay.io/krestomatio/base-stream](quay.io/krestomatio/base-stream@sha256:6e382b34097c308e112c8f0212c7dab8af4fe2ca8dfbf94c1eb8818dc674026d) | 0.1.0 |
| [httpd](httpd/ )| [quay.io/krestomatio/httpd](quay.io/krestomatio/httpd@sha256:f797343d6777552015ace4b7ed54bf24e21d9734c9b32721ed5b52a2110deb90) | 0.1.0 |
| [nginx](nginx/ )| [quay.io/krestomatio/nginx](quay.io/krestomatio/nginx@sha256:5528f71cad14abcc95e00c54022e53dedf0aa60370c156de99b7ad1bc241361e) | 0.1.0 |
| [php-fpm](php-fpm/ )| [quay.io/krestomatio/php-fpm](quay.io/krestomatio/php-fpm@sha256:7e8c044d1ae54bbefa4af7b71c1741e1eacf6a3eed5dd86522f535d36f022575) | 0.1.0 |
| [nginx_php-fpm](nginx_php-fpm/ )| [quay.io/krestomatio/nginx_php-fpm](quay.io/krestomatio/nginx_php-fpm@sha256:61a5538181b05a93d7ce955c150c802f1861297e89ce59c8df44dd1880176c89) | 0.1.0 |
| [postgres](postgres/ )| [quay.io/krestomatio/postgres](quay.io/krestomatio/postgres@sha256:fddec0120adb91cfde4867fcbf45dd1ee78be921b32c528f577d1e0939aaf683) | 0.1.0 |
| [ansible](ansible/ )| [quay.io/krestomatio/ansible](quay.io/krestomatio/ansible@sha256:e6ce947311fa2e67fb64f47861257f1af48e774b3ab7d34f01d0d2ecd01e7fba) | 0.1.0 |
| [ansible-operator-ci](ansible-operator-ci/ )| [quay.io/krestomatio/ansible-operator-ci](quay.io/krestomatio/ansible-operator-ci@sha256:310f8f01efed33811bd3bf2de875e8bb9bf3dc571f414c9be1ac5cfe0b0a3a6e) | 0.1.0 |
| [ansible-docker-ci](ansible-docker-ci/ )| [docker.io/krestomatio/ansible-docker-ci](docker.io/krestomatio/ansible-docker-ci@sha256:2f6ea74f579bf6b30ce840e85778caf3145d300c7f29b8c2608722002618c3e5) | 0.1.0 |
| [ansible-podman-ci](ansible-podman-ci/ )| [quay.io/krestomatio/ansible-podman-ci](quay.io/krestomatio/ansible-podman-ci@sha256:01b10ffd4253741b19be3f13f57d3efbdd27bd2fdbebf5a75fcb76bb4293ae69) | 0.1.0 |
| [moodle_app](moodle_app/ )| [quay.io/krestomatio/moodle_app](quay.io/krestomatio/moodle_app@sha256:86f807574cbf9ab32202d1a2d49d49ff32f50cf67754da9996cee02870999d0b) | 3.9.3 |
| [moodle_nginx](moodle_nginx/ )| [quay.io/krestomatio/moodle_nginx](quay.io/krestomatio/moodle_nginx@sha256:c2c802aacef28a352df90d679999a0dffeccba8e867ed3bcf872da261d0df557) | 0.1.0 |
| [moodle_nginx_web](moodle_nginx_web/ )| [quay.io/krestomatio/moodle_nginx_web](quay.io/krestomatio/moodle_nginx_web@sha256:95fcf4b2f71f44790ba13f4af8a2b05e1df0bae77832646da50633c85fecad4f) | 0.1.0 |
| [moodle_php-fpm](moodle_php-fpm/ )| [quay.io/krestomatio/moodle_php-fpm](quay.io/krestomatio/moodle_php-fpm@sha256:1f90e8dca25bc88639bf40fe868e6b8b5194964a8ebe159a202db800cda88f26) | 0.1.0 |
| [moodle_web](moodle_web/ )| [quay.io/krestomatio/moodle_web](quay.io/krestomatio/moodle_web@sha256:0ce99a5459b185dbe7d54d8d1f1c0dd6b5e5df04801c2db675dc5ce1562cd5aa) | 3.9.3 |
| [moodle_httpd](moodle_httpd/ )| [quay.io/krestomatio/moodle_httpd](quay.io/krestomatio/moodle_httpd@sha256:4302bd2e8bd3a96bf98e1e29b89e19071f970188c1e7c35f2cf1904fac19198e) | 0.1.0 |
| [rootfs-creator](rootfs-creator/ )| [quay.io/krestomatio/rootfs-creator](quay.io/krestomatio/rootfs-creator@sha256:7822d7dc10430a17700ad7951e4487c464a954cc336ada8aaaa7c992be786f53) | 0.1.0 |
