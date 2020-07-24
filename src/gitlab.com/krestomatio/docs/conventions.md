# Conventions
Several conventions and guidelines for Dockerfiles in this project

## Best practices
Follow container best practices:
1. [Docker](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
2. [Openshift](https://docs.openshift.com/container-platform/4.2/openshift_images/create-images.html)


## Variable names
When setting new variable names, these guidelines are followed:
1. '**COMPONENT_variable_name**'
2. '**UPPERCASE_lowercase**'

Examples for components
1. '**CTR**': prefix for container related config
2. '**PHP**': prefix for php related config
3. '**HTTPD**': prefix for apache related config
Some examples:
```
CTR_user=default
PHP_FPM_port=9000
```

## Labels
For labels inside Dockerfiles, place them at the end, as one block
