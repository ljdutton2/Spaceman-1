

from random import choice




def load_word():
    '''
    Fn reads text file of words and selects one randomly (secret word).  

    Returns:
        string: the secret word to be used in the game
    '''
    f = open('words.txt', 'r')   # opens words.txt and returns as file. r = read
    words_list = f.readlines()   # returns list w/ each line as list item 
    f.close()                    # closes opened file. Cannot be read anymore

    words_list = words_list[0].split(' ')   # split a string into a list
    secret_word = choice(words_list)        # random word from list

    return secret_word           #secret word returned







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
    
    lengthofsecretword = len(secret_word)
    i = 0

    for letter in letters_guessed:
        number_of_letters = secret_word.count(letter)
        if (number_of_letters > 0):
            i += number_of_letters

    if lengthofsecretword == i:
        return True
    else: False








def old_get_guessed_word (secret_word, letters_guessed):
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

    display_array1 = ["_"] * len(secret_word)
    print(display_array1)

    for letter in letters_guessed:
        i = 0
        for dif_letter in secret_word:
            if (letter == dif_letter):
                display_array1[i] = letter
                i = i + 1
    

    return display_array1
    #pass


def new_get_guessed_word (secret_word, letters_guessed):
    display_array = " "
    for letter in secret_word:
        if letter in letters_guessed:
            display_array += (letter + " ")
        else:
            display_array += ('_ ')
    return print(display_array)









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

    for letter in secret_word:
        if (guess == letter):
            return True
    return False
        

    #pass







def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.
    Args:
      secret_word (string): the secret word to guess.
    '''    




    letters_guessed = " "
    tries = 7
   

    #TODO: show the player information about the game according to the project spec
    # INTRODUCTION
    print('')
    print f('You have {tries} tries to guess the word correctly')
    #print (' _ ' * len(secret_word))
    new_get_guessed_word(secret_word, letters_guessed)
    print('')




    #TODO: Ask the player to guess one letter per round and check that it is only one letter
    # USER_INPUT: GUESS
    guess = input('Guess one letter.. ')
    letters_guessed += guess

    if (len(guess) != 1 or type(guess) != str):
        print('No thanks. One letter. Try again.')
        guess = input('Guess a letter..')




    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    if (is_guess_in_word(guess, secret_word)):
        print ('nice ')
    else:
        print ('nope, try again')




    #TODO: show the guessed word so far
    new_get_guessed_word(secret_word, letters_guessed)

    while (is_word_guessed(secret_word, letters_guessed) == False):


    #TODO: check if the game has been won or lost
    if (is_word_guessed(secret_word, letters_guessed)):
        return print ('WOOOOOHOOOOOO!!!!!')
    
    return  False


#These function calls that will start the game

#letters_guessed = ["a", "e", "i", "o", "u", "s", "t", "g", "r"]
#print(secret_word)
#new_get_guessed_word(secret_word, letters_guessed)

secret_word = load_word()
while (spaceman(secret_word) == False):
    spaceman(secret_word)

