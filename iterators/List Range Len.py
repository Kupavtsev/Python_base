#Ex1
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#2
squares = []
for x in range(1 , 11):
    square = x**2
    squares.append(square)
print(squares)

squares = [x**2 for x in range(1, 11)]
print(squares)

#3
names = ['oleg', 'liudmila', 'diana']
upper_names = []

for items in names:
    upper_names.append(items.upper())
print(upper_names)

names = ['oleg', 'liudmila', 'diana']
upper_names = [items.upper() for items in names]
print(upper_names)

#4
dimensions = (600, 800)
print(dimensions)
for dimension in dimensions:
    print(dimension)