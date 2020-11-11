# Ansible managed
FROM quay.io/krestomatio/httpd

# General variables
ENV IMAGE_name="moodle_httpd" \
    IMAGE_summary="Apache ${HTTPD_version} for Moodle 3.9" \
    IMAGE_description="This CentOS 8 minimal based container image runs Apache ${HTTPD_version} for Moodle 3.9" \
    IMAGE_title="Apache ${HTTPD_version} for Moodle3.9 " \
    TZ="UTC"

# Component bash variables
ENV MOODLE_version="3.9" \
    MOODLE_ver_short="39" \
    MOODLE_commit="a8e089a8c86fa2a7a04a2f4adf39de4bbd188975" \
    MOODLE_app=${APP_dest} \
    MOODLE_data=/var/moodledata \
    MOODLE_check_path=/login/index.php \
    MOODLE_check_code="200" \
    MOODLE_check_host=localhost

USER 0

COPY conf/usr/bin/* /usr/bin/
COPY conf/usr/libexec/* /usr/libexec/

RUN container-setup

RUN container-setup-httpd-moodle

USER ${CTR_user_id}

# Labels
LABEL name="${IMAGE_name}" \
      summary="${IMAGE_summary}" \
      description="${IMAGE_description}" \
      maintainer="Job Céspedes Ortiz <jobcespedes@gmail.com>" \
      org.opencontainers.image.title="${IMAGE_title}" \
      org.opencontainers.image.description="${IMAGE_description}" \
      org.opencontainers.image.version="0.0.4" \
      io.k8s.description="${IMAGE_description}" \
      io.k8s.display-name="${IMAGE_title}" \
      io.openshift.tags="${IMAGE_name},apache,apache${HTTPD_ver_short},apache-${HTTPD_ver_short},moodle,moodle${MOODLE_ver_short},moodle-${MOODLE_ver_short}"
