A=[1,2,3,4,5]
for x in A:
    print(x,type(x))
    x += 1
    print(x)
print(A)

A=[1,2,3,4,5]
for k in range(5):
    A[k]=A[k]*A[k]
print(A)
