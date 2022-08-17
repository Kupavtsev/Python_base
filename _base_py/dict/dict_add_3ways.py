# 1
spam = {'name': 'Pook', 'age': 5}

if 'color' not in spam:
    spam['color'] = 'black'

# 2
spam.setdefault('color2', 'black2')

spam['color3'] = 'black3'

print(spam)

# 3

print(spam.get('color2'))
print('\nThird method', spam)