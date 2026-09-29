# Repository guidance

Before working, read these optional instruction files in order,
resolving these paths from this repository's root:

1. `.agents/organization/AGENTS.md`
2. `.agents/workspace/AGENTS.md`

Read each file if it resolves to a readable regular file.
Skip absent files; report broken or unreadable links.
Read each resolved file only once to avoid duplicate loading and cycles.

Resolve references inside imported files relative to their real target
directory after following symlinks.

Apply organization guidance, then workspace guidance, then the repository
instructions below. More specific applicable instructions take precedence.

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
