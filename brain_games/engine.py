import prompt


MAX_ROUNDS = 3


def running_games_through_the_engine(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(
        f"Hello, {name}!"
        f"\n{game.RULE}")
    item = 0
    while item < MAX_ROUNDS:
        question, correct_answer = game.generate_data_for_game_round()
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
