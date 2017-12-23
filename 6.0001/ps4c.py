# Problem Set 4C
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string
from ps4a import get_permutations

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list


### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

# you may find these constants helpful
VOWELS_LOWER = 'aeiou'
VOWELS_UPPER = 'AEIOU'
CONSONANTS_LOWER = 'bcdfghjklmnpqrstvwxyz'
CONSONANTS_UPPER = 'BCDFGHJKLMNPQRSTVWXYZ'

class SubMessage(object):
    def __init__(self, text):
        '''
        Initializes a SubMessage object
                
        text (string): the message's text

        A SubMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
    
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
                
    def build_transpose_dict(self, vowels_permutation):
        '''
        vowels_permutation (string): a string containing a permutation of vowels (a, e, i, o, u)
        
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to an
        uppercase and lowercase letter, respectively. Vowels are shuffled 
        according to vowels_permutation. The first letter in vowels_permutation 
        corresponds to a, the second to e, and so on in the order a, e, i, o, u.
        The consonants remain the same. The dictionary should have 52 
        keys of all the uppercase letters and all the lowercase letters.

        Example: When input "eaiuo":
        Mapping is a->e, e->a, i->i, o->u, u->o
        and "Hello World!" maps to "Hallu Wurld!"

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        
        vowels_permutation_upper = vowels_permutation.upper()
        transp_dict = {}
        
        for i in range(len(CONSONANTS_LOWER)):
            transp_dict[CONSONANTS_LOWER[i]] = CONSONANTS_LOWER[i]
        
        for i in range(len(CONSONANTS_UPPER)):
            transp_dict[CONSONANTS_UPPER[i]] = CONSONANTS_UPPER[i]
            
        for i in range(len(VOWELS_LOWER)):
            transp_dict[VOWELS_LOWER[i]] = vowels_permutation[i]
            
        for i in range(len(VOWELS_UPPER)):
            transp_dict[VOWELS_UPPER[i]] = vowels_permutation_upper[i]

        return transp_dict

    def apply_transpose(self, transpose_dict):
        '''
        transpose_dict (dict): a transpose dictionary
        
        Returns: an encrypted version of the message text, based 
        on the dictionary
        '''
        letters = string.ascii_letters
        encrypted_text = ''

        for i in range(len(self.message_text)):
            if self.message_text[i] in letters:
                encrypted_text += transpose_dict[self.message_text[i]]
            else:
                encrypted_text += self.message_text[i]

        return encrypted_text
        
class EncryptedSubMessage(SubMessage):
    def __init__(self, text):
        '''
        Initializes an EncryptedSubMessage object

        text (string): the encrypted message text

        An EncryptedSubMessage object inherits from SubMessage and has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        SubMessage.__init__(self, text)

    def decrypt_message(self):
        '''
        Attempt to decrypt the encrypted message 
        
        Idea is to go through each permutation of the vowels and test it
        on the encrypted message. For each permutation, check how many
        words in the decrypted text are valid English words, and return
        the decrypted message with the most English words.
        
        If no good permutations are found (i.e. no permutations result in 
        at least 1 valid word), return the original string. If there are
        multiple permutations that yield the maximum number of words, return any
        one of them.

        Returns: the best decrypted message    
        
        Hint: use your function from Part 4A
        '''
        perm_scores = {}
        permutations = get_permutations('aeiou')
        
        for perm in permutations:
            valid_words = 0
            transp_dict = self.build_transpose_dict(perm)
            possible_text = self.apply_transpose(transp_dict)
            possible_text_list = possible_text.split()

            for word in possible_text_list:
                if is_word(self.valid_words, word):
                    if word == "I" or word == "love" or word == "programing!":
                        print(word)
                    valid_words += 1
            perm_scores[perm] = valid_words

        best_score = max(perm_scores.values())
        if best_score < 1:
            return self.message_text

        best_perm = max(perm_scores, key=lambda j: perm_scores[j])
        best_dict = self.build_transpose_dict(best_perm)
        best_message = self.apply_transpose(best_dict)

        return best_message
    

if __name__ == '__main__':

    # Example test case
#    message = SubMessage("Hello World!")
#    permutation = "eaiuo"
#    enc_dict = message.build_transpose_dict(permutation)
#    print("Original message:", message.get_message_text(), "Permutation:", permutation)
#    print("Expected encryption:", "Hallu Wurld!")
#    print("Actual encryption:", message.apply_transpose(enc_dict))
#    enc_message = EncryptedSubMessage(message.apply_transpose(enc_dict))
#    print("Decrypted message:", enc_message.decrypt_message())
     
    #TODO: WRITE YOUR TEST CASES HERE
    print("TEST CASE 1")
    print("-----------")
    test_message_1 = SubMessage("Programing is great!")
    permutation_1 = "uaoei"
    enc_dict_1 = test_message_1.build_transpose_dict(permutation_1)
    print("Original message:", test_message_1.get_message_text(), "Permutation:", permutation_1)
    print("Expected_encrytion:", "Pregrumong os graut!")
    print("Actual encryption:", test_message_1.apply_transpose(enc_dict_1))
    enc_message_1 = EncryptedSubMessage(test_message_1.apply_transpose(enc_dict_1))
    print("Decrypted message:", enc_message_1.decrypt_message())

    print("-------------------------------------------------------")
    
    print("TEST CASE 2")
    print("-----------")
    test_message_1 = SubMessage("The souls of the damned.")
    permutation_1 = "ioaue"

    enc_dict_1 = test_message_1.build_transpose_dict(permutation_1)
    print("Original message:", test_message_1.get_message_text(), "Permutation:", permutation_1)
    print("Expected_encrytion:", "Tho suels uf tho dimnod.")
    print("Actual encryption:", test_message_1.apply_transpose(enc_dict_1))
    enc_message_1 = EncryptedSubMessage(test_message_1.apply_transpose(enc_dict_1))
    print("Decrypted message:", enc_message_1.decrypt_message())
    
    