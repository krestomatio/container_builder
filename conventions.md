# Conventions

## Layers
- general to more specific as best practices suggest

## User id and group id for containers
- user id from distribution
- if  distribution do not set exclusively one user id, use 1001
- use group id 0 for permissions in order to offer OKD compatibility
  - except when setting /etc/passwd and /etc/group (use the same group id and name as user id and name)

## Variable names
- for variables meant to be used inside containers:
  - COMPONENT_variable_name
  - UPPERCASE_lowercase
  - No dots for bash
  - Examples:
    - 'CTR' prefix for container related config
    - 'PHP' prefix for php related config
    - 'HTTPD' prefix for apache related config
