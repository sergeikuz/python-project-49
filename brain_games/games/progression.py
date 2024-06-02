import random


RULE = "What number is missing in the progression?"


def generator_list_of_num():
    num1 = random.randint(1, 10)
    num2 = random.randint(90, 120)
    step = random.randint(1, 8)
    list_of_num = []
    for i in range(num1, num2, step):
        list_of_num.append(i)
    return list_of_num


def game_conditions():
    random_index = random.randint(0, 10)
    list_of_num = generator_list_of_num()
    correct_answer = str(list_of_num[random_index])
    list_of_num[random_index] = ".."
    question = " ".join(map(str, list_of_num[:11]))
    return question, correct_answer
