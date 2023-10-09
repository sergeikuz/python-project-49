import prompt
from random import randint
import random


def math_operator(a, b, c):
    if a == '+':
        return b + c
    elif a == '-':
        return b - c
    elif a == '*':
        return b * c


def game_calc():
    print('Welcome to the Brain Games!')

    name = prompt.string('May I have your name? ')
    print(
            f"Hello, {name}!"
            f"\nWhat is the result of the expression?")

    item = 0
    while item < 3:
        number1 = randint(20, 50)
        number2 = randint(1, 10)
        list_of_operators = ['+', '-', '*']

        math = random.choice(list_of_operators)
        result = math_operator(math, number1, number2)
        answer = prompt.integer(
                f"Question: {number1} {math} {number2}"
                f"\nYour answer: ")

        if result == int(answer):
            print('Correct!')
            item += 1
        else:
            print(
                    f"'{answer}' is wrong answer ;(."
                    f"Correct answer was '{result}'."
                    f"\nLet's try again, {name}!")
            item = 4

        if item == 3:
            print(f"Congratulations, {name}!")
