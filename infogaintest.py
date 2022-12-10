from infogain import filter_guess, probability, generate_all_result_combinations, infogain, expected_infogain
import math
import wordle_functions

possible_words = wordle_functions.read_csv('testing/3b1b_valid_guesses.csv')

# test filter_guess
# print(filter_guess("weary", [2, 1, 2, 2, 2], ["yodel", "zones"]))
assert filter_guess("weary", [2, 1, 2, 2, 2], ["yodel", "zones"]) == ["zones"]

guess = "float"
result = [2,0,0,0,0]
# print(filter_guess(guess, result, possible_words))
assert filter_guess(guess, result, possible_words) == ["bloat", "gloat", "ploat"]

guess = "weary"
result = [2, 1, 2, 2, 2]
# print(filter_guess(guess, result, possible_words))
# print(len(filter_guess(guess, result, possible_words)))
assert len(filter_guess(guess, result, possible_words)) == 1418


# test generate generate_all_result_combinations
assert generate_all_result_combinations() == [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [0, 2, 0], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 0], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]


# test expected_infogain
prob = probability("weary", [2, 1, 2, 2, 2], possible_words)
print("prob = ", prob)
assert prob == 1418.0/12953.0
infogain_weary = infogain("weary", [2, 1, 2, 2, 2], possible_words)
print("infogain_weary =", infogain_weary)
print("math.log(1/0.1094727, 2) = ", math.log(1/0.1094727090249363, 2))
assert infogain_weary == math.log(1/0.1094727090249363, 2)
print("expectedgain:", expected_infogain("weary", possible_words))
# assert expected_infogain("weary", possible_words) == 4.9