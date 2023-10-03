## Quick reference
- **Maintained by**:
[Krestomatio](https://github.com/krestomatio)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [moodle:4.1](#moodle41): `4.1, 4.1.5, moodle41-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-bundle](#moodle41-bundle): `4.1-bundle, 4.1.5-bundle, moodle41_bundle-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-httpd](#moodle41-httpd): `4.1-httpd, 4.1.5-httpd, moodle41_httpd24-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-kio](#moodle41-kio): `4.1-kio, 4.1.5-kio, moodle41_kio-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-nginx](#moodle41-nginx): `4.1-nginx, 4.1.5-nginx, moodle41_nginx120-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-nginx_php-fpm](#moodle41-nginxphp-fpm): `4.1-nginx_php-fpm, 4.1.5-nginx_php-fpm, moodle41_nginx120_php80-fpm-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`
- [moodle:4.1-php-fpm](#moodle41-php-fpm): `4.1-php-fpm, 4.1.5-php-fpm, moodle41_php80-fpm-47ceefa8b3b6c942747da3b18bb8d5a7bdfdba8a`


## Image Variants
### moodle:4.1
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41)

This CentOS 9 Stream minimal based container image runs PHP 8.0 (default) or NGINX 1.20 for Moodle 4.1. Use it as an inmutable image packing Moodle source, (optionally) moodle plugins, and executables for php-fpm and nginx.

It includes a copy of Moodle source code, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set).

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.1.5
* Moodle version number: 2022112805.12
* Moodle commit: b3ea1a9d5b1393c4135d8281eebbee0a6f41b171
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
The image packs both programs: PHP-FPM and Nginx. However, it only runs one, with a non-root user. This design is for those programs to run in different containers, using one image. By default, in a Kubernetes cluster, it runs php-fpm with user 48. For nginx, set pod args to 'nginx' and run it as user 1001. For a OKD cluster, setting args to `nginx` will suffice.
##### Configuration files
For adjusting PHP-FPM or Nginx config, just place the .ini or .conf files in the respective folders.
- `/etc/php.d/`: PHP .ini extra configuration
- `/etc/php-fpm.d/`: PHP-FPM .conf extra configuration
- `/etc/nginx/default.d/`: Nginx .conf server extra configuration

### moodle:4.1-bundle
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_bundle)

Extends [moodle:4.1](#moodle41) to add additional Moodle plugins.

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.1.5
* Moodle version number: 2022112805.12
* Moodle commit: b3ea1a9d5b1393c4135d8281eebbee0a6f41b171
* Moodle remote branch: MOODLE\_401\_STABLE

#### Plugins
The following is the list of plugins:
- [mod_attendance](https://moodle.org/plugins/mod_attendance)
- [mod_checklist](https://moodle.org/plugins/mod_checklist)
- [block_checklist](https://moodle.org/plugins/block_checklist)
- [gradeexport_checklist](https://moodle.org/plugins/gradeexport_checklist)

### moodle:4.1-httpd
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_httpd24)

Image based on CentOS 9 Stream minimal with [Apache HTTP Server](https://httpd.apache.org/) for Moodle app/source (not included)

### moodle:4.1-kio
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_kio)

Krestomatio Moodle variant

#### Details
* Moodle remote repo: https://github.com/krestomatio/moodle.git
* Moodle version: 4.1.5
* Moodle version number: 2022112805.12
* Moodle commit: 53f9ca8bd0ddb83f37e4174653235c5158172df0
* Moodle remote branch: MOODLE\_401\_STABLE\_KIO

#### Plugins
The following is the list of plugins:
- [block_checklist](https://moodle.org/plugins/block_checklist)
- [block_completion_progress](https://moodle.org/plugins/block_completion_progress)
- [block_xp](https://moodle.org/plugins/block_xp)
- [format_tiles](https://moodle.org/plugins/format_tiles)
- [format_onetopic](https://moodle.org/plugins/format_onetopic)
- [format_grid](https://moodle.org/plugins/format_grid)
- [format_topcoll](https://moodle.org/plugins/format_topcoll)
- [gradeexport_checklist](https://moodle.org/plugins/gradeexport_checklist)
- [mod_questionnaire](https://moodle.org/plugins/mod_questionnaire)
- [mod_attendance](https://moodle.org/plugins/mod_attendance)
- [mod_checklist](https://moodle.org/plugins/mod_checklist)
- [mod_customcert](https://moodle.org/plugins/mod_customcert)
- [mod_zoom](https://moodle.org/plugins/mod_zoom)
- [mod_game](https://moodle.org/plugins/mod_game)
- [theme_moove](https://moodle.org/plugins/theme_moove)
- [theme_boost_union](https://moodle.org/plugins/theme_boost_union)
- [auth_oidc](https://moodle.org/plugins/auth_oidc)
- [block_microsoft](https://moodle.org/plugins/block_microsoft)
- [local_o365](https://moodle.org/plugins/local_o365)
- [local_office365](https://moodle.org/plugins/local_office365)
- [repository_office365](https://moodle.org/plugins/repository_office365)
- [theme_boost_o365teams](https://moodle.org/plugins/theme_boost_o365teams)
- [local_onenote](https://moodle.org/plugins/local_onenote)
- [assignfeedback_onenote](https://moodle.org/plugins/assignfeedback_onenote)
- [assignsubmission_onenote](https://moodle.org/plugins/assignsubmission_onenote)
- [plagiarism_turnitin](https://moodle.org/plugins/plagiarism_turnitin)
- [plagiarism_turnitinsim](https://moodle.org/plugins/plagiarism_turnitinsim)

### moodle:4.1-nginx
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_nginx120)

Image based on CentOS 9 Stream minimal with [nginx HTTP Server](https://nginx.org/) for Moodle app/source (not included)

### moodle:4.1-nginx_php-fpm
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_nginx120_php80-fpm)

Image based on CentOS 9 Stream minimal with [nginx HTTP Server](https://nginx.org/) and [PHP-FPM](https://php-fpm.org/) for Moodle app/source (not included)

### moodle:4.1-php-fpm
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41_php80-fpm)

Moodle PHP-FPM image based on CentOS 9 Stream minimal for Moodle app/source (not included)

