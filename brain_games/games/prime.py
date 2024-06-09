from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0:
        return True
    else:
        return False


def generate_data_for_game_round():
    random_number = randint(1, 99)

    if is_prime(random_number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    question = f'{random_number}'

    return question, correct_answer
