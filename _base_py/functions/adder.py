def adder(*args):
    # print('adder = > ', end = ' ')
    if type(args[0]) == int:
        sum = 0
    else:
        sum = args[0][:0]   # S[:0], возвращает пустую последовательность того же типа, что и S
    for x in args:
        sum = sum + x
    return sum

def adder1(*args):
    # print('adder1 => ', end = ' ')
    sum = args[0]    # Инициализировать значением первого аргумента
                    # для определения типа
    for i in args[1:]:
        sum += i
    return sum

def check():
    for func in (adder, adder1):
        print(func.__name__, func(1, 2, 3))
        print(func.__name__, func('af', 'be', 'cb'))
        print(func.__name__, func([1,2], [3,4]))

# check()

def copyDict(kargs):
    newDict = {}
    print(type(kargs))
    # for key, val in kargs.items():
    #     newDict[key] = val
    for key in kargs.keys():
        newDict[key] = kargs[key]
    return newDict

ex_dict = {"1": 'a', '2': 'b', '3': 'c'}
new_dict = copyDict(ex_dict)
# new_replica = ex_dict[:]

ex_dict['hello'] = 143

for each in (ex_dict, new_dict):
    print(each)