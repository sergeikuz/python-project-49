import prompt
import random


def game_progression():
    name = prompt.string(
        "Welcome to the Brain Games!"
        "\nMay I have your name? ")
    print(
        f"Hello, {name}!"
        f"\nWhat number is missing in the progression?')")

    item = 0
    while item < 3:
        num1 = random.randint(1, 20)
        num2 = random.randint(80, 100)
        step = random.randint(1, 8)
        list_of_num = []

        for i in range(num1, num2, step):
            list_of_num.append(i)

        random_index = random.randint(0, 9)
        correct_answer = list_of_num[random_index]
        list_of_num[random_index] = ".."
        question = " ".join(map(str, list_of_num[0:10]))

        answer = prompt.integer(
            f"Question: {question}"
            f"\nYour answer: ")

        if answer == correct_answer:
            print('Correct!')
            item += 1

        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f" Correct answer was '{correct_answer}'."
                f"\nLet's try again, {name}!")
            item = 4

        if item == 3:
            print(f"Congratulations, {name}!")
