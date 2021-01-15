# Проверяет совпадающие элементы в переданных строках в виде параметров
# и возвращает массив с пересекающимися элементами
def intersect(*args):
    res = []
    # х - один элемент из строки первого параметра args[0]
    for x in args[0]:
        # other - строка целиком вторго параметра args[1:]
        for other in args[1:]:
            # проверяет х - каждый элемент строки первого параметра
            # на наличие в строке other - вторго параметра
            if x not in other:  break
        else:
            res.append(x)
    return res

# Объединение не совпадающих элементов
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return res

s1, s2, s3 = 'spam', 'scam', 'slam'

intersect(s1, s2)   #['s','a','m']
union(s1, s2)       #['s','a','m', 'c']

intersect([1, 2, 3], (1, 4))
union([1, 2, 3], (1, 4))

intersect(s1, s2, s3)
union(s1, s2, s3)