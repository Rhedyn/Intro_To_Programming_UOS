class Fraction():
	def __init__(self, num, denom):
		try:
			self.num = int(num)
		except ValueError:
			raise ValueError("Provided numerator is invalid (Is it of type int?)")
		try:
			self.denom = int(denom)
		except ValueError:
			raise ValueError("Provided denominator is invalid (Is it of type int?)")

	def get_as_string(self):
		return f"{self.num}/{self.denom}"

	def get_as_float(self):
		return self.num / self.denom

	def Add(self, other):
		return Fraction(self.num*other.denom + self.denom*other.num, self.denom*other.denom)

	def Sub(self, other):
		return Fraction(self.num*other.denom - self.denom*other.num, self.denom*other.denom)

	def Mul(self, other):
		return Fraction(self.num*other.num, self.denom*other.denom)

	def Div(self, other):
		return Fraction(self.num*other.denom, self.denom*other.num)

	def Inv(self):
		return Fraction(self.denom, self.num)

f = Fraction(2, 5)

g = Fraction(2, 5)

print(f.Add(g).get_as_string())

input("Program Finished...")
