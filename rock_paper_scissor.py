import random


ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'

emojis = {ROCK: '✊', PAPER: '✋', SCISSORS: '✌'}
choices = list(emojis.keys())


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper or Scissor? (r/p/s) :').lower()
        if user_choice in emojis:
            return user_choice
        print('Invalid choice')


def display_choices(user_choice, computer_choice):
    print(f'You choose {emojis.get(user_choice)}')
    print(f'Computer choose {emojis.get(computer_choice)}')


def determine_the_winner(user_choice, computer_choice):
    if computer_choice == user_choice:
        print('Draw!')
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print('You win!')

    else:
        print('You lose!')


def play():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_the_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break


if __name__ == "__main__":
    play()
