# Lesson: Importing (Pirple.com)
# Typed up by Franz Tapia Chaca
# on 11 April 2021

# Outside features customly-built for Python
# e.g. functions, classes

# Random library
# https://docs.python.org/3/library/random.html
#   features surrounding randomness generation
import random as r  # imports the whole library
# from random import *  # imports everything, but existing functions can be overwritten

# r.seed(1)
randInt = r.randint(0, 10)  # 0 <= N <= 10
print(randInt)  # pseudo random, can set seed above

randFloat = r.random()  # 0.0 <= N < 1.0
print(randFloat)

randUniform = r.uniform(1, 1100)  # 1 <= N <= 11
print(randUniform)

simplestList = [1, 3, 5, 7, 11]
pickElement = r.choice(simplestList)
print(pickElement)

print(simplestList)
r.shuffle(simplestList)
print(simplestList)

################
# Time library #
################

import time

# Duration of actions
currentTime = time.perf_counter()
print("Hello")
print("World")
pastTime = time.perf_counter()
print(pastTime - currentTime)

# Sleep
print("1")
time.sleep(2)
print("2")

for i in range(1, 11):
    print(i)
    time.sleep(1)

################
# Math library #
################

import math

val = 3
sqrtVal = math.sqrt(val)
print(sqrtVal)
# print(sqrtVal**2)

expVal = math.exp(val)  # e^val
print(expVal)

factVal = math.factorial(val)  # val!
print(factVal)

sinVal = math.sin(val)  # sine function is in radians (i.e. convert degrees to radians)
print(sinVal)

val = 3.14
floorVal = math.floor(val)
print(floorVal)

ceilVal = math.ceil(val)
print(ceilVal)
