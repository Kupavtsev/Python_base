spam = {'name': 'Pook', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
spam.setdefault('color', 'black')
