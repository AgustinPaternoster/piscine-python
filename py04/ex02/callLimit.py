from typing import Any


def callLimit(limit: int):
    """Decorator that limits how many times a function can be called.

    Args:
        limit: Maximum number of times the decorated function can be called.

    Returns:
        A decorator that wraps the function and tracks call count.
    """
    count = 0

    def callLimiter(function):
        def limit_function(*args: Any, **kwds: Any):
            nonlocal count
            if count >= limit:
                print(f'Error: {function} call too many times')
                return
            function(*args, **kwds)
            count += 1
        return limit_function

    return callLimiter
    