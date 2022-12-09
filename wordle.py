from wordle_functions import *

guesses = read_csv('valid_guesses.csv')
solutions = read_csv('valid_solutions.csv')

gains = [[0 for x in range(len(solutions))] for x in range(len(guesses))] # secondary index(solutions) on inside, first index on outside(guesses)
for g_index, guess in enumerate(guesses):
    print("line number "+ str(g_index)+ ": "+str(guess))
    
    for w_index, word in enumerate(solutions):
        gains[g_index][w_index] = infogain(guess,word)
        # need to implement pushing values to vector instead of accumulating
    print(sum(gains[g_index])) # should sum all values of a given word in the guess set, before infogain() is completed this should just return the amount of elements in the solution set
    