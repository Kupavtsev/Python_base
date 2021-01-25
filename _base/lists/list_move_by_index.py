# Находит по индексу элемент в Массиве, передвигаясь по 
# элементам массива
# Который соответствует выражению 2 ** Х
L = [1, 2, 4, 8, 16, 32, 64]
X = 5

found = False
i = 0

while not found and i < len(L):
    if 2 ** X == L[i]:
        found = 1
    else:
        i += 1

if found:
    print('at index', i)
else:
    print(X, 'not found')

print('--------2--------')
# b
# Проверяет наличие результат этого же выражения в Массиве

for x in L:
    if 2 ** X == x:
        print('at index: ', L.index(x))
    else:
        print(2 ** X, 'not found at ', L.index(x))

print('--------3--------')
# c

if 2 ** X in L:
    print('at position ', L.index(2 ** X))

print('--------4--------')
# d

L = []

for x in range(1,7):
    L.append(2 ** x)