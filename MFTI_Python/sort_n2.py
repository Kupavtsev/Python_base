def insert_sort(A):
    """ сортировка списка А вставками """
    N = len(A)
    for top in range(1, N):
        k = top
        while k > 0 and A[k-1] > A[k]:
            A[k], A[k-1] = A[k-1], A[k]     #тот кто левее он выше того кого я добавляю
            k -= 1                          #k это текущее положение элемента который мы переносим
                                            #top контролирует сколько элементов я сейчас добавляю

def choice_sort(A):
    """ сортировка списка А выбором """
    N = len(A)
    for pos in range(0, N-1):
        for k in range(pos+1, N):           #pos+1 проверка тех кто справа после отсортированных эелементов
            if A[k] < A[pos]:               #Если тот кто в позиции k лучше, чем в позиции pos, то меняем их местами
                A[k], A[pos] = A[pos], A[k]

def bubble_sort(A):
    """ сортировка списка А методом пузырька """
    N = len(A)
    for bypass in range(1, N):
        for k in range(0, N-bypass):
            if A[k] > A[k+1]:
                A[k], A[k+1] = A[k+1], A[k]

def test_sort(sort_algorithm):
    print("Тестируем: ", sort_algorithm.__doc__)
    """ засовываем функцию в качестве параметра """
    print("testcase #1: ", end="")
    A = [4, 2, 5, 1, 3]
    A_sorted = [1, 2, 3, 4, 5]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #2: ", end="")
    A = list(range(10, 20)) + list(range(0, 10))    #создаем список из прорессии
    A_sorted = list(range(20))                      #А создаст новый список взамен стр16
    sort_algorithm(A)                               #конкотенирование 2х списков
    print("Ok" if A == A_sorted else "Fail")

    print("testcase #3: ", end="")
    A = [4, 2, 4, 2, 1]
    A_sorted = [1, 2, 2, 4, 4]
    sort_algorithm(A)
    print("Ok" if A == A_sorted else "Fail")

#    if A == A_sorted:
#        print("Ok")
#    else:
#        print("Fail")

if __name__ == "__main__":
    test_sort(insert_sort)
    test_sort(choice_sort)
    test_sort(bubble_sort)
