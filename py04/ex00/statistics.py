from typing import Any


def mean(values, is_print=True):
    """Calculate the arithmetic mean of a list of numbers."""
    if len(values) < 1:
        print('ERROR')
        return None
    u = sum(values) / len(values)
    if is_print:
        print(f'mean : {u}')
    return u
    
def median(values, is_print=True):
    """Calculate the median of a list of numbers."""
    if len(values) < 1:
        print('ERROR')
        return None
    if len(values) % 2 == 0:
        m = (values[int((len(values)/2)) - 1 ] + values[(int(len(values)/2))]) / 2
    else:
        m = values[int((len(values) + 1) / 2) - 1]
    if is_print:
        print(f'median : {m}')
    return m

def var(values, is_print=True):
    """Calculate the variance of a list of numbers."""
    if len(values) < 1:
        print('ERROR')
        return None
    u = mean(values,is_print=False)
    o = sum([(x - u)**2 for x in values]) / len(values)
    if is_print:
        print(f'var : {o}')
    return o

def std(values):
    """Calculate the standard deviation of a list of numbers."""
    if len(values) < 1:
        print('ERROR')
        return None
    v = var(values,is_print=False)
    print(f'std : {v**0.5}') 

def quartile(values):
    """Calculate the first and third quartiles of a list of numbers."""
    if len(values) < 1:
        print('ERROR')
        return None
    length = len(values)
    half = int(length / 2)
    if length % 2 == 0:
        Q1 = median(values[0:half],is_print=False)
        Q3 = median(values[half:],is_print=False)
    else:
        Q1 = median(values[0:half + 1],is_print=False)
        Q3 = median(values[half:],is_print=False)
    print(f'quartile : [{Q1}, {Q3}]')

def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Process statistical calculations based on positional and keyword arguments."""
    
    if not all([isinstance(x,(int, float)) for x in args]):
        print("ERROR")
        return
    
    values = list(args)
    values.sort()
    for x in kwargs:
        match kwargs[x]:
            case "mean":
                mean(values)
            case "median":
                median(values)
            case "var":
                var(values)
            case "std":
                std(values)
            case "quartile":
                quartile(values)
            case _:
                pass
    