# Перебор элементов массива
# и операция над каждым элементом
def iter_arr() -> None:
    A = [1,2,3,4,5]
    for x in A:
        print(x,type(x))
        x += 1
        print(x)
    print(A, '\n')


# Change every element of array
def change_elem_arr() -> None:
    A = [1,2,3,4,5]
    for k in range(5):
        A[k]=A[k]*A[k]
    print(A, '\n')


# Big Arrays
def big_arr() -> None:
    A = [0] * 1000
    top = 0
    x = int(input('Enter the number: '))
    while x != 0:
        A[top] = x
        top += 1
        x = int(input())
    for k in range(4,-1,-1):    # Iter elements of New arr from Forth to start
        print(A[k])


if __name__ == '__main__':
    print('\n ---Start--- \n')
    print('Cycle for on each element and plus 1')
    iter_arr()

    print('\n Change every element of array')
    change_elem_arr()
    
    print('\n Big Arrays')
    big_arr()
