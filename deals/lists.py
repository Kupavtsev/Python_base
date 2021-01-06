
mar14t = {'open': 58.35, 'high': 58.74, 'low': 58, 'close': 58.53}

for pos in mar14t.values():
    print(pos)



mar14 = [58.35, 58.74, 58, 58.53]
mar15 = [58.51, 58.95, 57.74, 58.39]
mar18 = [58.75, 59.54, 58.37, 59.28]
mar19 = [59.31, 59.86, 58.89, 59.29]
mar20 = []

print(mar20)

from functools import reduce


result = reduce(lambda x, y: x + y, mar19)
print(result)

print(list(filter(lambda v: v > 59 and v < 59.50, [59.31, 59.86, 58.89, 59.29])))

import random
print(random.randint(49, 58))

'''

def mar20(**kwargs):
    print(type(kwargs))
    return print(kwargs)

x = mar20(open=59.29, high=60.28, low=58.56, close=59.99)
'''

'''

mar19 = (59.31, 59.86, 58.89, 59.29, 'hello')
print(mar19)
print(type(mar19))

try:
    new_tuple = tuple()
    for item in mar19:
        if not isinstance(item, str):
            new_tuple += (item, )
    print(item)
except TypeError:
    print('Syntax')            
except NameError:
    print('Name Error')

print('this is what ? {}'.format(new_tuple))

'''

#while mar14[-1] > mar15[0]:
#    print(mar14[-1] - 0.01)
#    mar15[0] += 0.01

'''
print(mar14[0])

for ohlc in mar14:
    print(ohlc)

print(mar20)

open = input('Enter the Open: ')
mar20.append(open)
print(mar20)
high = input('Enter the high: ')
mar20.append(high)
print(mar20)
low = input('Enter the low: ')
mar20.append(low)
print(mar20)
close = input('Enter the close: ')
mar20.append(close)
print(mar20)


mar20.append(59.29)
mar20.append(60.28)
mar20.append(58.56)
mar20.append(59.99)

print(mar20)

print('This is open of 20 March', mar20[0])
'''