import random
import string


def generate_password(length, has_uppercase, has_numbers, has_special_chars):
    if length < (has_numbers + has_uppercase + has_special_chars):
        raise ValueError(
            'Password length is too short for the specified criteria.')

    password = ''
    if has_numbers:
        password += random.choice(string.digits)
    if has_uppercase:
        password += random.choice(string.ascii_uppercase)
    if has_special_chars:
        password += random.choice(string.punctuation)

    printable_without_white_space = list(string.ascii_letters) +\
        list(string.punctuation)

    random.shuffle(printable_without_white_space)

    last_letters = random.sample(
        printable_without_white_space, length - len(password)
    )

    password_list = list(password)
    random.shuffle(password_list)

    password = password_list + last_letters

    return ''.join(password)


def main():
    length = int(input('Enter a password length: '))
    has_uppercase = input('Include uppercase letters? (y/n): ').lower() == 'y'
    has_numbers = input('Include numbers? (y/n): ') == 'y'
    has_special_chars = input('Include special characters? (y/n)') == 'y'
    try:
        password = generate_password(
            length, has_uppercase, has_numbers, has_special_chars)
        print(password)
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
