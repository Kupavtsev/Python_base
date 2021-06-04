# to the Left, first become last
def to_left() -> None:
    print('Moving elements to Left')
    N = int(input('Enter size of the Array: '))
    A :list[int] = [0] * N
    for k in range(N):
        A[k] = int(input('Enter element of Array, number: '))
    tmp :int = A[0]             # We put in to 'tmp' First elem of Array
    for k in range(N-1):
        A[k]=A[k+1]             # We take an elem and re-assign it to the elem wich is stay at the right
    A[N-1]=tmp                  # We assing for the last elem of Array - the First from 'tmp'
    print(A)


# to the Right, last become first
def to_right() -> None:
    print('Moving elements to Right')
    N = int(input('Enter size of the Array: '))
    A :list[int] = [0] * N
    for k in range(N):
        A[k] = int(input('Enter element of Array, number: '))
    tmp :int =A[N-1]            # We put in to 'tmp' Last elem of Array
    for k in range(N-2, -1, -1):
        A[k+1]=A[k]             # We take the Last elem and re-assign it to the curent elem by iteration
    A[0]=tmp                    # Last elem of Array became First
    print(A)


#Решето эратосфена
def resheto() -> None :
    print('Resheto Eratosphena')
    N = int(input('Enter size of the Array: '))
    A :list[int] = [True] * N
    A[0] = A[1] = False
    for k in range(2, N):
        if A[k]:
            for m in range(2*k, N, k):
                A[m] = False
    print(A)

    for k in range(N):
        print(k, '-', "простое" if A[k] else "составное")

if __name__ == '__main__':
    # to_left()
    # to_right()
    resheto()