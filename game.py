# game.py

import random
import csv

def play_game(player_name):

    player_wins = 0
    computer_wins = 0
    round_number = 0

    while round_number < 5:

        # Oota mängija Enteri vajutamist
        input('\nVajuta ENTER, et täringuid veeretada...')

        # Veereta täringuid
        player_dice = random.randint(1, 6)
        computer_dice = random.randint(1, 6)

        print(f'\nVoor {round_number + 1}:')
        print(f'{player_name} veeretas: {player_dice}')
        print(f'Arvuti veeretas: {computer_dice}')

        # Võrdle tulemusi
        if player_dice > computer_dice:
            print(f'{player_name} võitis vooru!')
            player_wins += 1
            round_number += 1

        elif computer_dice > player_dice:
            print('Arvuti võitis vooru!')
            computer_wins += 1
            round_number += 1

        else:
            print('Viik! Voor kordub.')

    # Mängu lõpptulemus
    print('\n--- MÄNGU TULEMUS ---')
    print(f'{player_name}: {player_wins} võitu')
    print(f'Arvuti: {computer_wins} võitu')

    # Selgita mängu võitja
    if player_wins > computer_wins:
        winner = player_name
        print(f'\n{player_name} võitis mängu!')

    else:
        winner = 'Arvuti'
        print('\nArvuti võitis mängu!')

    # Salvesta tulemus CSV-faili
    with open('dice_results.csv', 'a', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)

        writer.writerow([
            player_name,
            player_wins,
            computer_wins,
            winner
        ])

    print('Mängu tulemus salvestatud!')
