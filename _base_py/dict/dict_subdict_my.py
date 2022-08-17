
print('------------fin_actives------------')
fin_actives = {'futures': {
                    'CME': 'CL',
                    'FORTS': 'RTS'
                    },
            'stocks': {
                'NYSE': 'TSLA',
                'MOEX': 'SBER'
                }}
print(fin_actives)
for name_a, active in fin_actives.items():
    print('\nActive: ' + name_a)
    print('\nValues: ', active)
    full_name = str(active) + " "
    # full_name += active['FORTS']
    
    print('\nFull name: ' + full_name.title())