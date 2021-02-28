def adder1(*args):
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot


def adder2(**args):
    print('adder = > ', end = ' ')
    argkeys = list(args.keys())
    tot = argkeys[0]
    for key in argkeys[1:]:
        tot += key
    return tot

def adder3(**args):
    print('adder1 = > ', end = ' ')
    args = list(args.values())
    tot = args[0]
    for arg in args[1:]:
        tot += arg
    return tot

def adder4(**args):
    return adder1(*args.values())


for func in (adder1, adder2):
    print(func(good = 10, bad = 20, ugly = 30))
    print(func(a = 'spam', b = 'tot', c = 'nyse'))
    


test = copyDict(dict1)
print(test)