# main.py

import csv
from game import play_game

def main():

    filename = 'dice_results.csv'
    games = []

    # Loe varasemad mängud failist
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            games = list(reader)

        print(f'Varasemaid mänge kokku: {len(games)}')

    except FileNotFoundError:
        print('Varasemaid mänge pole.')

    # Arvuta statistika
    player_total = 0
    computer_total = 0

    for game in games:
        if len(game) == 4:
            if game[3] == game[0]:
                player_total += 1
            elif game[3] == 'Arvuti':
                computer_total += 1

    print(f'Mängija võidetud mängud: {player_total}')
    print(f'Arvuti võidetud mängud: {computer_total}')

    # Mängude kordamine
    while True:
        choice = input('\nSisesta oma nimi: ')

        play = input('Alusta mängu? (j/e): ').lower()

        if play == 'j':
            play_game(choice)

        elif play == 'e':
            print('Mäng ei alga.')
            break

        else:
            print('Vale sisend!')
            continue

        again = input('\nKas soovid uuesti mängida? (j/e): ').lower()

        if again != 'j':
            print('\nAitäh mängimast!')
            break


if __name__ == "__main__":
    main()
