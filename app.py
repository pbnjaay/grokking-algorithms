import re


def fizz_buzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print('fizzbuzz')
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)


def reverse(ch: str):
    return ch[::-1]


def palindrome(ch: str):
    # TODO: review re module
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', ch).lower()
    return clean_string == clean_string[::-1]


def how_many_vowels(ch: str):
    count = 0
    vowels = ['a', 'o', 'e', 'u', 'i']
    for i in ch.strip().lower():
        if i.lower() in vowels:
            count += 1
    return count


def is_anagram(ch1: str, ch2: str):
    if not len(ch1) == len(ch2):
        return False

    return sorted(ch1.lower()) == sorted(ch2.lower())


def fact(n: int):
    if n < 0:
        raise ValueError(
            "La factorielle n'est pas définie pour les nombres négatifs.")
    if (n == 1):
        return 1
    return n * fact(n-1)


def find_max(numbers: list):
    if not numbers:
        raise ValueError('La liste est vide.')
    max = numbers[0]
    for i in numbers:
        if max < i:
            max = i
    return max


def how_many_occ(numbers: list, to_find):
    if not numbers:
        raise ValueError('La liste est vide.')
    numbers.count(to_find)


def trier(numbers):
    return sorted(numbers)


print(trier([5, 2, 9, 1, 5, 6]))


def doublons(numbers):
    seen = set()
    duplicates = set()
    for number in numbers:
        if number in seen:
            duplicates.add(number)
        else:
            seen.add(number)

    return list(duplicates)


print(doublons([1, 2, 3, 2, 1, 4, 5, 3]))
