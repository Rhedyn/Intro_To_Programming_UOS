class Car():
	def __init__(self, color, manufacturer, model, number_of_doors, mileage, tank_size, tank_fill, miles_per_litre):
		self.color = color
		self.manufacturer = manufacturer
		self.model = model
		self.number_of_doors = number_of_doors
		self.mileage = mileage
		self.tank_size = tank_size
		self.tank_fill = tank_fill
		self.miles_per_litre = miles_per_litre

	def get_description(self):
		return f"The car is a {self.color} {self.manufacturer} {self.model} with {self.number_of_doors} doors. It has travelled {self.mileage} miles. It has a {self.tank_size}L tank, which has {self.tank_fill}L of fuel."

	def paint(self, color):
		self.color = color

	def drive(self, miles):
		if miles/self.miles_per_litre < self.tank_fill:
			self.mileage += miles
			self.decrease_fuel(miles/self.miles_per_litre)
		else:
			self.mileage += self.miles_per_litre*self.tank_fill
			self.decrease_fuel(self.tank_fill)

	def decrease_fuel(self, litres):
		self.tank_fill -= litres

	def refuel(self, spent_money, ppl):
		bought_fuel = spent_money/ppl
		if self.tank_fill + bought_fuel <= self.tank_size:
			self.tank_fill += bought_fuel
			return 0
		else:
			change = self.tank_size - self.tank_fill * ppl
			self.tank_fill = self.tank_size
			return change

c1 = Car("green", "ford", "escort", 4, 8500, 55, 30, 5.7)
c2 = Car("blue", "toyota", "picnic", 4, 12000, 60, 60, 5)

print(c1.get_description())
print(c2.get_description())

c1.paint("pink")
c2.drive(250)
print("Attempted to purchase £40 worth of fuel.\nChange given = £", end='')
print(c1.refuel(40, 1.25))

print(c1.get_description())
print(c2.get_description())

input("Program Finished...")
