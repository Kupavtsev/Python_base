def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    
    return new

def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new


# 5th
def copyDict2(dict):
    dict2 = dict.copy()
    return dict2
    
dict1 = {1 : 10, 2 : 20, 3 : 30}
dict2 = {4 : 40, 5 : 50, 1 : 60}


# _______________ 7 ________________________

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
