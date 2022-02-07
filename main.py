import random

print('******WELCOME TO TIC TAC TOE********')
logo = ['''__0__|''', '''__1__|''', '''__2__''',
        '''__3__|''', '''__4__|''', '''__5__''',
        '''  6  |''', '''  7  |''', '''  8  '''
        ]
print(f"{logo[0] + logo[1] + logo[2]}\n{logo[3] + logo[4] + logo[5]}\n{logo[6] + logo[7] + logo[8]}")

game_is_on = True

player_one_pick = str(input('player one please choose X or O\n')).lower()

if player_one_pick == 'x':
    print('from now on player 1 is X and player 2 is O')

else:
    print('from now on player 1 is O and player 2 is X')
winning_list = [[0, 1, 2], [0, 4, 8], [3, 4, 5], [6, 7, 8], [6, 4, 2], [1, 4, 7], [2, 5, 8]]

player_one_selection = []
player_two_selection = []


while game_is_on:
    try:
        player_one_position = int(input(f'player 1 turn: please select where you would like to play\n'))
        selection = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        if player_one_position <= 8:
            selection.remove(player_one_position)
            player_one_selection.append(player_one_position)
            for piece in winning_list:
                result = all(elem in piece for elem in player_one_selection)
                if len(player_one_selection) == 3 and result:
                    print('player one wins')
                    game_is_on = False
            if player_one_pick == 'x':
                logo[player_one_position] = logo[player_one_position].replace(f'{player_one_position}', 'X')
            else:
                logo[player_one_position] = logo[player_one_position].replace(f'{player_one_position}', 'O')
            shape = f"{logo[0] + logo[1] + logo[2]}\n{logo[3] + logo[4] + logo[5]}\n{logo[6] + logo[7] + logo[8]}"
            print(shape)
            player_two_position = random.choice(selection)
            #player_two_position = int(input(f'player 2 turn: please select where you would like to play\n'))
            if player_two_position <= 8:
                player_two_selection.append(player_two_position)
                for piece in winning_list:
                    result = all(elem in piece for elem in player_two_selection)
                    if len(player_one_selection) == 3 and result:
                        print('player Two wins')
                        game_is_on = False
                if player_one_pick == 'x':
                    logo[player_two_position] = logo[player_two_position].replace(f'{player_two_position}', 'O')
                    shape = f"{logo[0] + logo[1] + logo[2]}\n{logo[3] + logo[4] + logo[5]}\n{logo[6] + logo[7] + logo[8]}"
                    print(shape)
                else:
                    logo[player_two_position] = logo[player_two_position].replace(f'{player_two_position}', 'X')
                    shape = f"{logo[0] + logo[1] + logo[2]}\n{logo[3] + logo[4] + logo[5]}\n{logo[6] + logo[7] + logo[8]}"
                    print(shape)

        else:
            print('you entered an invalid number please re-enter')
    except ValueError:
        print('please re-enter')
