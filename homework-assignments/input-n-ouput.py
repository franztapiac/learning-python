# Homework assignment 08
# Input & Output
# Written by Franz A. Tapia Chaca
# on 08 February 2021

#######################
# Note-taking program #
#######################
# On start up, the user is prompted for a filename.
# If the filename doesn't exist:
#   User is prompted to enter the text they wish to write to the file
#   After text is entered, the file is saved and program is exited.
# If the filename does exist:
#   The user is prompted to A) read the file, B) delete the file and start over
#   C) append the file, and D) replace a single line.
#   If A)
#       The contents of the file are printed on the screen
#   If B)
#       File is deleted and another empty one is made in its place
#   If C)
#       User enters more text that is appended to the file
#   If D)
#       User is prompted for the line they want to update, and the replacing text.

import os.path

filename = input("Please enter a filename: ")

if os.path.isfile(filename):
    # File name exists
    option = input("Which of the following do you wish to do?\n"
                   "A) Read the file\n"
                   "B) Delete the file and start the file over\n"
                   "C) Append to the file\n"
                   "D) Replace a single line\n")

    # Read the file
    if option == "A":
        file = open(filename, "r")
        print("Contents of the file:\n")
        print(file.read())
        file.close()

    # Delete the file and start the file over
    elif option == "B":
        with open(filename, "w") as tempFile:  # overwrite the file clean
            print("'" + filename + ".txt' has been started over.")
        file = open(filename, "r")
        print("Contents of the file:\n")
        print(file.read())
        file.close()

    # Append to the file
    elif option == "C":
        file = open(filename, "a")
        toAppend = input("What do you wish to append to the file?\n")
        file.write(toAppend + "\n")
        print("Contents of the file:\n")
        file.close()

        with open(filename, "r") as tempFile:
            print("New contents of the file: ")
            print(tempFile.read())

    # Replace a single line
    elif option == "D":

        # Display the lines, numbered
        with open(filename, "r") as tempFile:
            print("These are the contents of '" + filename + ".txt':")
            lineCount = 0
            for line in tempFile:
                lineCount += 1  # ends with the total number of lines
                print("Line #" + str(lineCount) + ": " + line.strip("\n"))

        # Prompt for update information
        lineChoice = int(input("Which line do you want to update?\n#"))
        replacingText = input("What do you want to replace line "
                              + str(lineChoice) + " with?\n")

        # Replace the chosen line
        with open(filename, "r") as tempFile:
            fileLines = tempFile.readlines()  # stores list of lines
            fileLines[lineChoice-1] = replacingText + "\n"  # new list updated

        # Update the file
        with open(filename, "w") as tempFile:
            for line in range(1, len(fileLines)+1):  # 1 to num of lines
                tempFile.write(fileLines[line-1])

        # Show the new contents of the file
        with open(filename, "r") as tempFile:
            print("New contents of the file: ")
            print(tempFile.read())

else:
    # File name doesn't exist
    file = open(filename, "w")
    textInput = input("What do you wish to write to '" + filename + ".txt'?\n")
    file.write(textInput + "\n")
    file.close()

    # Show the new contents of the file
    with open(filename, "r") as tempFile:
        print("New contents of the file: ")
        print(tempFile.read())
