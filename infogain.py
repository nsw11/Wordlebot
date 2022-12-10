import math
import string

def generate_all_result_combinations():
    all_result_combinations = []
    for i in range(3):
        for j in range (3):
            for k in range (3):
                all_result_combinations.append([i,j,k])
    return all_result_combinations

# Returns the expected information of one guess.
# guess: 5 letters representing a word with an expected information when we make a guess
# possible_words: the possible solutions. If its the first guess the possible_words are
# all the words. If it's a subsequent guess it is the filtered word space.
def expected_infogain(guess,possible_words): #filler function please replace

    sum = 0
    # for each possible combination of results:
    # add probability of that guess*log(probability^-1)to sum
    # TODO enumerate all possible results ([0-2, 0-2, 0-2, 0-2, 0-2])
    for result in generate_all_result_combinations():
        # information of one guess based on its result
        sum += probability(guess, result, possible_words)*infogain(guess, result, possible_words)
    return sum

# returns the probabilIty that a guess ends with a given result
# e.g. The probability that the guess CRANE returns [0,0,0,0,1] = 0.32
def probability(guess, result, possible_words):
    # get total number of possible words before we've seen our results
    num_of_words = len(possible_words)
    # find number of possible solution after filtering with results
    num_pos_solutions = len(filter_guess(guess, result, possible_words))
    return num_pos_solutions/num_of_words

# return the info we get from making a guess and getting a result back
def infogain(guess, result, possible_words):
    prob = probability(guess, result, possible_words)
    return math.log(1/prob, 2)

# Returns a list of all possible solutions after filtering a guess
# with it's result.
# e.g. filter_guess(float, [2,0,0,0,0], valid_guesses.csv) returns [bloat, gloat]
# Known issue: words with double letters do not work
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
                if guess[idx] in word:
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

