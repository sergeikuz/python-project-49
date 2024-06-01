from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_conditions():
    number = randint(1, 999)
    if number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    question = f"{number}"
    return question, correct_answer
