from wordle_functions import *
from infogain import *
from greedy import *
from wordle import input_results

wordspace = read_csv('3b1b_valid_guesses.csv')
list_to_txtfile(wordspace, "words.txt")
for i in range(5):
    best_guess = greedy()
    result = input_results()
    wordspace = filter_guess(best_guess, result, wordspace)
    print(wordspace)
    print(len(wordspace), "remaining words:")
    list_to_txtfile(wordspace, "words.txt")