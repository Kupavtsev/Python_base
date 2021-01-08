def f1(a, b): print(a, b)
def f2(a, *b): print(a, b)
def f3(a, **b): print(a, b)
def f4(a, *b, **c): print(a, b, c)
def f5(a, b=2, c=3): print(a, b, c)
def f6(a, b=2, *c): print(a, b, c)

print(f1(1, 2))
print(f1(b=2, a=1))

print(f2(1, 2, 3))
print(f3(1, x=2, y=3))
print(f4(1, 2, 3, x=2, y=3))

print(f5(1))
print(f5(1, 4))

print(f6(1))
print(f6(1, 3, 4))
