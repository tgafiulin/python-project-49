#!/usr/bin/env python

import random

from brain_games.startGame import startGame


def main():
    question = 'Find the greatest common divisor of given numbers.'
    startGame(getRoundData, question)


def getRoundData():
    randomFirstNumber = random.randint(0, 99)
    randomSecondNumber = random.randint(0, 99)

    question = f'Question: {randomFirstNumber} {randomSecondNumber}'
    rightAnswer = str(getGcd(randomFirstNumber, randomSecondNumber))
    return (rightAnswer, question)


def getGcd (a, b):
  if not b:
    return a

  return getGcd(b, a % b)


if __name__ == '__main__':
    main()
