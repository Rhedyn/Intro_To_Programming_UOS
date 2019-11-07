annual_salary = int(input("Please enter your annual salary\n> "))

def amount_to_save(annual_salary):
    epsilon = 100
    semi_annual_raise = 0.07
    investment_return = 0.04
    down_payment = 0.25
    house_cost = 1000000 # £
    current_savings = 0

    #search
    epsilon = 100 # £ leeway for search
    num_guesses = 0
    low = 0
    high = house_cost / 36
    guess = int( ( ( high*100 ) + ( low*100 ) )/2 )/100
    
    print(f"{num_guesses}, {high} > {guess} > {low}, {current_savings}")
    
    while abs(guess) >= epsilon+(house_cost/36):
        current_savings += (current_savings * investment_return / 12 ) + ( annual_salary / 12 )
        
        if num_guesses >= 36:
            return("Took longer than 36 months")
        
        if guess*36 < house_cost:
            low = guess
            
        else:
            high = guess
            
        guess = int( ( ( high*100 ) + ( low*100 ) )/2 )/100
        num_guesses += 1
        print(f"{num_guesses}, {high} > {guess} > {low}, {current_savings}")
    return(f'Number of guesses = {num_guesses}\n{guess} is close to the best rate of savings')

print (amount_to_save(annual_salary))
