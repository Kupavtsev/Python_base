spam = {'name': 'Pook', 'age': 5}

if 'color' not in spam:
    spam['color'] = 'black'

spam.setdefault('color2', 'black2')

spam['color3'] = 'black3'

print(spam)

# Another way

spam = {'name': 'Pook', 'age': 5}
#if 'color' not in spam:
#    spam['color'] = 'black'
spam.setdefault('color', 'black')
