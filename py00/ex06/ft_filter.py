def ft_filter(filter_function, iterable):
    return [n for n in iterable if filter_function(n)]

