import math

# Returns the expected information of one guess.
# A guess consist of ordered 5 letters
# The expected information is derived by summing the probability 
# and the information gained of each possible result.
def infogain (guess,word): #filler function please replace

    sum = 0
    # for each possible combination of results:
    # add probability of that guess*log(probability^-1)to sum
    # TODO enumerate all possible results ([0-2, 0-2, 0-2, 0-2, 0-2])
    for result in all_possible_results:
        probability = probability(guess, result)
        sum += probability*math.log(1/probability, 2)

    return sum

# returns the probabilty that a guess ends with a given result
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
def filter_guess(guess, result):
    raise NotImplemented