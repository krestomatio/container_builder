This CentOS 8 Stream minimal based container image runs PHP ${PHP_VERSION} or NGINX ${NGINX_VERSION} for Moodle 3.9.

It includes a copy of Moodle source, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set)

Moodle remote branch: MOODLE_39_STABLE
Moodle commit: bb743c23587c30177880422ce36212c90ce6f40b
Moodle version: 3.9.12
Moodle version number: 2020061512.03


## Repository
This image is built from [this repo](https://github.com/krestomatio/container_builder/tree/master/moodle_web)
