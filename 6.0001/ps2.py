# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"
VOWELS = "aieou"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    secret_word_list = list(secret_word)
    secret_word_list_copy = secret_word_list[:]
    
    for i in letters_guessed:
        for j in secret_word_list_copy:
            if i == j:
                secret_word_list.remove(j)
                if len(secret_word_list) == 0:
                    break
    
    if len(secret_word_list) == 0:
        return True
    else:
        return False
                

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    secret_word_list = list(secret_word)
    user_guess = []
    
    for letter in secret_word:
        user_guess.append('_ ')
    
    for i in range(len(letters_guessed)):
        for j in range(len(secret_word_list)):
            if letters_guessed[i] == secret_word_list[j]:
                user_guess[j] = secret_word_list[j]
    
    return ''.join(user_guess)
                


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    available_letters = list(string.ascii_lowercase)
    
    for letter in letters_guessed:
        available_letters.remove(letter)
    
    return ''.join(available_letters)



def get_number_of_unique_letters(secret_word):
    '''
    secret_word: string, the word the user is guessing
    returns: integer, accounting for the number of unique letters
      in secret_word
    '''
    unique_words = []
    
    for letter in secret_word:
        if not letter in unique_words:
            unique_words.append(letter)
    
    return len(unique_words)

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    warnings_remaining = 3
    letters_guessed = []
    guesses_remaining = 6
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_remaining) + " warnings left.")
    print("-------------")
    
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_remaining > 0:
        print("You have " + str(guesses_remaining) + " guesses left.")
        print("Available letters " + get_available_letters(letters_guessed))
        
        user_input = input("Please guess a letter: ")
    
        if not user_input.isalpha():
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! That is not a valid letter. You have no warnings left: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
            
        user_input = user_input.lower()
        
        if user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter.. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you loose one guess: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
        
        letters_guessed.append(user_input)
        
        if not user_input in secret_word:
            if user_input in VOWELS:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
            
        print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        print("-------------")
    
    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    else:
        score = guesses_remaining * get_number_of_unique_letters(secret_word)
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(score))

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    trimmed_word = my_word.replace(' ' , '')
    
    # if words are of different length, return False
    if len(trimmed_word) != len(other_word):
        return False
    
    # if a letter in a position of my_word is different from the letter in
    # the same position of other_word, return False
    # if a letter in a position of my_word equal to the letter in the same
    # position of other_word, it must occur the same number of times in both
    for i in range(len(trimmed_word)):
        if trimmed_word[i] != '_' and trimmed_word[i] != other_word[i]:
            return False
        elif trimmed_word[i] != '_' and trimmed_word[i] == other_word[i]:
            trimmed_word_count = 0
            other_word_count = 0
            for k in range(len(trimmed_word)):
                if trimmed_word[k] == trimmed_word[i]:
                    trimmed_word_count += 1
            for l in range(len(other_word)):
                if trimmed_word[i] == other_word[l]:
                    other_word_count += 1
            if trimmed_word_count != other_word_count:
                return False
    
    return True



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    possible_matches = []
    
    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) == 0:
        print("No matches found")
    else:
        print(' '.join(possible_matches), end=' ')
    return '' # return empty string in order for 'None' not to be printed


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    warnings_remaining = 3
    letters_guessed = []
    guesses_remaining = 6
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(len(secret_word)) + " letters long.")
    print("You have " + str(warnings_remaining) + " warnings left.")
    print("-------------")
    
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_remaining > 0:
        print("You have " + str(guesses_remaining) + " guesses left.")
        print("Available letters " + get_available_letters(letters_guessed))
        
        user_input = input("Please guess a letter: ")
    
        if not user_input.isalpha():
            if user_input == '*':
                print("Possible word matches are:")
                print(show_possible_matches(secret_word))
            else:
                if warnings_remaining > 0:
                    warnings_remaining -= 1
                    print("Oops! That is not a valid letter. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_remaining -= 1
                    print("Oops! That is not a valid letter. You have no warnings left: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
            
        user_input = user_input.lower()
        
        if user_input in letters_guessed:
            if warnings_remaining > 0:
                warnings_remaining -= 1
                print("Oops! You've already guessed that letter.. You have " + str(warnings_remaining) + " warnings left: " + get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_remaining -= 1
                print("Oops! You've already guessed that letter. You have no warnings left, so you loose one guess: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
        
        letters_guessed.append(user_input)
        
        if not user_input in secret_word:
            if user_input in VOWELS:
                guesses_remaining -= 2
            else:
                guesses_remaining -= 1
            print("Oops! That letter is not in my word: " + get_guessed_word(secret_word, letters_guessed))
            print("-------------")
            continue
            
        print("Good guess: " + get_guessed_word(secret_word, letters_guessed))
        print("-------------")
    
    if guesses_remaining == 0:
        print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
    else:
        score = guesses_remaining * get_number_of_unique_letters(secret_word)
        print("Congratulations, you won!")
        print("Your total score for this game is: " + str(score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
#     pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
