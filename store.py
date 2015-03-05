#store app. Items sold. Buyers. 
items = {apples: {price: 1, qty: 5}, kashi: {price: 2, qty: 15}, mops: {price: 5, qty: 20}}

class Profile(object):
	def __init__(self, first_name, last_name, money, password):
		self.FirstName = first_name
		self.LastName = last_name
		self.money = money
		self.password = password

class Buyer(Profile):
	def cart(self):
		self.cart = {}


