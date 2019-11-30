# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"

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
	for c in secret_word:
		if not c in letters_guessed:
			return False
	return True



def get_guessed_word(secret_word, letters_guessed):
	'''
	secret_word: string, the word the user is guessing
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string, comprised of letters, underscores (_), and spaces that represents
	  which letters in secret_word have been guessed so far.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	redacted_word = ""
	for c in secret_word:
		if c in letters_guessed:
			redacted_word += c
		else:
			redacted_word += '_'
		redacted_word += ' '
	return redacted_word



def get_available_letters(letters_guessed):
	'''
	letters_guessed: list (of letters), which letters have been guessed so far
	returns: string (of letters), comprised of letters that represents which letters have not
	  yet been guessed.
	'''
	# FILL IN YOUR CODE HERE AND DELETE "pass"
	all_letters = []
	for c in string.ascii_lowercase:
		all_letters.append(c)
	
	for c in letters_guessed:
		if c in all_letters:
			del(all_letters[all_letters.index(c)])
			
	return all_letters



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
	
	guesses_remaining = 6
	warnings_remaining = 3
	letters_guessed = []
	win = False
	while guesses_remaining >= 1:
		available_letters = get_available_letters(letters_guessed)
		
		print('='*80+f"\nYou have {guesses_remaining} guesses left.")
		
		if warnings_remaining >= 1:
			print(f"You have {warnings_remaining} warnings left.")
			
		print("Letters not selected:\n" + ", ".join(available_letters)[0:len(available_letters)*3-2])
		
		letters_guessed.append(str(input('-'* 80 + "Please guess a letter:\n> ")))
		

		if not letters_guessed[len(letters_guessed)-1] in string.ascii_lowercase: #checks if the most recent input is not an ascii letter.
			if warnings_remaining <= 0:
				guesses_remaining -= 1
			else:
				warnings_remaining -= 1
			print("Please enter only single english alphabetical letters.")

		 #checks if the most recent input is a repeat input.
		elif len(letters_guessed) > 1 and letters_guessed[len(letters_guessed)-1] in letters_guessed[0:len(letters_guessed)-1]:
			if warnings_remaining <= 0:
				guesses_remaining -= 1
			else:
				warnings_remaining -= 1
			print("Please enter one of the remaining letters.")
			
		else:
			if not letters_guessed[len(letters_guessed)-1] in secret_word: #checks that the most recent guessed letter isn't part of the secret word.
				if letters_guessed[len(letters_guessed)-1] in "aeiou":
					guesses_remaining -= 2
				else:
					guesses_remaining -= 1
				print("Guess incorrect. ", end='')
			else:
				print("Guess correct. ", end='')
				
		print(f"{get_guessed_word(secret_word, letters_guessed)}")
		
		if is_word_guessed(secret_word, letters_guessed):
			unique = []
			for char in secret_word:
				if char not in unique:
					unique.append(char)
			print(f"You win! The hidden word was {secret_word}.")
			print("Your total score for this game is:" + str(guesses_remaining + len(unique)))
			win = True




			break
	if not win:
		print(f"You lose. The hidden word was {secret_word}")

secret_word = choose_word(wordlist)
hangman(secret_word)
