#----------- 1 ----------

#a
# Каждую букву строки поместить в массив в числом представлении ord(x)
S = "hello"
a = []
for x in S:
    x = ord(x)
    a.append(x) 
print(a)

#b
# Суммирует эти значения в массиве
sum = 0
for b in a:
    sum = sum + b
print(sum)

#c
# Итератор, который Мапит каждое кодовое значение буквы из S
S = "hello"
ascii = map(ord, S)
next(ascii)
next(ascii)