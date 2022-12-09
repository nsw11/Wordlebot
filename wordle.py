from wordle_functions import *

def infogain (guess,word): #filler function please replace
    return 1

guesses = read_csv('valid_guesses.csv',True)
solutions = read_csv('valid_solutions.csv',True)


for guess in guesses:
    total = 0
    for word in solutions:
        total += infogain(guess,word)
        # need to implement pushing values to vector instead of accumulating
    avg = total/ len(solutions)