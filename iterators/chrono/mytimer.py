import time, sys

if sys.platform[:3] == 'win':
    timefunc = time.perf_counter
else:
    timefunc = time.time


def trace(*args): pass

def timer(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 1000)

    trace(func, pargs, kargs, _reps)
    replist = range(_reps)

    start = timefunc()
    for i in replist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret)

def best(func, *pargs, **kargs):
    _reps = kargs.pop('_reps', 50)
    best = 2 ** 32
    (time, ret) = timer(func, *pargs, _reps=1, **kargs)
    if time < best: best = time
    return (best, ret)
