#!/usr/bin/env python

import random

from brain_games.startGame import startGame


def main():
    question = 'What is the result of the expression?'
    startGame(getRoundData, question)


def getRoundData():
    randomFirstNumber = random.randint(0, 99)
    randomSecondNumber = random.randint(0, 99)
    operations = ('+', '-', '*')
    randomOperation = operations[random.randint(0, len(operations) - 1)]

    question = f'{randomFirstNumber} {randomOperation} {randomSecondNumber}'
    rightAnswer = str(calculation(randomFirstNumber, randomOperation, randomSecondNumber))
    return (rightAnswer, question)


def calculation (firstNumber, operation, secondNumber):
  if operation == '+':
    return firstNumber + secondNumber
  if operation == '-':
    return firstNumber - secondNumber
  if operation == '*':
    return firstNumber * secondNumber


if __name__ == '__main__':
    main()
