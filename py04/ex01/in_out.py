def square(x: int | float) -> int | float:
    """Return the square of x."""
    return x ** 2

def pow(x: int | float) -> int | float:
    """Return x raised to the power of x."""
    return x ** x

def outer(x: int | float, function) -> object:
    """Return a closure that applies function to x and accumulates the result."""
    count = 0
    def inner() -> float:
        """Apply function to the current value of x and return the result."""
        nonlocal count
        result = x
        count += 1
        for i in range(count):
            result = function(result)
        return result
    return inner
        


