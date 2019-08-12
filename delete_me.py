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


print(getGuessedWord('apple', ['f', 'r', 'l', 'e', 'a']))


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


poop = ['f', 'r', 'l', 'e', 'a']
print(getAvailableLetters(poop))
