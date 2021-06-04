# Лекция 5. 48мин.

def array_search(A:list, N:int, x:int): # А Является формальным параметром и будет ссылкой на А1
    """ Осуществляет поиск числа Х в массиве А
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента Х в массиве А.
        Или -1, если такого нет.
        Если в массиве несколько одинаковых элементов,
        равных Х, то вернуть индекс первого по счету.
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, len(A1), 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test2 - ok")
    else:
        print("#test2 - fail")

    A3 = [10, 20, 30, 10, 10]
    m = array_search(A3, 5, 10)
    if m == 0:
        print("#test3 - ok")
    else:
        print("#test3 - fail")

test_array_search()
