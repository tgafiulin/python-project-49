#!/usr/bin/env python

import random

from brain_games.startGame import startGame


def main():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    startGame(getRoundData, question)


def getRoundData():
    randomNumber = random.randint(1, 100)
    question = randomNumber
    rightAnswer = 'yes' if checkEvenNumber(randomNumber) else 'no'
    return (rightAnswer, question)


def checkEvenNumber(number):
    return number % 2 == 0


if __name__ == '__main__':
    main()
