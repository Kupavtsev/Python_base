import pickle
import struct


# file = open('file.txt', 'w')

# file.write('Test of first string\n')
# file.write('test of second without newline\n')

# file.close()

# file_open = open('file.txt', 'r')
# one = file_open.readlines()
# two = file_open.readline()
# print(one)

# a, *b = file_open
# print(a, b)

# L2 = [line.rstrip() for line in file_open]
# L1 = list(enumerate(L2))
# print(L1)
# D = {k:v for k,v in L1}
# print(D)


# L = [line.rstrip() and line.replace('first', 'WOW') for line in open('file.txt', 'r')]
# S = ''.join(L[0])
# S1 = ''.join(L[1])
# print(S)
# print(S1)

# file_open.close()

# for line in open('file.txt', 'r'):
#     print(line)


# Pickle
A, B, C = 11, 20, 14
D = {'a': 1, 'b': 'hello'}
D['my'] = 'try'
T = (B, '1566')
L = [12, 17, 22, 55]

D2 = [x for x in T]
# print(D2)

with open('dif_types.pkl', 'wb')as F:
    pickle.dump(D, F)

with open('dif_types.pkl', 'rb')as F:
    D = pickle.load(F)
    print('pickle:', D)

# with open('dif_types.txt', 'w') as f:
#     f.write('%s, %s, %s\n' % (A, B, C))
#     f.write(str(D) + '$' + str(T))
    
# with open('dif_types.txt', 'r') as f:
#     line = f.readline()
#     line = line.split(',')
#     line = [int(x) for x in line]
#     print(type(line))
#     print(line)
#     line2 = f.readline()
#     print(line2)
#     print(type(line2))
#     line2 = line2.split('$')
#     print(line2)
#     print(type(line2[0]))
#     line2 = [eval(x) for x in line2]
#     print(line2)
#     print(type(line2[0]))


FB = open('binary.bin', 'wb')

data = struct.pack('>i4sh', 7, 'spam', 8)
# print(data)
FB.write(data)
FB.close()

FB2 = open('binary.bin', 'rb')
data2 = FB2.read()
# print(data2)