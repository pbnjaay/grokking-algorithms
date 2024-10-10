import re

strength_level = {
    1: 'very weak',
    2: 'weak',
    3: 'medium',
    4: 'strong',
    5: 'very strong'
}


def get_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search('[a-z]', password):
        strength += 1
    if re.search('[A-Z]', password):
        strength += 1
    if re.search('[\d]', password):
        strength += 1
    if re.search('[!@#$%&]', password):
        strength += 1

    return strength


def main():
    password = input('Enter a password: ')
    strength = get_password_strength(password)
    print(f'Password strength is: {strength_level[strength]}')


if __name__ == "__main__":
    main()
