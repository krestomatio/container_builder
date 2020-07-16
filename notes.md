# References
https://github.com/sclorg/s2i-base-container
https://github.com/sclorg/s2i-php-container
https://github.com/docker-library/php
https://github.com/sclorg/httpd-container
https://github.com/docker-library/httpd
https://github.com/sclorg/postgresql-container
https://github.com/docker-library/postgres



# TODO: image development and production version
## php-fpm development version needs xdebug and profiling
# DONE: variable name convention for container builds and runs:
    # layers: general to more specific as best practices suggest.
    # Variable name convention:
        # For variables meant to be used inside containers:
        # COMPONENT_variable_name
        # UPPERCASE_lowercase
        # No dots for bash
        # 'CTR' prefix for container related config
        # 'PHP' prefix for php related config
        # 'HTTPD' prefix for apache related config
* DONE: gracefully stop opencontainers
  - apache: sigswitch. DONE
  - php-fpm: sigquit    there are more recomendation, one approach is pre_stop. DONE
  - TODO: postgres: sidecar?
* TODO: container path
  - localcache
  - autobackups
* TODO: add notice that also you are agreing with moodle user agreement or add variables
* TODO: secure php-fpm layer from access of no auth pods
* TODO: test if httpd pods only need files other than .php
* TODO: add strategy to each pod
* TODO: postgres should be deployment or replicaset. What happen if deployment is deleted and created. Same uid?
* TODO: add nodeSelector to pods (variable)
* TODO: add network policies
* TODO: agregar o quitar variables: Flexibilidad y muchas variables pueden crear problemas de configuración si se modifican "mid-flight".
* TODO: crear validaciones para crd (structural para evitar campos nuevos)
* TODO: usar el campo de status del CR para guardar info como instantiated, images, dates
* TODO: imagePullPolicy y como controlar versión de Moodle. Imagepolicy de postgres: igual, diferente, crear una imagen de moodle?
  - Image policy de cronjobs? como asegurar misma versión?
