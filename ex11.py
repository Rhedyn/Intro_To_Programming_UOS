import random
def GuessGame(floor, ceil):
	c_guess = random.randint(floor, ceil)
	g_count = 0
	is_correct = False
	while not is_correct:
		g_count += 1
		p_guess = int(input(f" Please select a number between {floor} and {ceil}\n\n> "))
		if p_guess == c_guess:
			is_correct = True
		else:
			print(f"Guess {g_count} incorrect...")
	print(f"Guess correct! Took {g_count} guesses.")

GuessGame(1, 5)

input("Program Finished...")
