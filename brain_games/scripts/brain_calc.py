#!/usr/bin/env python

import random

from brain_games.startGame import startGame


def main():
    question = 'What is the result of the expression?'
    startGame(getRoundData, question)


def getRoundData():
    randFirstNumber = random.randint(0, 99)
    randSecondNumber = random.randint(0, 99)
    operations = ('+', '-', '*')
    operation = operations[random.randint(0, len(operations) - 1)]

    question = f'{randFirstNumber} {operation} {randSecondNumber}'
    rightAnswer = str(calculation(randFirstNumber, operation, randSecondNumber))
    return (rightAnswer, question)


def calculation(firstNumber, operation, secondNumber):
    if operation == '+':
        return firstNumber + secondNumber
    if operation == '-':
        return firstNumber - secondNumber
    if operation == '*':
        return firstNumber * secondNumber


if __name__ == '__main__':
    main()
