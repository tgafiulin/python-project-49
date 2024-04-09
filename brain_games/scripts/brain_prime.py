#!/usr/bin/env python

import math
import random

from brain_games.startGame import startGame


def main():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    startGame(getRoundData, question)


def getRoundData():
    number = random.randint(0, 99)
    isPrime = checkPrimeNumber(number)
    question = str(number)
    rightAnswer = 'yes' if isPrime else 'no'
    return (rightAnswer, question)


def checkPrimeNumber(number):
    if number == 1:
        return False
    elif number > 1:
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
    return True


if __name__ == '__main__':
    main()
