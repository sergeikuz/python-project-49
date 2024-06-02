from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer


def game_conditions():
    number = randint(1, 999)
    correct_answer = is_even(number)
    question = f"{number}"
    return question, correct_answer
