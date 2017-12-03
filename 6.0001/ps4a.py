# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    
    listed_sequence = list(sequence)

    if len(listed_sequence) == 1:
        return listed_sequence
    else:
        first_char = listed_sequence[0]
        del listed_sequence[0]
        permutations = get_permutations(listed_sequence)
        new_permutations = []
        for permutation in permutations:
            for j in range(len(permutation) + 1):
                new_permutations.append(permutation[:j] + first_char + permutation[j:])
        return new_permutations

if __name__ == '__main__':
#    #EXAMPLE
#    example_input = 'abc'
#    print('Input:', example_input)
#    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
#    print('Actual Output:', get_permutations(example_input))
    
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a 
#    sequence of length n)

    print("TEST CASE 1")
    print("------------")
    example_input_1 = 'abc'
    print("Input:", example_input_1)
    print("Expected Output:", ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print("Actual Output:", get_permutations(example_input_1))
    
    print("TEST CASE 2")
    print("------------")
    example_input_2 = 'tea'
    print("Input:", example_input_2)
    print("Expected Output:", ['aet', 'ate', 'eat', 'eta', 'tae', 'tea'])
    print("Actual Output:", get_permutations(example_input_2))
    
    print("TEST CASE 3")
    print("------------")
    example_input_3 = 'band'
    print("Input:", example_input_3)
    print("Expected Output:", ['abdn', 'abnd', 'adbn', 'adnb', 'anbd', 'andb', 'badn', 'band', 'bdan', 'bdna', 'bnad', 'bnda', 'dabn', 'danb', 'dban', 'dbna', 'dnab', 'dnba', 'nabd', 'nadb', 'nbad', 'nbda', 'ndab', 'ndba'])
    print("Actual Output:", get_permutations(example_input_3))
    


