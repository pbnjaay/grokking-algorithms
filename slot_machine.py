import random


def pull_lever():
    return random.choices(['🎈', '🎁', '🧨', '🎱', '🎃'], k=3)


def get_payout(result, bet_amount):
    if len(set(result)) == 1:
        return 10 * bet_amount
    if len(set(result)) == 2:
        return 2 * bet_amount
    return 0


def update_balance(balance, result, bet_amount):
    payout = get_payout(result, bet_amount)
    if payout == 0:
        print('You lost!')
    else:
        print(f'You win {payout} !')
    return balance - bet_amount + payout


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
            if 0 < bet_amount <= current_balance:
                return bet_amount
            print(
                f'Invalid bet amount. You can bet between $1 and ${current_balance}.')
        except ValueError:
            print('Please enter a valid number.')


def welcome_player(current_balance):
    print('\nWelcome to the slot machine game!')
    print(f'You start with a balance of ${current_balance}\n')


def play_again():
    return input('Do you want to play again? (y/n): ').lower() != 'n'


def main():
    balance = get_starting_bet()
    welcome_player(balance)
    while True:
        print(f'Current balance: ${balance}')
        result = pull_lever()
        print(' | '.join(result))
        bet_amount = get_bet_amount(balance)
        balance = update_balance(balance, result, bet_amount)

        if balance == 0:
            print('You are out of money!')
            break

        print('\n')

        if not play_again():
            print(f'You walk away with ${balance}.')
            break


if __name__ == '__main__':
    main()
