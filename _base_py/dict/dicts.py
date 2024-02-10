# Создание копии словаря через цикл for по ключу
def copyDict(old):
    new = {}
    for key in old.keys():
        new[key] = old[key]
    return new

# Объеденение двух словарей через цикл for
def addDict(d1, d2):
    new = {}
    for key in d1.keys():
        new[key] = d1[key]
    for key in d2.keys():
        new[key] = d2[key]
    return new

# Создание копии словаря с использованием Метода словаря .copy
def copyDict2(dict):
    dict2 = dict.copy()
    return dict2
    
dict1 = {1 : 10, 2 : 20, 3 : 30}
dict2 = {4 : 40, 5 : 50, 1 : 60}

first = copyDict(dict1)
print(first)

two = addDict(dict1, dict2)
print(two)

three = dict1.copy()
three[7] = 70
print(three)
print(dict1)

# print(dir(dict1))
