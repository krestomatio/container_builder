# References
https://github.com/sclorg/s2i-base-container
https://github.com/sclorg/s2i-php-container
https://github.com/docker-library/php
https://github.com/sclorg/httpd-container
https://github.com/docker-library/httpd
https://github.com/sclorg/postgresql-container
https://github.com/docker-library/postgres



# TODO: moodle source code
# TODO: image development and production version
## php-fpm development version needs xdebug and profiling
# TODO: delete php pspell and aspell pckg: https://moodle.org/mod/forum/discuss.php?d=232297. DONE
# TODO: defined SO binaries require by Moodle
# TODO: foreground php.fpm y otras conf iniciales como log https://github.com/https://github.com/docker-library/php/blob/master/7.2/buster/fpm/Dockerfile
# TODO: default user 1001 or apache?. DONE
# TODO: timezone in minimal. DONE
# TODO: timezone in moodle images. DONE
# TODO: permissions of files created other than rpm installed. DONE
# TODO: variable name convention for container builds and runs:
    # layers: general to more specific as best practices suggest.
    # Variable name convention:
        # For variables meant to be used inside containers:
        # COMPONENT_variable_name
        # UPPERCASE_lowercase
        # No dots for bash
        # 'CTR' prefix for container related config
        # 'PHP' prefix for php related config
        # 'HTTPD' prefix for apache related config
# TODO: httpd moodle source? and how to deal with directory index html
# TODO: define how origin and registry groups are defined and dir tree
# TODO: avoid syncing to build when src has Dockerfile with no jinja template
# TODO: issue with vagrant and podman
    # fatal: [instance-centos7]: FAILED! => {"changed": false, "msg": "Failed to build image example.com/mycontainer:latest:  cannot clone: Invalid argument\nuser namespaces are not enabled in /proc/sys/user/max_user_namespaces\nError: could not get runtime: cannot re-exec process\n"}
    # fatal: [instance-ubuntu1804]: FAILED! => {"changed": false, "msg": "Failed to build image example.com/mycontainer:latest:  time=\"2020-01-15T02:58:54Z\" level=error msg=\"cannot find mappings for user vagrant: No subuid ranges found for user \\\"vagrant\\\" in /etc/subuid\"\nError: error creating build container: (image name \"alpine:latest\" is a short name and no search registries are defined in /etc/containers/registries.conf): while pulling \"alpine:latest\" as \"localhost/alpine:latest\": Error initializing source docker://localhost/alpine:latest: pinging docker registry returned: Get https://localhost/v2/: dial tcp [::1]:443: connect: connection refused\n"}
* TODO: gracefully stop opencontainers
  - apache: sigswitch. DONE
  - php-fpm: sigquit    there are more recomendation, one approach is pre_stop. DONE
  - postgres: sidecar?
* TODO: container path
  - localcache
  - autobackups
* TODO: add notice that also you are agreing with moodle user agreement or add variables
* TODO: secure php-fpm layer
