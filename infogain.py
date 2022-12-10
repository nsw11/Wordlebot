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
# e.g. filter_guess(float, [0,2,2,2,2]) returns [bloat, gloat]
def filter_guess(guess, result, all_possible_words):

    # Returns whether a given word is compatible with a given result
    def match_filter(guess, result, word) -> bool:
        for idx, color in enumerate(result):
            if color == 0: # green
                # check if green letter is not in the potential word at idx
                if word[idx] != guess[idx]:
                    return False # disqualify
            elif color == 1: # yellow
                # check if word doesn't contains this letter,
                # or if the yellow letter is in the same spot
                if guess[idx] not in word or word[idx] == guess[idx]:
                    return False
            elif color == 2: #grey
                # check if grey letter is in the potential word at idx
                if word[idx] == guess[idx]:
                    return False
        
        #if we've gone through all 5 positions and the word pass, it qualifies
        return True
    
    possible_words = []
    for word in all_possible_words:
        # check if the word is compatible with the results
        if match_filter(guess, result, word):
            # append to list if so
            possible_words.append(word)

    return possible_words

# some test cases
import wordle_functions
possible_words = wordle_functions.read_csv('valid_solutions.csv')
guess = "float"
result = [2,0,0,0,0]
print(filter_guess(guess, result, possible_words))
assert filter_guess(guess, result, possible_words) == ["bloat", "gloat"]
guess = "chess"
result = [2, 2, 2, 1, 0]
print(filter_guess(guess, result, possible_words))
