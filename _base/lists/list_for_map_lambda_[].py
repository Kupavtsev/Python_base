#Functions task 9
import math

L = [2, 4, 9, 16, 25]

#1
# square root
for x in L:
    print(math.sqrt(x))

print('--------2----------')
#2
# Мапинг вместо цикла for, и создание итератора
t = (map(math.sqrt, L))
print(next(t))
print(next(t))
print(next(t))
# Массив оставшихся элементов
print(list(t))

print('------------------')
# Создаем переменную х, применяем к ней sqrt и мапим по L
r = map((lambda x: math.sqrt(x)), L)
print(list(r))

print('---------3---------')
#3
b = [math.sqrt(x) for x in L]
print(list(b))

#4
print('---------4---------')
if 4**2 in L:
    print('4^2 in L', 4**2)