
def hotel_cost(time_period):
	return int(70 * time_period)


def plane_ticket_cost(city, ticket_class):
	base_cost= {
	"New York": 2000,
	"Auckland": 790,
	"Venice":   154,
	"Glasgow":  65}

	class_multiplier = {
	"Economy":          1,
	"Premium Economy":  1.3,
	"Business Class":   1.6,
	"First Class":      1.9}

	return int(base_cost[city] * class_multiplier[ticket_class])

def car_rental_cost(time_period):
	if time_period / 7 >= 1:
		return (30*time_period)-50
	
	elif time_period / 3 >= 1:
		return (30*time_period)-30
	
	else:
		return int(30*time_period)

	
def total_cost(city, ticket_class, time_period):
	return(f"Total Cost = £{hotel_cost(time_period) + plane_ticket_cost(city, ticket_class) + car_rental_cost(time_period)}:\n- Hotel Cost = £{hotel_cost(time_period)}\n- Flight Cost = £{plane_ticket_cost(city, ticket_class)}\n- Car Rental Cost = £{car_rental_cost(time_period)}")



c = input("Please enter the city you'll be visiting:\n\n> ")
t = input("Please enter the ticket class you'll be flying with:\n\n> ")
p = int(input("Please enter the number of days you'll be visiting:\n\n> "))
print(total_cost(c, t, p))
