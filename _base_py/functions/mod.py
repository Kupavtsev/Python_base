def adder1(*args):
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder2(**args):
    # print('adder2 = > ', end = ' ')
    argkeys = list(args.keys())
    tot = argkeys[0]
    for key in argkeys[1:]:
        tot += key
    return tot

def adder3(**args):
    # print('adder3 = > ', end = ' ')
    args = list(args.values())
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder4(**args):
    return adder1(*args.values())


for func in (adder2, adder4):
    print(func.__name__, ': ' )
    print(func(good = 10, bad = 20, ugly = 30))
    print(func(a = 'spam', b = 'tot', c = 'nyse'))
    


# test = copyDict(dict1)
# print(test)