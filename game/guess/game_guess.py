#!/usr/local/bin/python
import random

number = input("guess number:\n")
number = int(number)

n = random.randint(1, 10)
while True:
    if number == n:
        print("guess right")
        break
    else:
        if number > n:
            print("larger")
        else:
            print("lower")
        number = input("请输入数组:\n")
        number = int(number)

print("game over")
