# yo mikey!!!!
# Here is our initial list of items for our store. This will eventually live in another file once we
# have set up a few more of the basic items.
class store(object):

	#catalog of items in the inventory
	def items(self):
		self.items = {apples: {price: 1, qty: 5}, kashi: {price: 2, qty:15}, mops: {price: 5, qty: 20}}




# This will create a basic profile for users. Later in the program buyers/sellers will be distinguished
class Profile(object):
  def __init__(self, first_name, last_name, money, password):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
    self.password = password

class Buyer(Profile):
	def Cart(self):
		#this will take items selected by buyer from the store items dictionary.
		self.inventory = {}
#class to separate the user interface (what is displayed to the user) and the logic of the program.

class User_Interface(store):

	def options(self):
		self.display = raw_input("what would you like to do")
		self.options = raw_input("search, view cart, review and payment")

    
 # we are gonna rock!