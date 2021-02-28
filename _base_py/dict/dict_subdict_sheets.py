# добавление словарей в Массив
users = []

new_user = {'last': 'fermi', 'first': 'enrico', 'username': 'efermi'}
users.append(new_user)

new_user = {'last': 'curie', 'first': 'marie', 'username': 'mcurie'}
users.append(new_user)

# print(users)

for each_user_dict in users:
    for k, v in each_user_dict.items():
        print(k, ':', v)
    print('\n')


print('------------the same------------')
# Иной метод этой же задачи.

users2 = [{'last': 'fermi', 'first': 'enrico', 'username': 'efermi'},
        {'last': 'curie', 'first': 'marie', 'username': 'mcurie'}]

for user_dict in users:
    for k, v in user_dict.items():
        print(k, ':', v)
    print('\n')


print('------------people------------')

people = {'andy': ['sud', 'port'],
        'jhony': ['nice', 'gue'],
        'sveta': ['bycycle']}

for any, hobby in people.items():
    print(any, ':')
    for each in hobby:
        print('-', each)