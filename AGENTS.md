# Repository guidance

Follow this repository's documentation and any more specific instructions for
the files being changed.

## Repository scope

- This repository generates and builds Krestomatio base, runtime, database,
  Moodle, and CI container images through the Ansible inventory in `.ansible-ci/`.
- The operational branch is `develop`. Image definitions combine inventory/group
  variables, templates, per-image directories, and state files; update them as one
  contract rather than hand-editing generated contexts.
- The LTS-specific Moodle image packages the Krestomatio Moodle fork and plugins.
  Keep its branch/SHA pins explicit; a source change is not deployed until the
  matching image is rebuilt and `kio-web-app-infra` consumes the new immutable
  digest.

## Validation

- Mirror pull-request CI with targeted Ansible/YAML lint and, when the required
  builder is available, `ansible-playbook .ansible-ci/build.yml` for the affected
  inventory host/group.
- Image builds can be expensive and release playbooks push artifacts. Never run
  `.ansible-ci/release.yml`, promotion, registry pushes, or cloud builders without
  explicit authorization.
