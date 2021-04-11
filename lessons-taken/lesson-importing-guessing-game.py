# Lesson: Guessing game (Pirple.com, "Python is Easy")
# A random integer is created, and the user is prompted to guess the integer
# If guess is more or less than or equal to the integer, the user is informed so.
# Typed by Franz Tapia Chaca
# 11 April 2021

#######################################
# The user guesses the random integer #
#######################################

#from random import randint

# randVal = randint(0, 100)
#
# while True:
#     guess = int(input("Guess the number: "))
#     if randVal == guess:
#         print("Correct. The random integer was " + str(randVal) + ".")
#         break
#     elif randVal > guess:
#         print("Your guess is lower.")
#     else:
#         print("Your guess is higher.")

##########################################
# The computer guesses the random number #
##########################################

from time import perf_counter
from random import random, uniform
upper = 1.0
lower = 0.0
randVal = uniform(lower, upper)  # [lower, uppper]

iterations = 0

startTime = perf_counter()
while True:
    print("\nUpper boundary: " + str(upper))
    print("Lower boundary: " + str(lower))
    guess = uniform(lower, upper)
    iterations += 1
    if randVal == guess:
        print("Correct. The random number was " + str(randVal) + ".")
        break
    elif randVal > guess:
        print("Guess: " + str(guess))
        print("The guess is lower than the random number.")
        lower = guess
    else:
        print("Guess: " + str(guess))
        print("The guess is higher than the random number.")
        upper = guess
endTime = perf_counter()

print("\nThe computer took " + str(iterations) + " iterations to guess the random number.")
print("The computer took " + str(endTime - startTime) + " seconds to guess the random number.")

