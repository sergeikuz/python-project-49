import random


RULE = "What number is missing in the progression?"


def generator_list_of_num():
    max_length_of_list = 10
    num1 = random.randint(1, 10)
    num2 = random.randint(90, 120)
    step = random.randint(1, 8)
    list_of_num = []

    for i in range(num1, num2, step):
        if len(list_of_num) < max_length_of_list:
            list_of_num.append(i)

    return list_of_num


def game_conditions():
    random_index = random.randint(0, 9)
    list_of_num = generator_list_of_num()

    correct_answer = str(list_of_num[random_index])

    list_of_num[random_index] = ".."

    question = " ".join(map(str, list_of_num))

    return question, correct_answer
