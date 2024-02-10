# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

# A = input('first: ')
# B = input('second: ')
A = '29 28 10'
B = '11 01'

A = A.split()
B = B.split()

A = [int(x) for x in A]
B = [int(x) for x in B]

res = product(A, B)

for x in res:
    print(x, end=' ')