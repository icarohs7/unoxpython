"""
Utils for validation
"""

# noinspection PyUnusedFunction
from typing import Iterable
from unoxpython import Predicate, T


# noinspection PyUnusedFunction
def require(checked: T, predicate: Predicate) -> T:
    """
    Verify if the given value passes the predicate,
    if it does, return the value, else raise an Exception

    :param checked: Value to be checked
    :param predicate: Predicate that will check the value
    :return: The value if the predicate returns true when operated
            against it
    """
    assert predicate(checked), "Predicate must be true to pass"
    return checked


# noinspection PyUnusedFunction
def require_not_empty(value: Iterable[T]) -> T:
    """
    Verify if the given iterable arg is not empty
    or blank, in the case of strings and return
    it, if not, else raise an exception

    :param value: The iterable to be validated
    :return: The iterable passed or raise an exception
            if it's empty
    """
    checked = value.replace(" ", "") if type(value) is str else value
    return require(checked, lambda it: len(it) > 0)
