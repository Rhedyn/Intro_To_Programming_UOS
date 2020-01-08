total_cost = int(input("Please enter the cost of your dream house\n> ")) # total cost of house)
annual_salary = int(input("Please enter your total annual salary\n> ")) # your annual salary
salary_savings = int(input("Please enter the percentage of your salary to save\n> ")) # % of salary saved each year
semi_annual_raise = int(input("Please enter the percentage of a raise to be added to your salary\n> ")) # % of salary saved each year

def deposit_calculator(total_cost, annual_salary, salary_savings, semi_annual_raise):
	deposit_cost = int(total_cost/5) # the portion of total_cost that is a deposit (20% by default)
	current_savings = 0 # your current savings (bank balance)
	month = 0
	investment_return = 0.04 # 4% return over the year

	while current_savings < deposit_cost:
		month+=1
		current_savings = (current_savings + (investment_return/12)) + (annual_salary / 12)
		if month % 6 == 1:
			annual_salary += annual_salary * (1 + semi_annual_raise / 100)

	print(f"Number of Months: {month}")

deposit_calculator(total_cost, annual_salary, salary_savings, semi_annual_raise)

input("Program Finished...")
