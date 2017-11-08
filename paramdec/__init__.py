"""
Parametrized decorator
"""


from functools import wraps


def paramdec(decorator):
    """
    Parametrized decorator

    :param decorator: decorator that will be parametrized
    :return: parametrized decorator
    """
    @wraps(decorator)
    def wrapper(*args, **kwargs):
        without_params = len(args) == 1 and callable(args[0]) and not kwargs
        if without_params:
            return decorator(args[0])
        else:
            return lambda real_func: decorator(real_func, *args, **kwargs)
    return wrapper