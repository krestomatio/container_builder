This CentOS 8 Stream minimal based container image runs PHP 7.4 or NGINX 1.18 for Moodle 3.9.

It includes a copy of Moodle source code, ready in the image public folder. A specific git commit is used to get the Moodle source version. That commit is fetch every build from remote repo to keep it up to date.  It is build from the latest available Moodle version (depending on the remote repo and branch set).

## Details

* Moodle version: 3.9.14
* Moodle version number: 2020061514.00
* Moodle commit: a63efe42d15236e08f10d9158eef5d20f92222db
* Moodle remote branch: MOODLE\_39\_STABLE


## Repository
This image is built from [this repo](https://github.com/krestomatio/container_builder/tree/master/moodle_web)
