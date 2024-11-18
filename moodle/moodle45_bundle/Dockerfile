# Ansible managed
ARG ARG_IMAGE_FROM=quay.io/krestomatio/moodle:4.5
FROM ${ARG_IMAGE_FROM}

# Install additional plugins, a space separated arg, (if any)
# Argument is also a mechanism to invalidate cache if changed
ARG ARG_MOODLE_PLUGIN_LIST="mod_customcert"
ENV MOODLE_PLUGIN_LIST=${ARG_MOODLE_PLUGIN_LIST}
RUN if [ -n "${MOODLE_PLUGIN_LIST}" ]; then /usr/libexec/moodle/install-plugin-list -p "${MOODLE_PLUGIN_LIST}"; fi && \
  rm -rf /tmp/moodle-plugins
