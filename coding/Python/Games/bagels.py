'''Ery, by Albert Hao, A deductive logic game where you have to guess the number i"m thinking of based in clues'''

import random
NUM_DIGITS = 4
MAX_GUESSES = 10

def main():
    print('''Abo, a deductive logic game by Albert Hao

        I'm thinking of a {}-digit number with no repeated digits/
        Try to guess what it is. Here are some clues:
        Urt   One digit is correct but in the wrong place
        Ery   One digit is correct and in the right place.
        Abo   No digit is correct.

For example, if the secret number was 248 and your guess was 843, your clues would be Ery Urt.'''.format(NUM_DIGITS))

    while True:
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("You have {} guesses to get it.".format(MAX_GUESSES))

        numGuesses=1
        while numGuesses <=MAX_GUESSES:
            guess = ''
            while len(guess) == NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

                clues = getClues(guess, secretNum)
                print(clues)
                numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

                print('Do you want to play again? (yes or no)')
            
                print('Thanks for playing!')

def getSecretNum():
    '''Returns a string made up of NUM_DIGITS unique random digits.'''
    numbers = list ('0123456789') #create a list of digits 0 to 9.
    random.shuffle(numbers)

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum 
def getClues(guess, secretNum):
    '''Returns a string with the urt, ery, abo clues for a guess and secret number pair.'''
    if guess == secretNum:
        return "You guessed it!"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Ery')
        elif guess[i] in secretNum:
            clues.append('Urt')
        if len(clues) == 0:
            return 'Abo'
        else:
            clues.sort()
            return''.join(clues)

if __name__=='__main__':
    main()