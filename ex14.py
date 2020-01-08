def Recursive_Fib(n):
	if n <= 1:
		return n
	else:
		return(Recursive_Fib(n-1)+Recursive_Fib(n-2))

for i in range(0, 20):
	print(Recursive_Fib(i))

input("Program Finished...")
