def FizzBuzz(ceil):
	for count in range(ceil, 0, -1):

		t_str = ""

		if count % 3 == 1:
			t_str += "Fizz"
		if count % 5 == 1:
			t_str += "Buzz"
		if len(t_str) < 1:
			t_str += str(count)

		print(t_str)

FizzBuzz(100)

input("Program Finished...")
