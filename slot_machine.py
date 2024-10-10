import random


def pull_lever():
    return random.choices(['🎈', '🎁', '🧨', '🎱', '🎃'], k=3)


def get_coeff(result):
    if len(set(result)) == 1:
        return 3
    elif len(set(result)) == 2:
        return 2
    return 1


def get_new_balance(balance, bet_amount, result):
    balance -= bet_amount
    coeff = get_coeff(result)

    if coeff <= 1:
        print('You lost !')
        return balance

    win_amount = coeff * bet_amount
    balance += win_amount
    print(f'You won ! ${win_amount}')

    return balance


def get_starting_bet():
    while True:
        try:
            starting_bet = int(input('Enter your starting balance: $'))
            if starting_bet > 0:
                return starting_bet
            print('Balance must be positive.')
        except ValueError:
            print('Please enter a valid number.')


def get_bet_amount(current_balance):
    while True:
        try:
            bet_amount = int(input('Enter your bet amount: $'))
            if not (bet_amount <= 0 or bet_amount > current_balance):
                return bet_amount
            print(
                f'Invalid bet amount. You can bet between $1 and ${current_balance}.')
        except ValueError:
            print('Please enter a valid number.')


def welcome_player(current_balance):
    print('\n')
    print('Welcome to the slot machine game!')
    print(f'You start with a balance of ${current_balance}')
    print('\n')


def main():
    balance = get_starting_bet()

    welcome_player(balance)

    while True:
        print(f'Current balance: ${balance}')

        bet_amount = get_bet_amount(balance)

        result = pull_lever()
        print(' | '.join(result))

        balance = get_new_balance(balance, bet_amount, result)

        if balance == 0:
            print('You are out of money!')
            break

        play_again = input('Do you want to play again? (y/n): ').lower() == 'y'
        print('\n')

        if not play_again:
            print(f'You walk away with ${balance}.')
            break


if __name__ == '__main__':
    main()
