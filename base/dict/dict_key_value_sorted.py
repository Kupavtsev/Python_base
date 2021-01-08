#----------- 3 ----------
my_dict = {1: 'a', 3: 'c', 4: 'd', 6: 'f', 2: 'b', 5: 'e'}

for num, values in sorted(my_dict.items()):
	print(num, values)

hey = len(my_dict)
print('Length', hey)