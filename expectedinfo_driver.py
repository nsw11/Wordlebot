
from wordle_functions import *
from infogain import *
import sys
from wordle import *

initial_wordspace = read_csv('3b1b_valid_guesses.csv')
# print("Calculating best first guess from", len(initial_wordspace), "words...")
# print("The best first guess is:", find_best_guess(initial_wordspace))
print("The best first guess is: seals")
result = input_results()

best_guess = "seals"
new_wordspace = initial_wordspace
for i in range(5):
    new_wordspace = filter_guess(best_guess, result, new_wordspace)
    print(new_wordspace)
    print(len(new_wordspace), "remaining words:")
    best_guess = find_best_guess(new_wordspace)
    print("The next best guess with highest expected info:", best_guess)
    result = input_results()

# first_guess = filter_guess("seals", result, initial_wordspace)
# print(len(first_guess), "remaining words:")
# print(first_guess)
# print("The next best guess with highest expected info:", find_best_guess(first_guess))
# result = input_results()

# second_guess = filter_guess("dared", result, first_guess)
# print(len(second_guess), "remaining words:")
# print(second_guess)
# print("The next best guess with highest expected info:", find_best_guess(second_guess))
# result = input_results()