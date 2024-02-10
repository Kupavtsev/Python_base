var = 99

def local():
    var = 0

def glob1():
    global var 
    var =+ 1

def glob2():
    var = 0
    import test
    glob.var += 1

def glob3():
    var = 0
    import sys
    glob = sys.modules['thismod']

    glob.var +=1 

def test():
    print(var)
    local(); glob1(); glob2(); glob3()
    print(var)

# ====================================
X = 99

def geotest():
    import __main__
    print(__main__.X)
    X = 77
    print(X)

def gorlik(x=[]):
    x.append(1)
    print(x)

def gitr(x=None):
    # x = x or []
    if x is None:
        x = []
    x.append(1)
    print(x)


# gitr([2])
# gitr([3])
# gitr()
# gitr()
# gitr()
# gitr([5])

def saver():
    saver.x.append(1)
    print(saver.x)

saver.x = []
saver()
saver()
saver()