import random


def gen_secret():
    return ''.join(
        [str(number) for number in random.sample(range(0, 10), 4)]
    )


def is_4_digit_and_unique(guess):
    return len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4


def get_cows_and_bulls(secret, guess):
    cows = sum(1 for i in guess for j in secret if i == j)
    bulls = sum(1 for i in range(4) if guess[i] == secret[i])

    return cows, bulls


def run():
    secret = gen_secret()
    print('I have generated a 4-digit number with unique digits. Try to guess it!')
    while True:
        guess = input('Guess: ').strip()
        if not is_4_digit_and_unique(guess):
            print('Invalid guess. Please enter a 4-digit number with unique digits.')
            continue

        cows, bulls = get_cows_and_bulls(secret, guess)
        print(f"{cows} cows, {bulls} bulls")

        if bulls == 4:
            print('Congratulations! You guessed the correct number.')
            break


if __name__ == '__main__':
    run()
