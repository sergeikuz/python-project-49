import prompt
from random import randint


def game_even():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")

    print('Answer "yes" if the number is even, otherwise answer "no".')

    item = 0
    while item < 3:
        number = randint(1, 999999)
        print(f"Question: {number}")

        answer = prompt.string('Your answer: ')

        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'

        if correct_answer == answer:
            print('Correct!')
            item += 1

        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")

            item = 4

        if item == 3:
            print(f"Congratulations, {name}!")
