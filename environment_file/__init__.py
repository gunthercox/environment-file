"""
Package information for the Environment File module.
"""

__version__ = '1.0.0'
__author__ = 'Gunther Cox'
__email__ = 'gunthercx@gmail.com'
__url__ = 'https://github.com/gunthercox/environment-file'
__download__ = '{}/tarball/{}'.format(__url__, __version__)

from .environment_file import get_variable

__all__ = [
    'get_variable'
]
