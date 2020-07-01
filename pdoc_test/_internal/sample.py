""" Some internal sample module """

from .interface import MyInterface


MY_VAR = 10
"""This is my variable"""

def my_function(iface: MyInterface) -> str:
    """My function doc

    Args:
        iface: interface parameter doc

    Returns:
        return value doc
    """    

    return ''