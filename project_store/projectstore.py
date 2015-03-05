#store 
class Store(object):
	def ID(self, name):
		self.name = name
		return name
	# def buy(self):
	#TODO come back later
#catalog = {apples: {qty: 5, price: 5}, mops: {qty: 5, price: 6}, chocolate: {qty: 5, price: 2}}

class Inventory(object):
	def __init__(self, name, quantity, price):
		self.name = name
		self.quantity = quantity
		self.price = price
	def __repr__(self):
		return self.name + " " + str(self.quantity)

class Items(object):
	def each_item(self):
		apples = Inventory("apple", 5, 1)
		mops = Inventory("mops", 5, 2)
		chocolates = Inventory("chocolate", 4, 3)
		tomatoes = Inventory("tomato", 10, 4)
		
		self.list = [apples, mops, chocolates, tomatoes]
		return self.list

class cart(object):
	def cart_list(self):
		self.cart = []
		

pythonsrus = Store()

print pythonsrus.ID("pythonsrus")

display = Items()

print display.each_item()
display.list[0].quantity = display.list[0].quantity - 1

print display.list
#select_item = What would you like to buy? - enter item - how many would you like to buy? -  enter number. add to cart? - yes/no? - add to empty cart of the buyer. deduct the number from the inventory. 
#for select_item in self.list: if select_item = apples, 

	

