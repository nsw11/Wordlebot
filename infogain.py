import math
import string

# Returns the expected information of one guess.
# A guess consist of ordered 5 letters
# The expected information is derived by summing the probability 
# and the information gained of each possible result.
def infogain(guess,word): #filler function please replace

    sum = 0
    # for each possible combination of results:
    # add probability of that guess*log(probability^-1)to sum
    # TODO enumerate all possible results ([0-2, 0-2, 0-2, 0-2, 0-2])
    for result in all_possible_results:
        probability = probability(guess, result)
        # information of one guess based on its result
        sum += probability*math.log(1/probability, 2)

    return sum

# returns the probabilIty that a guess ends with a given result
# e.g. The probability that the guess CRANE returns [0,0,0,0,1] = 0.32
def probability(guess, result):
    num_of_words = len(solutions)
    
    # find number of possible solution after filtering with results
    # TODO some filter function
    num_pos_solutions = len(filter_guess(guess, result))
    return num_of_words/num_pos_solutions

# Returns a list of all possible solutions after filtering a guess
# with it's result.
# e.g. filter_guess(FLOAT, [0,2,2,2,2]) returns [BLOAT]
def filter_guess(guess, result, all_possible_words):

    # a list with 5 elements.
    # each element is a set of all possible letters.
    word_vector = [set(string.ascii_lowercase) for i in range(5)]

    # filter word vector based on result
    for i, color in enumerate(result):
        if color == 0: # green
            word_vector[i] = guess[i]
        elif color == 1: # yellow
            word_vector[i].remove(guess(i))
        elif color == 2: # grey
            for idx in word_vector:
                idx.remove(guess[i])
    # this is not ideal: for a yellow result we remove a letter for that pos, but
    # nothing to enforce that letter must be in some other pos. Perhaps good enough

    # add up list of all possible words
    list_possible_words = []
    for word in all_possible_words:
        for letter, v_letter in zip(word, word_vector):
            if letter not in v_letter:
                continue
        list_possible_words.append(word)
        # does word match -
    return list_possible_words