""" pdoc-test """

# version information
__version__ = '0.0.1'

# Add the public API by importing just the API symbols from ._internal.XXX

from ._internal.interface import MyInterface
from ._internal.sample import MY_VAR, my_function

__all__ = ['MyInterface', 'MY_VAR', 'my_function']
