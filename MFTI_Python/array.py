N = int(input())
A = [0] * N
n = 0
x = int(input())
A[n] = x
n += 1

n -= 1
x = A[n]

####

A = []
x = int(input())
A.append(x)
n = len(A)
x = A.pop()

#### List Conprehentions

A = [x**2 for x in range(10)]
A = []
for x in range(10):
    A.append(x**2)

#### Отфильтровать массив, чтобы остались только четный элементы м возвести в квадрат

B = []
A = [1,2,3,4,5,7,12,9,6]
for x in A:
    if x%2 == 0:
        B.append(x**2)
#
B = []
A = [1,2,3,4,5,7,12,9,6]
B = [x**2 for x in A if x%2 == 0]