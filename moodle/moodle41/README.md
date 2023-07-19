### moodle:4.1
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41)

This CentOS 9 Stream minimal based container image runs PHP 8.0 (default) or NGINX 1.20 for Moodle 4.1. Use it as an inmutable image packing Moodle source, (optionally) moodle plugins, and executables for php-fpm and nginx.

It includes a copy of Moodle source code, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set).

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.1.4
* Moodle version number: 2022112804.06
* Moodle commit: 272fdb321a421f72aef696a3b4a78dbf477d483b
* Moodle remote branch: MOODLE\_401\_STABLE

#### Custom builds
This Dockerfile allows setting OS extra packages, Moodle remote repo, Moodle repo branch and/or additional Moodle plugins. For that purpose, use build args to customize the build as you need.

##### Extra packages
For building with OS extra packages, use `ARG_INSTALL_EXTRA_PKGS`:
```
docker build . -t my_moodle_image:my_tag \
    --build-arg ARG_INSTALL_EXTRA_PKGS='php-xdebug php-mysqlnd'
```

##### Moodle remote
For building from a different Moodle remote, use `ARG_MOODLE_REMOTE`:
```
docker build . -t my_moodle_image:my_tag \
    --build-arg ARG_MOODLE_REMOTE='https://github.com/moodle/moodle.git'
```

##### Moodle branch
For building from a different Moodle branch, use `ARG_MOODLE_BRANCH`:
```
docker build . -t my_moodle_image:my_tag \
    --build-arg ARG_MOODLE_BRANCH='MOODLE_401_STABLE'
```

##### Moodle plugins
For installing plugins while building the main Dockerfile (slower), use `ARG_MOODLE_PLUGIN_LIST`:
```
docker build . -t my_moodle_image:my_tag \
    --build-arg ARG_MOODLE_PLUGIN_LIST=''
```
For building only to install additional moodle plugins (faster), create a Dockerfile like the following and then build.
Example of `Dockerfile.plugins`:
```dockerfile
# Dockerfile.plugins
FROM quay.io/krestomatio/moodle:4.1

# Install additional plugins, a space separated arg, (if any)
# Argument is also a mechanism to invalidate cache if changed
ARG ARG_MOODLE_PLUGIN_LIST=""
ENV MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST}
RUN if [ -n "${MOODLE_PLUGIN_LIST}" ]; then /usr/libexec/moodle/install-plugin-list -p "${MOODLE_PLUGIN_LIST}"; fi && \
    rm -rf /tmp/moodle-plugins
```
Example of build using `Dockerfile.plugins`:
```
# Build
docker build . -t my_moodle_image:my_tag \
    -f Dockerfile.plugins \
    --build-arg ARG_MOODLE_PLUGIN_LIST=''
```

#### PHP-FPM or NGINX
The image packs both programs: PHP-FPM and Nginx. However, it only runs one, with a non-root user. This design is for those programs to run in different containers, using one image. By default, in a Kubernetes cluster, it runs php-fpm with user 48. For nginx, set pod args to 'nginx' and run it as user 999. For a OKD cluster, setting args to `nginx` will suffice.
##### Configuration files
For adjusting PHP-FPM or Nginx config, just place the .ini or .conf files in the respective folders.
- `/etc/php.d/`: PHP .ini extra configuration
- `/etc/php-fpm.d/`: PHP-FPM .conf extra configuration
- `/etc/nginx/default.d/`: Nginx .conf server extra configuration
