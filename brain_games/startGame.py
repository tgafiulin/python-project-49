import prompt
from brain_games.cli import welcome_user


def startGame(getRoundData, question):
    name = welcome_user()
    print(question)
    gameSteps = 3
    i = 0

    while i < gameSteps:
        rightAnswer, question = getRoundData()
        print(f'Question: {question}')
        userAnswer = prompt.string('Your answer: ')

        if rightAnswer == userAnswer:
            print('Correct!')
        else:
            print(f'''{userAnswer} is wrong answer ;(.
                Correct answer was {rightAnswer}.''')
            print(f'Let\'s try again, {name}!')
            return
        i += 1
    print(f'Congratulations, {name}!')
