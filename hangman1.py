import random

name = input("What is your name?\n")
print("Hello ", name)
print("Welcome to the Hangman Game \nBest of luck")

words = ["balloon", "hook", "octopus", "communication", "piano", "honey", "playstation"]
guesses = ''
word = random.choice(words)
print("Guess the characters!")

turns = 6

# main loop of game
while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char)
        else:
            print("_")

            failed += 1

    if failed == 0:
        print("You win")
        print("The word is ", word)
        break

# taking user input
    guess = input("guess any letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("wrong")
        print(f"You have {turns} turns left")

    if turns == 0:
        print("You Lose")
