#влево
N = int(input())
A = [0] * N
for k in range(N):
    A[k] = int(input())
tmp = A[0]
for k in range(N-1):
    A[k]=A[k+1]
A[N-1]=tmp


#вправо
N = int(input())
A = [0] * N
for k in range(N):
    A[k] = int(input())
tmp=A[N-1]
for k in range(N-2, -1, -1):
    A[k+1]=A[k]
A[0]=tmp

#Решето эратосфена
N = int(input())
A = [True] * N
A[0] = A[1] = False
for k in range(2, N):
    if A[k]:
        for m in range(2*k, N, k):
            A[m] = False
print(A)

for k in range(N):
    print(k, '-', "простое" if A[k] else "составное")