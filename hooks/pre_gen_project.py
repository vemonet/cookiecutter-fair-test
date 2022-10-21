#!/usr/bin/env python

"""Code to run before generating the project.

Adapted from https://github.com/audreyfeldroy/cookiecutter-pypackage/blob/master/hooks/pre_gen_project.py.
"""

import re
import sys

REPO_REGEX = re.compile(r'^[-a-zA-Z][-a-zA-Z0-9]+$')

repo_name = '{{cookiecutter.package_name}}'

if not REPO_REGEX.match(repo_name):
    print(
        f'ERROR: {repo_name} is not a valid repository name. Please do not use a _ and use - instead'
    )

    # Exit to cancel project
    sys.exit(1)
