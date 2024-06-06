from random import randint
import random
import operator


RULE = "What is the result of the expression?"


def get_operation(str_, a, b):
    if str_ == '+':
        return operator.add(a, b)
    elif str_ == '-':
        return operator.sub(a, b)
    elif str_ == '*':
        return operator.mul(a, b)


def get_conditions():
    number1 = randint(20, 50)
    number2 = randint(1, 10)
    list_of_operators = ['+', '-', '*']

    math = random.choice(list_of_operators)
    correct_answer = str(get_operation(math, number1, number2))
    question = f"{number1} {math} {number2}"
    return question, correct_answer
