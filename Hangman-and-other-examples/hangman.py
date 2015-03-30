### GAME OF HANGMAN ###
# wordsEn.txt ile originally sourced from: http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

# Replace your name here.
__author__ = 'Alpita Masurkar'

# Modules to be imported for this code
import sys
import random
import re



# Stores all the possible words from the text file
WORDLIST = []
GUESS_LIST = []
LETTERS_GUESSED = set() # Set is a type of container for data, similar to lists
                        # It does not store repeats
TURNS = 5


# It populates list from the accompanying word file
def populate_word_file(path_to_file):
    """
    Reads the input file and populates the words list from
    the given file
    :param path_to_file:
    :return:
    """
    with open(path_to_file) as inputfile:
        for line in inputfile:
            WORDLIST.append(line.strip()) # Adds every word from the file to this list


# Helper function to get difficulty level and update game data
def get_difficulty_level():
    """
    Select level of difficulty that
    you want to play with for the game
    :return:
    """
    
    length_of_word = 0
    while length_of_word == 0:
        allowed_level = ["easy", "medium", "hard", "quit"]
        level = raw_input ("Enter level of difficulty: Easy/Medium/Hard/Quit : ").lower()
        try :
            if level not in allowed_level :
                raise ValueError
        except ValueError :
            print "Please enter a valid choice"
        if level == "quit" :
            print "Exiting...."
            sys.exit()
        else:
            if level == "easy":
                length_of_word = 3
                TURNS = 3
            elif level == "medium" :
                length_of_word = 5
                TURNS = 5
            else :
                length_of_word = 7
                TURNS = 7
        print "We will play with length of words at: ", length_of_word
    return length_of_word
        



# Helper function that reduces the size of the list from which a random
# word is to be selected for the game
def filter_words(difficulty):
    """

    :param difficulty:
    :return:
    """
    filtered_words = []
        
    for word in WORDLIST :
        if len(word) == difficulty :
            filtered_words.append(word)
    
    return filtered_words


# This function calls filter_words function above.
# Input given to function is output(return) of get_difficulty_level
def word_selector(difficulty):
    """

    :param difficulty:
    :return:
    """
    return random.choice(filter_words(difficulty)) 

# Helper function that keeps a check on the status of the game
def is_game_complete():
    """

    :param:
    :return:
    """
    game_complete = False
            
    if "_" not in GUESS_LIST :
        game_complete = True
        print "You guessed the word. Game complete!"
    elif TURNS == 0 :
        game_complete = True 
        print "No more turns left. Game complete!"
    if game_complete :    
        play_again = raw_input("Play again? Y/N").upper
        if play_again == "Y" :
            main()
        else :
            sys.exit()   

    return game_complete


# The main logic of the game
def play_game(game_word, level):
    """

    :param game_word, level:
    :return:
    """
    global TURNS, GUESS_LIST # global allows us to use updated results of
                             # common variables from within a function.
                             # Useful when constantly updating a variable inside a function

    
    while not is_game_complete():        
        guess = get_and_verify_input()
        if guess in game_word:
            if guess not in LETTERS_GUESSED :
                LETTERS_GUESSED.add(guess)
            else :
                print "You already guessed this letter. Remaining turns: ", TURNS
            occurrences = [m.start() for m in re.finditer(guess, game_word)]
            for i in occurrences:
                GUESS_LIST[i] = guess
            print "Word so far: ", GUESS_LIST
            print " Turns left: ", TURNS
        else :
            if guess not in LETTERS_GUESSED :
                TURNS -= 1
            else:    
                print "Aleady guessed this letter. Try again"
            
            print " Turns left: ", TURNS
            LETTERS_GUESSED.add(guess)
            
            
        
        

def get_and_verify_input():
    """

    :param guess:
    :return:
    """
   
    guess = raw_input("Guess a letter or Press * to exit the game: \n ").lower()
    
    """
    Your code goes here.
    1) If guess is *, print appropriate message and sys.exit() to exit
    2) Check if user input is one character long
    3) If it's not, keep asking above question
    """
    while len(guess) != 1 :
        guess = raw_input("Guess a letter or Press * to exit the game: \n ").lower()
    if guess == "*" :
        print "Done guessing? Will stop the game"
        sys.exit()
    return guess


# Update file path to the Words file
def main():
    global GUESS_LIST
    
    # Add appropriate path to the word file here.
    # wordsEn.txt ile originally sourced from: http://www-01.sil.org/linguistics/wordlists/english/wordlist/wordsEn.txt

    
    path_to_file = "/home/nsoman/SmartyGirls/Hangman-and-other-examples/wordsEn.txt"
    populate_word_file(path_to_file)

    level = get_difficulty_level()

    game_word = word_selector(level)
    # Uncomment the following statement to see hangman game word
    print("The word that was selected is", game_word)

    GUESS_LIST = list(level * "_")
    print((" ").join(GUESS_LIST))

    play_game(game_word, level)

main()

