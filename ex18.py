import random

#5 card draw rules
#ante price decided
#all who wish to play pay ante to pot
#first hand dealt - 5 cards
#call, raise, fold
#substitutions made (up to three, or up to four if they hold an ace)
#call, raise, fold
#compare hands
#pot distributed


class Card():
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def get_as_text(self):
		#creates a string interpretation of the card's value and returns it
		text = ""

		if self.value != 0 and self.value <=9:
			text += str(self.value+1)
		elif self.value == 0:
			text += "A"
		elif self.value == 10:
			text += "J"
		elif self.value == 11:
			text += "Q"
		elif self.value == 12:
			text += "K"

		if self.suit == 0:
			text += "♥"
		if self.suit == 1:
			text += "♢"
		if self.suit == 2:
			text += "♣"
		if self.suit == 3:
			text += "♤"

		return text


class Pile():
	def __init__(self):
		self.cards = []


class Deck():
	def __init__(self):
		# Creates each suit and populates it with 13 cards (0-12), storing all in self.cards
		self.cards = [Card(k, i) for k in range (4) for i in range(13)]

	def Shuffle(self):
		# Shuffling the deck once is faster than randomly selecting a card each time.
		random.shuffle(self.cards)

	def Draw(self, quantity):
		# Pops a quantity of cards from the top of the deck and returns them as a list
		if quantity <= len(self.cards):
			hand = []
			for i in range(quantity):
				hand += [self.cards.pop()]
			return hand

	def Return(self, cards):
		# Adds cards back into the deck
		for c in cards:
			self.cards.append(c)


class Hand():
	def __init__(self):
		self.cards = []

	def Sort(self):
		#Public access sort function
		self.cards = self._sort(self.cards)

	def _sort(self, l):
		#Private access sort function
		#Recursive quicksort algorithm

		lv = [] #low value
		ev = [] #equal value
		hv = [] #high value

		if len(l) > 1:
			piv = l[0].value #sets pivot to first position
			for i in l:
				if i.value  < piv:
					lv.append(i)
				elif i.value  == piv:
					ev.append(i)
				elif i.value  > piv:
					hv.append(i)
			return self._sort(lv) + ev + self._sort(hv)

		else:
			return l


D = Deck()
H = Hand()
P = Pile() # Discard Pile

hand_size = 5

print("Press enter to draw a hand.")
while True:

	if len(D.cards) < hand_size:
		D.cards += P.cards
		P.cards = []
		D.Shuffle()

	H.cards = D.Draw(hand_size)
	H.Sort()
	for i in H.cards:
		print(i.get_as_text(), end='\t')

	print(f"\nDeck contains {len(D.cards)} cards.")
	print(f"Discard Pile contains {len(P.cards)} cards.")

	input()
	P.cards += H.cards
