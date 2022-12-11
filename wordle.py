from wordle_functions import *
import sys
from infogain import *

# guesses = read_csv('valid_guesses.csv')
# solutions = read_csv('valid_solutions.csv')

# gains = [[0 for x in range(len(solutions))] for x in range(len(guesses))] # secondary index(solutions) on inside, first index on outside(guesses)
# for g_index, guess in enumerate(guesses):
#     print("line number "+ str(g_index)+ ": "+str(guess))
    
#     for w_index, word in enumerate(solutions):
#         gains[g_index][w_index] = infogain(guess,word)
#         # need to implement pushing values to vector instead of accumulating
#     print(sum(gains[g_index])) # should sum all values of a given word in the guess set, before infogain() is completed this should just return the amount of elements in the solution set
    

##########
def find_best_guess(possible_guesses):
    best_information = -sys.maxsize -1
    best_guess_index = -1
    sum = 0
    for idx, word in enumerate(possible_guesses):
        # print("word:", word)
        # print("idx:", idx)
        expected_info = expected_infogain(word, possible_guesses)
        # print(word, "expected info:", expected_info)
        if expected_info > best_information:
            best_information = expected_info
            best_guess_index = idx
    return possible_guesses[best_guess_index]

def input_results():
    n = 5
    result = list(map(int,input("\nEnter the results: ").strip().split()))[:n]
    print()
    return result

initial_wordspace = read_csv('3b1b_valid_guesses.csv')
# print("Calculating best first guess from", len(initial_wordspace), "words...")
# print("The best first guess is:", find_best_guess(initial_wordspace))
print("The best first guess is: seals")
result = input_results()

first_guess = filter_guess("seals", result, initial_wordspace)
print(len(first_guess), "remaining words:")
print(first_guess)
print("The next best guess with highest expected info:", find_best_guess(first_guess))
result = input_results()

second_guess = filter_guess("dared", result, first_guess)
print(len(second_guess), "remaining words:")
print(second_guess)
print("The next best guess with highest expected info:", find_best_guess(second_guess))
result = input_results()