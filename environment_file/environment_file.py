"""
Environment File
"""
import os
import json
from pathlib import Path


def get_variable(variable_name, default=None, required=False):
    """
    Loads an environment variable.
    Falls back to check in the user's home directory for an env file.
    It will load the variable from that file if it exists.
    """
    value = os.environ.get(variable_name)

    if value is not None:
        try:
            env_dir = os.path.join(str(Path.home()), 'ENV.json')
        except AttributeError:
            env_dir = None

        if env_dir:

            with open(env_dir) as data_file:
                data = json.load(data_file)
                value = data.get(variable_name)

    if value is None:
        value = default

    if value is None and required:
        raise Exception(
            'The environment variable %s is required '
            'for this application to run.' % (
                variable_name,
            )
        )

    return value
