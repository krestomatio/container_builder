# References
https://github.com/sclorg/s2i-base-container
https://github.com/sclorg/s2i-php-container
https://github.com/docker-library/php
https://github.com/sclorg/httpd-container
https://github.com/docker-library/httpd



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
        # 'HTTPD' prefix for apache2 related config
# TODO: httpd moodle source? and how to deal with directory index html
