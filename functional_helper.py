import functools


def identity(x):
    return x


def comp(functions):
    return functools.reduce(lambda f, g: lambda x: g(f(x)), functions, identity)
