
import random


def roll_dice():
    return random.randint(1, 6)


def play_turn(current_player):
    print(f'Player {current_player + 1} turn')
    score = 0
    while True:
        roll = roll_dice()
        print(f'Your rolled a {roll}')
        if roll == 1:
            return 0
        score += roll
        user_input = input('Roll dice again (y/n): ').lower()
        if user_input == 'n':
            return score


def run():
    current_player = 0
    scores = [0, 0]
    while True:
        turn_score = play_turn(current_player)

        scores[current_player] += turn_score

        print(f'\nYou scored {turn_score} points this turn.')
        print(f'Current scores: Player 1: {scores[0]}, Player 2: {scores[1]}')

        if scores[current_player] >= 10:
            print(f"Player {current_player + 1} wins !")
            break

        current_player = 1 if current_player == 0 else 0


if __name__ == "__main__":
    run()
