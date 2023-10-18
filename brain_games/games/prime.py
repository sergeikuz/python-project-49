from random import randint
import prompt


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'


def game_prime():
    name = prompt.string(
        "Welocom to the Brain Games!"
        "\nMay I have your name? ")
    print(
        f'Hello, {name}!'
        f'\nAnswer "yes" if given number is prime.'
        f' Otherwise answer "no".')
    item = 0
    while item < 3:
        random_number = randint(1, 999)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        correct_answer = is_prime(random_number)
        if answer == correct_answer:
            print('Correct!')
            item += 1
        else:
            print(
                f'"{answer}" is wrong answer ;(.'
                f' Correct answer was "{correct_answer}".'
                f"\nLet's try again, {name}!")
            item = 4

        if item == 3:
            print(f"Congratulations, {name}!")
