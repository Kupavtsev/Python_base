#Matrix
M = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
]

N = [[2, 2, 2],
     [3, 3, 3],
     [4, 4, 4]
]

print([row[1] for row in M])            # Вывод первого столбца матрицы
print([M[row][1] for row in (0, 1, 2)]) # Вывод первого элемента матрицы по номеру строки
print([M[i][i] for i in range(len(M))]) # Выводит диагональ, но как ???
print([M[row][col] * N[row][col] for row in range(3) for col in range(3)])  # Перемножает элементы матрицы друг на друга
[[M[row][col] * N[row][col] for col in range(3)] for row in range(3)] # итерации по строкам выполняются во внешнем цикле

res = []
for row in range(3):
    tmp = []
    for col in range(3):                # Это все тоже самое, что и последняя строка 
        tmp.append(M[row][col] * N[row][col])
    res.append(tmp)    