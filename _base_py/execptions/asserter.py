def f(x):
    assert x < 0, 'x must be negative'      # AssertionError: x must be negative
    return x ** 2


print(f(1))