s = [1,2,3, 'to-delete', 5,6, 'to-delete']

a = list(filter(lambda x: x != 'to-delete', s))
print(a)

print(s == a)