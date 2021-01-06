def myzip(*args):
    iters = list(map(iter, args))
    while iters:
        res = [next(i) for i in iters]
    yield tuple(res)
    
a = 'abc'
b = 'zxynop'

print(list(myzip(a, b)))