def get_available_letters(L1, L2):
	for e in L2:
		if e in L1:
			L1.remove(e)

L1 = [1, 2, 3, 4]
L2 = [1, 2, 5, 6]
get_available_letters(L1, L2)
print(L1, L2)

input("Program Finished...")
