
from wordle_functions import *

guesses = read_csv('valid_guesses.csv')
solutions = read_csv('valid_solutions.csv')

gains = [[0 for x in range(len(solutions))] for x in range(len(guesses))] # secondary index(solutions) on inside, first index on outside(guesses)
for g_index, guess in enumerate(guesses):
    #print("line number "+ str(g_index)+ ": "+str(guess))
    
    for w_index, word in enumerate(solutions):
        gains[g_index][w_index] = g_index
        # need to implement pushing values to vector instead of accumulating
    #print(sum(gains[g_index])) # should sum all values of a given word in the guess set, before infogain() is completed this should just return the amount of elements in the solution set

write_csv("results.csv",gains)

##########
def find_best_guess(possible_guesses):
    best_information = -sys.maxsize -1
    best_guess_index = -1
    for idx, word in enumerate(possible_guesses):
        expected_info = expected_infogain(word, possible_guesses)
        # print(word, "expected info:", expected_info)
        if expected_info > best_information:
            best_information = expected_info
            best_guess_index = idx
    return possible_guesses[best_guess_index]

# print(find_best_guess(read_csv('3b1b_valid_guesses.csv')))

# first_guess = filter_guess("seals", [2,2,2,0,2], read_csv('valid_guesses.csv'))
# # print(first_guess)
# print("guess:", find_best_guess(first_guess))
# second_guess = filter_guess("doilt", [2,2,1,0,2], first_guess)
# print("guess:", find_best_guess(second_guess))
# third_guess = filter_guess("gilly", [2,0,0,0,0], second_guess)
# print("guess:", find_best_guess(third_guess))