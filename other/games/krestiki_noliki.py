# alias cls='printf "\033[H\033[3J"'

'''
take care when neither one have win - Strange reaction
protect busy squares from user
DRY
'''

table = {(1,1): '_',(1,2): '_',(1,3): '_',
        (2,1): '_', (2,2): '_', (2,3): '_',
        (3,1): '_', (3,2): '_', (3,3): '_',
        }

def show_board(table):
    
    print("\033[H\033[J", end="")       # clean console

    print(f'3,1 |{table[(3,1)]}|' + f'{table[(3,2)]}' + f'|{table[(3,3)]}| 3,3')
    print(f'2,1 |{table[(2,1)]}|' + f'{table[(2,2)]}' + f'|{table[(2,3)]}| 2,3')
    print(f'1,1 |{table[(1,1)]}|' + f'{table[(1,2)]}' + f'|{table[(1,3)]}| 1,3')
    

def turn():
    global table

    # create a list of free keys
    free_squares = []
    for key in table:
        if table[key] != 'x':
            if table[key] != '0':
                free_squares.append(key)

    # Show possible enterance for user
    free_squares_user_friendly = []
    for each in free_squares:
        turn = str(each[0]) + str(each[1])
        
        free_squares_user_friendly.append(int(turn))

    print('You can choice from free squares : ', free_squares_user_friendly)
    user_turn = input('Enter your turn: ')
    # turn = (int(user_turn[0]), int(user_turn[1]))
    if user_turn.isdigit():
        turn = (int(user_turn[0]), int(user_turn[1]))
    else:
        # print('Введите допустимое число!')
        user_turn = input('Введите допустимое число! ')
        turn = (int(user_turn[0]), int(user_turn[1]))


    table[turn] = 'x'
    ai_turn()

def ai_turn():
    global table

# create a list of free keys
# random choise from this list and put the value
    free_squares = []

    for key in table:
        if table[key] != 'x':
            if table[key] != '0':
                free_squares.append(key)

    if free_squares:
        table[random.choice(free_squares)] = '0'
        show_board(table)
    else:
        return None
        print('No one have won!!!')

# RULES OF THE GAME: Steight line three of kind
def check_end_game(table):
    for key in table:
        if (
            table[(1,1)] == 'x' and
            table[(1,2)] == 'x' and
            table[(1,3)]) == 'x':
            return play_again(True)
        elif table[(2,1)] == 'x' and table[(2,2)] == 'x' and table[(2,3)] == 'x':
            return play_again(True)
        elif table[(3,1)] == 'x' and table[(3,2)] == 'x' and table[(3,3)] == 'x':
            return play_again(True)
        elif table[(3,1)] == 'x' and table[(2,2)] == 'x' and table[(1,3)] == 'x':
            return play_again(True)
        elif table[(1,1)] == 'x' and table[(2,2)] == 'x' and table[(3,3)] == 'x':
            return play_again(True)
        elif table[(1,1)] == 'x' and table[(2,1)] == 'x' and table[(3,1)] == 'x':
            return play_again(True)
        elif table[(1,2)] == 'x' and table[(2,2)] == 'x' and table[(3,2)] == 'x':
            return play_again(True)
        elif table[(3,3)] == 'x' and table[(2,3)] == 'x' and table[(1,3)] == 'x':
            return play_again(True)

        if table[(1,1)] == '0' and table[(1,2)] == '0' and table[(1,3)] == '0':
            return play_again(False)
        elif table[(2,1)] == '0' and table[(2,2)] == '0' and table[(2,3)] == '0':
            return play_again(False)
        elif table[(3,1)] == '0' and table[(3,2)] == '0' and table[(3,3)] == '0':
            return play_again(False)
        elif table[(3,1)] == '0' and table[(2,2)] == '0' and table[(1,3)] == '0':
            return play_again(False)
        elif table[(1,1)] == '0' and table[(2,2)] == '0' and table[(3,3)] == '0':
            return play_again(False)
        elif table[(1,1)] == '0' and table[(2,1)] == '0' and table[(3,1)] == '0':
            return play_again(False)
        elif table[(1,2)] == '0' and table[(2,2)] == '0' and table[(3,2)] == '0':
            return play_again(False)
        elif table[(3,3)] == '0' and table[(2,3)] == '0' and table[(1,3)] == '0':
            return play_again(False)

        # # Thats not work!
        elif '_' not in table.values():
            # for key in table:
            #     if table[key] != '_':
            print('No one have won!!!')
        else: turn()

def play_again(user):
    print('You won' if user else 'AI won')
   
#    Is it possible to clear table throu cycle for ?
    user_choice = input('Do you want to play again? (y/n): ')
    if user_choice == 'y':
        global table
        table = {(1,1): '_',(1,2): '_',(1,3): '_',
                (2,1): '_', (2,2): '_', (2,3): '_',
                (3,1): '_', (3,2): '_', (3,3): '_',
                }
        show_board(table)
        check_end_game(table)
    else:
        print('Good bye')
        pass
    

if __name__ == "__main__":
    import random
    show_board(table)
    check_end_game(table)