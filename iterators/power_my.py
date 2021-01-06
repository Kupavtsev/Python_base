L = [1, 2, 4, 8, 16, 32, 64]
X = 5





# a

i = 0   

while i < len(L):
    if 2 ** X == L[i]:
        print('at index', i)
        break
    else:
        i += 1
else:
    print(X, 'not found')        

# b

for x in L:
    if 2 ** X == x:
        print('at index: ', L.index(x))
    else:
        print(2 ** X, 'not found at ', L.index(x))

# c

if 2 ** X in L:
    print('at position ', L.index(2 ** X))

# d

L = []

for x in range(1,7):
    L.append(2 ** x)

