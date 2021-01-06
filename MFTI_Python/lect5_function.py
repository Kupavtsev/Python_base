def array_search(A:list, N:int, x:int): # А Является формальным параметром и будет ссылкой на А1
    """ Осуществляет поиск числа Х в массиве А
        от 0 до N-1 индекса включительно.
        Возвращает индекс элемента Х в массиве А.
        Или -1, если такого нет.
    """
    pass

def test_array_search():
    A1 = [1, 2, 3, 4, 5]
    m = array_search(A1, 5, 8)
    if m == -1:
        print("#test1 - ok")
    else:
        print("#test1 - fail")

    A2 = [-1, -2, -3, -4, -5]
    m = array_search(A2, 5, -3)
    if m == 2:
        print("#test1 - ok")
    else:
        print("#test1 - fail")
