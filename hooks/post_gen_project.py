#!/usr/bin/env python

"""Code to run after generating the project."""

# import os
# import pathlib
# import shutil
from pathlib import Path

repo_folder = f"{{ cookiecutter.package_name }}"

print(f"\nā Your repository for defining FAIR tests have been initialized in \033[1m{repo_folder}\033[0m")
print("\nš To start the API with docker, run:")
print(f"cd {repo_folder}")
print("docker-compose up")

print("\nšļø  And check the README.md for more details on the development workflow")