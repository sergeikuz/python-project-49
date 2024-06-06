from random import randint


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    k = 0
    for i in range(2, number // 2 + 1):
        if (number % i == 0):
            k = k + 1
    if k <= 0:
        return 'yes'
    else:
        return 'no'


def get_conditions():
    random_number = randint(1, 999)
    correct_answer = is_prime(random_number)
    question = f'{random_number}'
    return question, correct_answer
