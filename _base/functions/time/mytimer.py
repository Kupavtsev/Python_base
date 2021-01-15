import time, sys


# Third Version

trace = lambda *args: None  # or print
timefunc = time.clock if sys.platform == 'win32' else time.time

def timer(func, *pargs, _reps=1000, **kargs):
    trace(func, pargs, kargs, _reps)
    # page 593


'''
# Second version

if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time

def trace(*args): pass      # Заглушка: вывод аргументов

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)    # Полученное число повторов или значение по умолчанию

    trace(func, pargs, kargs, _reps)
    replist = range(_reps)

    start = timefunc()
    for i in replist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, **kargs ):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    for i in range(_reps):
        (time, ret) = timer(func, *pargs, _reps=1, **kargs)
        if time < best: best = time
    return (best, ret)
'''



'''
# First Version
reps = 1000
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)
'''


# Version for http://pythontutor.com/visualize.html#mode=edit

'''

import time
reps = 2
repslist = range(reps)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)
    
def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return x

def listComp():
    return [abs(x) for x in repslist]

def mapCall():
    return list(map(abs(x), repslist))

def genExpr():
    return list(abs(x) for x in repslist)

def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())
    

for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print('-' * 33)
    print('%-9s => %.2f' % (test.__name__, elapsed))

'''