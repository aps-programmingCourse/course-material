#!/usr/bin/python3

import random
from gallows import *

def hangman():
    wordList = open("wordList", "r")
    words = wordList.read().splitlines()
    wordToGuess = random.choice(words)
    completedWord = []

    for char in wordToGuess:
        completedWord.append("_")

    lettersGuessed = ''
    incorrectLetters = ''
    i = 0

    while True:
        for e in range(0, 50):
            print("")

        print("Incorrect letters: ", incorrectLetters, '\n' + gallowsList[i])

        if i == 6:
            print("Sorry, you lost.")
            print("The word was", wordToGuess + ". Do you want to try again? ")
            if input("y/n: ") == "y":
                hangman()
            else:
                print("Exiting...")
                return False

        for char in wordToGuess:
            if char in lettersGuessed:
                print(char, end=" ")
            else:
                print("_", end=" ")

        print("","\n")

        wordGuess = input("Enter a letter or a word: ")

        if wordGuess == wordToGuess:
            print("You've guessed the word! ")
            break

        if (len(wordGuess) > 1 and wordGuess != wordToGuess) or (len(wordGuess) == 1 and wordGuess not in wordToGuess):
            i += 1
            print("That letter is not in the word or the correct word, sorry. ")
            incorrectLetters += wordGuess + " "

        if wordGuess in wordToGuess:
            lettersGuessed += wordGuess

hangman()
