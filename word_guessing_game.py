import random
import re


def generate_word(words):
    return random.choice(words)


def get_words_from_file(file):
    try:
        with open(file, 'r') as file:
            lines = file.readlines()

        return [line.strip().lower() for line in lines]
    except FileNotFoundError:
        print(f'{file} does not exist')
        return []


def get_guessed_letter(already_guessed_letters):
    letter = input('Enter a letter: ').lower()

    if re.search('[0-9]', letter):
        print('Enter only letter fom a - z.')
        return ''

    if len(letter) != 1:
        print('Enter only one letter.')
        return ''

    if letter in already_guessed_letters:
        print('You already guess that word')
        return ''

    return letter


def show_hint(already_guessed_letters, word_to_guess):
    for letter in word_to_guess:
        print(letter, end='') \
            if letter in already_guessed_letters \
            else print('_', end='')
    print('\n')


def is_word_guessed(word_to_guess, already_guessed_letters):
    return set(already_guessed_letters) == set(word_to_guess)


def exhausted_attempts(attemp_count):
    return attemp_count >= 6


def game_over(attemp_count, word_to_guess, already_guessed_letters):
    if exhausted_attempts(attemp_count):
        print(f"Game over! The word was {word_to_guess}.")
        return True

    if is_word_guessed(word_to_guess, already_guessed_letters):
        print('Congratulations! you guessed the correct word.')
        return True

    return False


def main():
    list_of_words = get_words_from_file('words.txt')

    if not list_of_words:
        print('No word loaded.')
        return

    word_to_guess = generate_word(list_of_words)
    already_guessed_letters = []
    attemp_count = 0

    while True:

        if game_over(attemp_count, word_to_guess, already_guessed_letters):
            break

        letter = get_guessed_letter(already_guessed_letters)

        if not letter:
            continue

        if not letter in word_to_guess:
            attemp_count += 1
            print('Wrong guess!')
            continue

        already_guessed_letters.append(letter)
        print('Good guess!')
        show_hint(already_guessed_letters, word_to_guess)


if __name__ == '__main__':
    main()
