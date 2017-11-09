"""
Paramdec
========

This module provides a convenient way to create parametrized decorators:

    Create your decorator:

    >>> from paramdec import paramdec
    >>> @paramdec
    ... def my_dec(func, *dec_args, **dec_kwargs):
    ...     def wrapper(*func_args, **func_kwargs):
    ...         # Process dec_args and dec_kwargs
    ...         return func(*func_args, **func_kwargs)
    ...     return wrapper

    Use it with parameters:

    >>> @my_dec(42, foo="bar")
    >>> def func(): pass

    Or without parameters:

    >>> @my_dec  # No parentheses required
    >>> def func(): pass

    For more info checkout github repo <https://github.com/Suenweek/paramdec>.
"""


from collections import namedtuple


Author = namedtuple("Author", ["name", "email"])


authors = [
    Author("Roman Novatorov", "suenweek@protonmail.com")
]


__version__ = "2.0.0"
__author__ = ", ".join("%s <%s>" % author for author in authors)


from .paramdec import paramdec


__all__ = ("paramdec",)
