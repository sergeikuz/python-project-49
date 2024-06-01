import prompt


MAX_ROUNDS = 3


def engine_for_brain_games(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
            f"Hello, {name}!"
            f"\n{game.RULE}")
    item = 0
    while item < MAX_ROUNDS:
        question, correct_answer = game.game_conditions()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            print("Correct!")
            item += 1
        else:
            print(
                    f"'{answer}' is wrong answer ;(. "
                    f"Correct answer was '{correct_answer}'."
                    f"\nLet's try again, {name}!")
            break
        if item == MAX_ROUNDS:
            print(f"Congratulations, {name}!")
