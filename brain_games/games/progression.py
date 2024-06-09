import random


RULE = "What number is missing in the progression?"


def generate_list_of_num():
    max_length_of_list = slice(10)
    num1 = random.randint(1, 10)
    num2 = random.randint(90, 120)
    step = random.randint(1, 8)

    list_of_num = list(range(num1, num2, step)[max_length_of_list])

    return list_of_num


def generate_data_for_game_round():
    random_index = random.randint(0, 9)
    list_of_num = generate_list_of_num()

    correct_answer = str(list_of_num[random_index])

    list_of_num[random_index] = ".."

    question = " ".join(map(str, list_of_num))

    return question, correct_answer
