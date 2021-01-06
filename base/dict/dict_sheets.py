'''

my_dict = {1: 'a', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 2: 'b'}

for num, values in sorted(my_dict.items()):
    print(num, values)

hey = len(my_dict)
print(hey)


users = []

new_user = {'last': 'fermi', 'first': 'enrico', 'username': 'efermi'}
users.append(new_user)

new_user = {'last': 'curie', 'first': 'marie', 'username': 'mcurie'}
users.append(new_user)

for user_dict in users:
    for k, v in user_dict.items():
        print(k, ':', v)
    print('\n')



#Иной метод этой же задачи.

users = [{'last': 'fermi', 'first': 'enrico', 'username': 'efermi'},
        {'last': 'curie', 'first': 'marie', 'username': 'mcurie'}]

for user_dict in users:
    for k, v in user_dict.items():
        print(k, ':', v)
    print('\n')



people = {'andy': ['sud', 'port'],
        'jhony': ['nice', 'gue'],
        'sveta': ['bycycle']}

for any, hobby in people.items():
    print(any, ':')
    for each in hobby:
        print('-', each)

'''

fin_actives = {'futures': {
                    'CME': 'CL',
                    'FORTS': 'RTS'
                    },
            'stocks': {
                'NYSE': 'TSLA',
                'MOEX': 'SBER'
                }}
for name_a, active in fin_actives.items():
    print('\nActive: ' + name_a)
    full_name = active['CME'] + " "
    full_name += active['FORTS']
    
    print('\nFull name: ' + full_name.title())