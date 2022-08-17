S = 'string'
SL = []
for el in S:
    SL.append(ord(el))

print(sum(SL))

S = list(map(ord, S))
print(S)

D = dict(a=1, d=3, z=6, b=2, c=4)
print(sorted(D))
# D = sorted(D)
# print(D)
# for i in sorted(D):
#     print(i, D[i])



L = [1, 2, 4, 8, 16, 32, 64]
X = 5

found = False
i = 0
while i < len(L):
    if 2 ** X == L[i]:
        # found = 1
        print('at index', i)
        break
    else:
        print(X, 'not found')
        i = i+1
    # else:
    #     i = i+1
    # if found:
    #     print('at index', i)
    # else:
    #     print(X, 'not found')


for i in L:
    index = L.index(i)
    if 2**X == L[index]:
        print('at index', index)
        break
    else:
        print(index, 'not found')


if 2**X in L:
    print(L.index(2**X))
else:
    pass
# print(2**X in L)

L = [1, 2, 4, 8, 16, 32, 64]
X = 5
X2 = range(X+1)

L2 = []
for i in X2:
    # x =- 1
    L2.append(2 ** X2[i])

# print(L2)

intersect = [x for x in L2 if x in L]
print(intersect)

B = '1101'
I = 0
while B != '':
    # print(ord(B[0]))
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]

print(I)

print(ord('1'))
# print(int('0'))
