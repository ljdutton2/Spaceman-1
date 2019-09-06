import random

def load_word():
    '''
    Fn reads text file of words and selects one randomly (secret word).  

    Returns:
        string: the secret word to be used in the game
    '''
    f = open('words.txt', 'r')   # opens words.txt and returns as file. r = read
    words_list = f.readlines()   # returns list w/ each line as list item 
    f.close()                    # closes opened file. Cannot be read anymore

    words_list = words_list[0].split(' ')  # split a string into a list
    secret_word = random.choice(words_list)  # random word from list

    return secret_word      #secret word returned

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word
    have been guessed. 

    Args: 
        secret _word (string): random word user is trying to guess
        letters_guessed (list of strings): letters that been guessed
    
    Returns:
        bool: True only if all letters in secret_word are in letters_guessed
    '''
    # Loop through the letters in the secret_word and check if a letter
    # not in lettersGuessed
    correctly_guessed_letters=[]
    i = 0

    for (guessed_letter in secret_word):
        if (secret_word.find(guessed_letter) == True):
            guessed_letter = correctly_guessed_letters[i]
            i +=


def get_guessed_word (secret_word, letters_guessed):
    '''
    Used to get a string showing the correct letters guessed 
    in the secret word and underscores for letters not guessed yet

    Args: 
        secret_word (string): the random word the user is trying to guess
        letters_guessed (list of strings): list of letters that have been guessed 

    Returns: 
        string: letters and underscores. For letters in the word that the user has
    '''
    # Loop through the letters in secret word and build a string that shows the
    # letters that have been guessed correctly so far that are saved in 
    # letters_guessed and underscores for the letter that have not been guessed

    pass


def is_guess_in_word(guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word
    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word
    Returns:
        bool: True if the guess is in the secret_word, False otherwise
    '''
    #TODO: check if the letter guess is in the secret word

    pass




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''


    #TODO: show the player information about the game according to the project spec

    #TODO: Ask the player to guess one letter per round and check that it is only one letter

    #TODO: Check if the guessed letter is in the secret or not and give the player feedback

    #TODO: show the guessed word so far

    #TODO: check if the game has been won or lost






#These function calls that will start the game
secret_word = load_word()
spaceman(load_word())


