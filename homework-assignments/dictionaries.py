# Pirple: Python is Easy
# Homework Assignment 07 - Dictionaries and Sets
# Written by Franz A. Tapia Chaca
# on 01 Feburary 2021

# Practice using dictionaries
# Program:
# 1) Details of a song are stored in a dictionary, and a single loop
# prints out the song's details
# 2) The user is prompted to guess the dictionary keys and values,
# and is told if the guesses were correct or not.

# Dictionary
favouriteSong = {"title": "Christ is Mine Forevermore",
                 "artist": "CityAlight",
                 "releaseYear": 2016,
                 "album": "Only a Holy God",
                 "durationInSeconds": 5*60 + 28,
                 "genre": "Christian worship",
                 "CCLInum": 7036096
                 }

# Print dictionary
print("favouriteSong Dictionary keys and values:")
for key in favouriteSong.keys():
    print(key + ": " + str(favouriteSong[key]))


# Function that determines the correctness of user's guess
def guess(keyGuess, valueGuess):
    if keyGuess in favouriteSong and valueGuess == str(favouriteSong[keyGuess]):
        return True
    else:
        return False


# Prompt user to guess a key and its value
print("\nI have a dictionary called favouriteSong")
keyGuess = input("Guess a key in it : ")
valueGuess = input("Guess the key's value: ")

print("Does the key exist in favouriteSong and is its value correct?")
print(str(guess(keyGuess, valueGuess)) + "\n")
