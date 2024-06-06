from random import randint


RULE = "Find the greatest common divisor of given numbers."


def get_conditions():
    number1 = randint(1, 100)
    number2 = randint(1, 100)

    question = f"{number1} {number2}"

    while number1 != 0 and number2 != 0:
        if number1 > number2:
            number1 = number1 % number2
        else:
            number2 = number2 % number1

    answer = number1 + number2
    correct_answer = str(answer)

    return question, correct_answer
