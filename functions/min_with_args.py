def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < args[0]:
            res = arg
    return res

def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first

def min3(*args):
    l = list(args)
    l.sort()
    
    return l[0]

def minmax(test, *args):
    res = args[0]
    for arg in args[1:]:
        if test(arg, res):
            res = arg
    return res
        

def lessthan(x, y): return x < y
def gtrthan(x, y): return x > y

print(minmax(lessthan, 4,5,6,2,3,4,8,1))
print(minmax(gtrthan, 4,5,6,2,3,4,8,1))