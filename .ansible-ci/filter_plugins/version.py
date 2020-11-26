# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
        author: Job Céspedes Ortiz <jobcespedes@krestomatio.com>
        version_added: "2.9"
        requirements:
            - semantic_version
"""

EXAMPLES = """
- vars:
    myversion: 0.0.1-prerelease-1
  debug:
    msg: |
      {{ myversion | next_version('major') }}
      {{ myversion | next_version('minor') }}
      {{ myversion | next_version }}
      {{ myversion | next_version_dict('major') }}
      {{ myversion | next_version_dict('minor') }}
      {{ myversion | next_version_dict }}
      {{ myversion | next_version_list('major') }}
      {{ myversion | next_version_list('minor') }}
      {{ myversion | next_version_list }}
"""

HAS_SEMATIC_VERSION = False
try:
    import semantic_version
    HAS_SEMATIC_VERSION = True
except ImportError:
    pass
from ansible.module_utils.six import string_types
from ansible.module_utils._text import to_text
from ansible.errors import AnsibleFilterError

def bump_version(v, bump):
    ''' Bump semantic version '''

    bump = bump.lower()
    if not isinstance(bump, string_types) or bump not in ['patch', 'minor', 'major']:
        raise AnsibleFilterError(
            'Bump paramater must be a string and one of "patch", "minor" or "major", not %s' % bump)

    # check v prefix
    if v.startswith('v'):
        v = v[1:]

    # Validate semver
    if not semantic_version.validate(v):
        raise AnsibleFilterError(
            'Value "%s" is not a proper semantic version' % v)

    # bump
    v = semantic_version.Version(v)
    if bump:
        v = getattr(v, 'next_' + bump)()

    return v

def next_version(v, bump='patch'):
    ''' Get next semantic version as a string
        Args:
            bump (str): Which semantic version part to bump
        Raises:
            errors.AnsibleFilterError: If 'bump' is not 'major', 'minor'
            or 'patch'
        Returns:
            str: Next semantic version
    '''
    v = bump_version(to_text(v), bump)
    return v

def next_version_dict(v, bump='patch'):
    ''' Get next semantic version as a dictionary
        Args:
            bump (str): Which semantic version part to bump
        Raises:
            errors.AnsibleFilterError: If 'bump' is not 'major', 'minor'
            or 'patch'
        Returns:
            dict: Next semantic version as a dictionary
    '''
    v = bump_version(to_text(v),bump)
    v = {
        "full": str(v),
        "major": v.major,
        "minor": v.minor,
        "patch": v.patch,
        "prerelease": '.'.join(v.prerelease),
        "build": '.'.join(v.build)
    }
    return v

def next_version_list(v, bump='patch'):
    ''' Get next semantic version as a list
        Args:
            bump (str): Which semantic version part to bump
        Raises:
            errors.AnsibleFilterError: If 'bump' is not 'major', 'minor'
            or 'patch'
        Returns:
            list: Next semantic version as a list
    '''
    v = bump_version(to_text(v),bump)
    v = [str(v)] + list(v)
    return v

# ---- Ansible filters ----
class FilterModule(object):
    ''' Semantic version filter '''

    def filters(self):
        return {
            'next_version': next_version,
            'next_version_dict': next_version_dict,
            'next_version_list': next_version_list
        }
