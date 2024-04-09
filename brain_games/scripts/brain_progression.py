#!/usr/bin/env python

import random

from brain_games.startGame import startGame


def main():
    question = 'What number is missing in the progression?'
    startGame(getRoundData, question)


def getRoundData():
    firstNumberProgression = random.randint(0, 99)
    stepProgression = random.randint(1, 3)
    lengthProgression = random.randint(5, 10)
    indexAnswer = random.randint(0, lengthProgression - 1)

    params = firstNumberProgression, stepProgression, lengthProgression
    row = generateProgression(params)
    rightAnswer = str(row[indexAnswer])
    row[indexAnswer] = '..'

    question = ' '.join(row)

    return (rightAnswer, question)


def generateProgression(params):
    firstNumberProgression, stepProgression, lengthProgression = params
    row = []

    for i in range(lengthProgression):
        number = firstNumberProgression + i * stepProgression
        row.append(str(number))

    return row


if __name__ == '__main__':
    main()
