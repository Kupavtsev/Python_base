#1

#a
S = "hello"
a = []
for x in S:
    x = ord(x)
    a.append(x) 
#b

sum = 0
for b in a:
    sum = sum + b

#c ???

S = "hello"
ascii = map(ord, S)
next(ascii)
next(ascii)

#3
my_dict = {1: 'a', 3: 'c', 4: 'd', 6: 'f', 2: 'b', 5: 'e'}

for num, values in sorted(my_dict.items()):
	print(num, values)