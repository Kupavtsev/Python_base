print('----------1--------')
#Ex1
# Проход по индексам, используая range и длину len
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

print('----------2--------')
#2
# Заполнение массива
squares = []
for x in range(1 , 11):
    square = x**2
    squares.append(square)
print(squares)

# Создание массива с использованием выражения и диапазона
squares2 = [x**2 for x in range(1, 11)]
print(squares2)

print('----------3--------')
#3
names = ['oleg', 'liudmila', 'diana']
upper_names = []

for items in names:
    upper_names.append(items.upper())
print(upper_names)

names = ['oleg', 'liudmila', 'diana']
upper_names = [items.upper() for items in names]
print(upper_names)

print('----------4--------')
#4
dimensions = (600, 800)
print(dimensions)
for dimension in dimensions:
    print(dimension)