A = [0]*1000
top = 0
x = int(input('Enter the number: '))
while x != 0:
    A[top] = x
    top += 1
    x = int(input())
for k in range(4,-1,-1):
    print(A[k])
