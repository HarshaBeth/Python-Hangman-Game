def printHangman():
    print(" ______")
    print(" |    |")
    print(" |")
    print(" |")
    print(" |")
    print(" |")
    print("^^^")


def firstError():
    print(" ______")
    print(" |    |")
    print(" |  (^_^)")
    print(" |")
    print(" |")
    print(" |")
    print("^^^")


def secondError():
    print(" ______")
    print(" |    |")
    print(" |  (^_^)")
    print(" |    |")
    print(" |    |")
    print(" |")
    print("^^^")


def thirdError():
    print(" ------")
    print(" |    |")
    print(" |  (^_^)")
    print(" |    |")
    print(" |    |")
    print(" |   /")
    print("^^^")


def fourthError():
    print(" ------")
    print(" |    |")
    print(" |  (^_^)")
    print(" |    |")
    print(" |    |")
    print(" |   / \\")
    print("^^^")


def fifthError():
    print(" ------")
    print(" |    |")
    print(" |  (^_^)")
    print(" |   /|")
    print(" |    |")
    print(" |   / \\")
    print("^^^")


def sixthError():
    print(" ------")
    print(" |    |")
    print(" |  (^_^)")
    print(" |   /|\\")
    print(" |    |")
    print(" |   / \\")
    print("^^^")


yOrN = "y"
count = 1
dashesCounter = 0

word = "zootopia"
dashesToFill = ['_']

dashesToFill *= len(word)



while(yOrN.lower() == "y"):

    printHangman()

    for i in range(len(word)):  # Printed dashes and hangman frame
        print(dashesToFill[i], end=" ")

    print()

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if(dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)


    firstError()
    count = 1

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if (dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)

    secondError()
    count = 1

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if (dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)

    thirdError()
    count = 1

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if (dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)

    fourthError()
    count = 1

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if (dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)

    fifthError()
    count = 1

    while (count != 0):

        dashesCounter = 0
        count = 0
        guess = input("Guess a letter: ")

        for i in range(len(word)):
            if (guess[0] == word[i]):
                dashesToFill[i] = guess[0]
                count += 1

        for i in range(len(word)):
            print(dashesToFill[i], end=" ")

            if (dashesToFill[i] == "_"):
                dashesCounter += 1

        print()

        if (dashesCounter == 0):
            print("CONGRATS! YOU WON")
            exit(0)

    sixthError()
    count = 1

    print("GAME OVER. YOU LOST")
    yOrN = input("Press Y to play again. Press any other key to exit. \n")
