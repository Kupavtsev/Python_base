def adder(*args):
    print('adder = > ', end = ' ')
    if type(args[0]) == type(0):
        sum = 0
    else:
        sum = args[0][:0]
    for x in args:
        sum = sum + x
    return sum

def adder1(*args):
    print('adder1 => ', end = ' ')
    sum = args[0]    # Инициализировать значением первого аргумента
                    # для определения типа
    for i in args[1:]:
        sum += i
    return sum

for func in (adder, adder1):
    print(func(1, 2, 3))
    print(func('af', 'be', 'cb'))
    print(func([1,2], [3,4]))
