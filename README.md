# Build containers
It builds containers using Ansible. The containers are defined as hosts in the inventory. They are generated using inventory variables, local connection and templates dirs.

It is required Ansible >= 2.9. Run it with:
```
ansible-playbook -i inventory/hosts build.yml
```
## Directory layout
* Variables can be changed inside [inventory](inventory) dir
* Context and dockerfile templates are inside [templated_contexts](templates) dir
* The generated contexts and dockerfiles are inside [generated_contexts](generated) dir
