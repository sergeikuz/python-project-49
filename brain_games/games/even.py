from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def generate_data_for_game_round():
    number = randint(1, 100)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = f"{number}"

    return question, correct_answer
