def matryushka(n):
    if n == 1:
        print("Матрёшечка")
    else:                           #else показывает, что эта мат-ка не последняя
        print("Верх матрёшки n=", n)
        matryushka(n-1)
        print("Низ матрёшки n=", n)