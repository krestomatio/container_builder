# Moodle
## Quick reference
- **Maintained by**:
[Krestomatio](https://krestomatio.com)
- **Where to get help**:
[Mono repo issue tracker](https://github.com/krestomatio/container_builder/issues)

## Variants and tags
- [moodle:4.1](#moodle41): `4.1, 4.1.19, moodle41-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-bundle](#moodle41-bundle): `4.1-bundle, 4.1.19-bundle, moodle41_bundle-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-httpd](#moodle41-httpd): `4.1-httpd, 4.1.19-httpd, moodle41_httpd24-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-kio](#moodle41-kio): `4.1-kio, 4.1.19-kio, moodle41_kio-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-nginx](#moodle41-nginx): `4.1-nginx, 4.1.19-nginx, moodle41_nginx120-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-nginx_php-fpm](#moodle41-nginx_php-fpm): `4.1-nginx_php-fpm, 4.1.19-nginx_php-fpm, moodle41_nginx120_php80-fpm-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.1-php-fpm](#moodle41-php-fpm): `4.1-php-fpm, 4.1.19-php-fpm, moodle41_php80-fpm-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5](#moodle45): `4.5, 4.5.5, moodle45-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-bundle](#moodle45-bundle): `4.5-bundle, 4.5.5-bundle, moodle45_bundle-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-httpd](#moodle45-httpd): `4.5-httpd, 4.5.5-httpd, moodle45_httpd24-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-kio](#moodle45-kio): `4.5-kio, 4.5.5-kio, moodle45_kio-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-nginx](#moodle45-nginx): `4.5-nginx, 4.5.5-nginx, moodle45_nginx126-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-nginx_php-fpm](#moodle45-nginx_php-fpm): `4.5-nginx_php-fpm, 4.5.5-nginx_php-fpm, moodle45_nginx126_php83-fpm-62f9cdca283987b077d0663c8430260985b2ad1b`
- [moodle:4.5-php-fpm](#moodle45-php-fpm): `4.5-php-fpm, 4.5.5-php-fpm, moodle45_php83-fpm-62f9cdca283987b077d0663c8430260985b2ad1b`


## Image Variants
### moodle:4.1
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle41)

This CentOS 9 Stream minimal based container image runs PHP 8.0 (default) or NGINX 1.20 for Moodle 4.1. Use it as an inmutable image packing Moodle source, (optionally) moodle plugins, and executables for php-fpm and nginx.

It includes a copy of Moodle source code, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set).

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.1.19
* Moodle version number: 2022112819.01
* Moodle commit: 4f61b2974b97f1c9a31022e750446fc52a6f416b
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
* Moodle version: 4.1.19
* Moodle version number: 2022112819.01
* Moodle commit: 4f61b2974b97f1c9a31022e750446fc52a6f416b
* Moodle remote branch: MOODLE\_401\_STABLE

#### Plugins
The following is the list of plugins:
- [mod_attendance](https://moodle.org/plugins/mod_attendance)
- [mod_checklist](https://moodle.org/plugins/mod_checklist)
- [mod_customcert](https://moodle.org/plugins/mod_customcert)
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
* Moodle version: 4.1.19
* Moodle version number: 2022112819.01
* Moodle commit: 95cf5ba2d9053e47490cc9836f5361930fa6e56b
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

### moodle:4.5
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45)

This CentOS 9 Stream minimal based container image runs PHP 8.3 (default) or NGINX 1.26 for Moodle 4.5. Use it as an inmutable image packing Moodle source, (optionally) moodle plugins, and executables for php-fpm and nginx.

It includes a copy of Moodle source code, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set).

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.5.5
* Moodle version number: 2024100705.02
* Moodle commit: 97ed6b7083cfb547c14ae3a2dcaf759079d48f66
* Moodle remote branch: MOODLE\_405\_STABLE

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
    --build-arg ARG_MOODLE_BRANCH='MOODLE_405_STABLE'
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
FROM quay.io/krestomatio/moodle:4.5

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

### moodle:4.5-bundle
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_bundle)

Extends [moodle:4.5](#moodle45) to add additional Moodle plugins.

#### Details
* Moodle remote repo: https://github.com/moodle/moodle.git
* Moodle version: 4.5.5
* Moodle version number: 2024100705.02
* Moodle commit: 97ed6b7083cfb547c14ae3a2dcaf759079d48f66
* Moodle remote branch: MOODLE\_405\_STABLE

#### Plugins
The following is the list of plugins:
- [mod_customcert](https://moodle.org/plugins/mod_customcert)

### moodle:4.5-httpd
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_httpd24)

Image based on CentOS 9 Stream minimal with [Apache HTTP Server](https://httpd.apache.org/) for Moodle app/source (not included)

### moodle:4.5-kio
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_kio)

Krestomatio Moodle variant

#### Details
* Moodle remote repo: https://github.com/krestomatio/moodle.git
* Moodle version: 4.5.5
* Moodle version number: 2024100705.01
* Moodle commit: 95518023c6216c1284b05377d673f8a5ebddeeb7
* Moodle remote branch: MOODLE\_405\_STABLE\_KIO

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

### moodle:4.5-nginx
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_nginx126)

Image based on CentOS 9 Stream minimal with [nginx HTTP Server](https://nginx.org/) for Moodle app/source (not included)

### moodle:4.5-nginx_php-fpm
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_nginx126_php83-fpm)

Image based on CentOS 9 Stream minimal with [nginx HTTP Server](https://nginx.org/) and [PHP-FPM](https://php-fpm.org/) for Moodle app/source (not included)

### moodle:4.5-php-fpm
> [Repo source](https://github.com/krestomatio/container_builder/tree/master/moodle/moodle45_php83-fpm)

Moodle PHP-FPM image based on CentOS 9 Stream minimal for Moodle app/source (not included)

