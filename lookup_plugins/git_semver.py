# python 3 headers, required if submitting to Ansible
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = """
        lookup: git_semver
        author: Job Céspedes <jobcespedes@gmail.com>
        version_added: "2.9"
        short_description: get/bump version from git current branch latest tag
        requirements:
            - semantic_version
        description:
            - This lookup returns/bump the version from git current branch latest tag
        options:
            _terms:
                description: path of repo
                required: True
            bump:
                description:
                    - increase/bump version number: major, minor, patch
                default: ''
                type: string
                required: False
                choices: ['major', 'minor', 'patch']
            want:
                description:
                    - return str,list or dict
                default: str
                type: string
                required: False
                choices: ['str', 'dict', 'list']
"""

EXAMPLES = """
- vars:
    version: "{{ lookup('git_semver', playbook_dir) }}"
    version_image_patch: "{{ lookup('git_semver', playbook_dir, bump='patch') }}"
    version_image_minor: "{{ lookup('git_semver', playbook_dir, bump='minor') }}"
    version_image_major: "{{ lookup('git_semver', playbook_dir, bump='major') }}"
    version_list: "{{ lookup('git_semver', playbook_dir, want='list') }}"
    version_dict: "{{ lookup('git_semver', playbook_dir, want='dict') }}"
  debug:
    msg:  |
      {{ version }}
      {{ version_image_patch }}
      {{ version_image_minor }}
      {{ version_image_major }}
      {{ version_list }}
      {{ version_dict}}
"""

RETURN = """
_raw:
    description:
      - version from git current branch latest tag
    type: str
_dict:
    description:
      - dictionary with break down version from git current branch latest tag:
        {'full','major','minor','patch','prerelease','build'}
    type: dcit
_list:
    description:
      - list with break down version from git current branch latest tag:
        ['full','major','minor','patch','prerelease','build']
    type: list

"""
import os
import semantic_version
import git
from git import Repo
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.plugins.lookup import LookupBase
from ansible.utils.display import Display


display = Display()


class LookupModule(LookupBase):

    def run(self, terms, variables=None, **kwargs):

        bump = kwargs.get('bump', '').lower()
        if not isinstance(bump, string_types) or bump not in ['patch', 'minor', 'major', '']:
            raise AnsibleError(
                '"bump" must be a string and one of "patch", "minor" or "major", not %s' % bump)

        want = kwargs.get('want', 'str').lower()
        if not isinstance(want, string_types) or want not in ['str', 'dict', 'list']:
            raise AnsibleError(
                '"want" must be a string and one of "str", "dict" or "list", not %s' % want)

        ret = []
        for term in terms:
            display.debug("Repo path: %s" % term)
            repo = Repo(term)

            display.vvvv(u"Git semver lookup using %s as repo" % repo)
            try:
                if repo:
                    # gheck this is a git repo
                    assert not repo.bare

                    # get branch name
                    branch = repo.git.branch('--show-current')

                    # get tag
                    try:
                        # get tag
                        v = repo.git.describe('--tags', '--abbrev=0')
                        # set tag as rev
                        rev = v
                    except git.GitCommandError as e:
                        # initialize semantic version if error code 128
                        if e.status == 128 and ('No names' in e.stderr or 'No tags' in e.stderr):
                            # set default initial semver
                            v = '0.0.0' + '-SNAPSHOT-' + \
                                os.getenv('BRANCH_NAME', branch) + \
                                '-' + os.getenv('BUILD_ID', repo.git.describe('--always'))
                            # set HEAD as rev
                            rev = 'HEAD'
                        else:
                            raise

                    # set commit
                    commit = repo.git.rev_parse(rev)

                    # check v prefix
                    if v.startswith('v'):
                        v = v[1:]

                    # Validate semver
                    if not semantic_version.validate(v):
                        raise AnsibleError(
                            'Tag "%s" is not a proper semantic version' % v)

                    # bump
                    v = semantic_version.Version(v)
                    if bump:
                        v = getattr(v, 'next_' + bump)()

                    # return dict
                    if want == 'dict':
                        v = {
                            "full": str(v),
                            "major": v.major,
                            "minor": v.minor,
                            "patch": v.patch,
                            "prerelease": '.'.join(v.prerelease),
                            "build": '.'.join(v.build),
                            "branch": branch,
                            "commit": commit
                        }

                    # return list
                    if want == 'list':
                        v = [str(v)] + list(v) + [branch] + [commit]

                    # return str
                    if want == 'str':
                        v = str(v)

                    ret.append(v)
                else:
                    raise AnsibleParserError()
            except AnsibleParserError:
                raise AnsibleError(
                    "could not get version in lookup: %s" % term)

        return ret
