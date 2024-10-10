import random

a = random.randint(1, 100)
while True:
    try:
        number_to_guess = int(input('Guess the number between 1 and 100: '))
        if number_to_guess > a:
            print('Too high!')
        elif number_to_guess < a:
            print('Too low!')
        else:
            print('Congratulations!')
            break
    except:
        print('Invalid value')
