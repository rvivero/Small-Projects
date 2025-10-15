#test
import random

NUM_DIGITS = 3 #(!) try setting this to 1 or 10
MAX_GUESSES = 10 #(!) try setting this to 1 or 100

print('''Bagels, a deductive logic game.
By Al Sweigart al@inventwithpython.com
          
I am thinking of a {}-digit number with no repeated digits.
Try to guess what it is. Here are some clues:
When i say:   That means:
Pico          One digit is correct but in the wrong position
Fermi         One digit is correct and in the right position
Bagels        No digit is correct

For example, if the secret number was 248 and your guess was 843
the clues would be Fermi Pico'''.format(NUM_DIGITS))
