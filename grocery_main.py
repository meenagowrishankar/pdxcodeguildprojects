# Here is our initial list of items for our store. This will eventually live in another file once we
# have set up a few more of the basic items.
#<<<<<<< HEAD
items = {apples: {price: 1, qyt: 5}, kashi: {price: 2, qty:15}, mops: {price: 5, qty: 20}}
# =======

class Store(object):

# catalog of items in the inventory
	def items(self):
		self.items = {apples: {price: 1, qty: 5}, kashi: {price: 2, qty:15}, mops: {price: 5, qty: 20}}

# >>>>>>> FETCH_HEAD
# This will create a basic profile for users. Later in the program buyers/sellers will be distinguished


class Profile(object):
  def __init__(self, first_name, last_name, money, password):
    self.first_name = first_name
    self.last_name = last_name
    self.money = money
    self.password = password

# <<<<<<< HEAD
  def __str__(self):
    return 'Customer: {0} {1}, Money: ${2}, Password: {3}'.format(self.first_name, self.last_name, self.money, self.password)

# <<<<<<< HEAD


class Buyer(Profile):
    pass
# this will take items selected by buyer from the store items dictionary.

    def cart(self):
      self.inventory = {}


#class to separate the user interface (what is displayed to the user) and the logic of the program.
class User_Interface(Store):
    pass

  def options(self):
      self.display = raw_input("what would you like to do")
      self.options = raw_input("search, view cart, review and payment")

# >>>>>>> FETCH_HEAD
    