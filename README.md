# container_builder
It builds containers using Ansible. The containers are defined as hosts in the Ansible inventory. They are generated using host and group variables, template dirs and local connection.

## Requirements
* Ansible >= 2.9
* docker or podman
* python docker

## Usage
Run it with:
```bash
ansible-playbook -i inventory/hosts build.yml
```
## Directory layout
```
├── build.yml               # build pipeline/playbook
├── generated_contexts/     # generated contexts and files
├── inventory/              # container inventory and its variables
├── roles/                  # dependant Ansible role
├── tasks/                  # files with Ansible tasks
├── templated_contexts/     # container templates
└── vars/                   # include vars for usage in plays

```
As an Ansible project:

## Contribute
* Context and dockerfile templates are inside [templated_contexts](templates) dir. Some contexts and templates are reused by more than one container. Their respective variables generate different contexts in [generated_contexts](generated) dir
* Variables can be changed inside [inventory](inventory) dir
* Please update only [templated_contexts](templates) or [inventory](inventory) dir
* List of containers:
  - ansible
  - ansible-operator-ci
  - ansible-docker-ci
  - ansible-podman-ci
  - rootfs-creator
  - centos8-minimal
  - centos8-stream-minimal
  - base
  - httpd
  - nginx
  - php-fpm
  - postgres
  - moodle_app
  - moodle_httpd
  - moodle_nginx
  - moodle_nginx_web
  - moodle_php-fpm
  - nginx_php-fpm
  - moodle_web
* The generated contexts and dockerfiles are inside [generated_contexts](generated) dir
