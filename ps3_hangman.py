# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    flag = True

    for letter in secretWord:
        if letter in lettersGuessed:
            flag = True
        else:
            flag = False
            break

    return flag


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''

    answer = ''

    for letter in secretWord:
        if letter in lettersGuessed:
            answer = answer + letter
        else:
            answer = answer + ' _'
    return answer


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    answer = ''

    for letter in alphabet:
        if letter in lettersGuessed:
            answer = answer
        else:
            answer = answer + letter
    return answer


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''

    print("\nAlright! Let's play a game of hangman! First off, the secret word contains ", len(secretWord), end=" letters.\n\n")

    ready_to_play = input("Are you ready to play?? Please type yes or no\n").lower()
    if ready_to_play == 'y' or 'yes':
        playing = True
    else:
        ready_to_play = False

    mistakesMade = 0
    lettersGuessed = []
    availableLetters = 'abcdefghijklmnopqrstuvwxyz'

    while playing and mistakesMade < 8:

        guess = input("what will your guess be?\n").lower()
        lettersGuessed.append(guess)

        if isWordGuessed(secretWord, lettersGuessed):
            print("you win")
            playing = False

        else:

            if guess not in secretWord:
                mistakesMade = mistakesMade + 1
            print("\n\n\n\n\n\n\n\n\n\n")
            print("you have ", 8 - mistakesMade, end=" guesses left\n")
            print(getGuessedWord(secretWord, lettersGuessed))
            print("these are the letters you haven't guessed yet")
            print(getAvailableLetters(lettersGuessed))
            print("\n\n\n\n\n\n\n\n\n\n")

    print("the word was " + secretWord)


# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
