import prompt
from random import randint
import math


def game_gcd():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
            f"Hello, {name}!"
            f"\nFind the greatest common divisor of given numbers.")
    item = 0
    while item < 3:
        number1 = randint(1, 100)
        number2 = randint(1, 100)
        answer = prompt.integer(
                f"Question: {number1} {number2}"
                f"\nYour answer: ")
        max_divisor = math.gcd(number1, number2)

        if max_divisor == answer:
            print('Correct!')
            item += 1

        else:
            print(
                    f"'{answer}' is wrong answer ;(."
                    f" Correct answer was '{max_divisor}'."
                    f"\nLet's try again, {name}!")
            item = 4
        if item == 3:
            print(f"Congratulations, {name}!")
