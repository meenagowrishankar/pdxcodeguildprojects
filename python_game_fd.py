import random
class character(object):
	def __init__(self, points):
		self.points = points
	def attack(self, character):
		character.points -= 10
	def defend(self):
		self.points += 10

class user(character):
		
	def action(self,monster):
		act = raw_input("attack or defend? a/d?")
		if act == "a":
			self.attack(monster)
		elif act =="d":
			self.defend()
	

class monster(character):
			
	def action(self,user):
		act = random.choice([1,2])
		if act == 1:
			self.attack(user)
		elif act == 2:	
			self.defend()
			

class TheFight(object):
	def __init__(self, user, monster):
		self.user = user
		self.monster = monster
	def fight(self):
		while self.user.points > 0 and self.monster.points > 0:
			self.monster.action(self.user)
			print self.user.points
			self.user.action(self.monster)
			print self.user.points
		if self.user.points <= 0 and self.monster.points > 0:
			print "You lost :(!"
		if self.monster.points<=0 and self.user.points > 0:
			print "You beat the monster! On to the next question!"
				
riddles = {1: ("What is the best among things? A: Knowledge, B:Money", "A"), 2: ("Which is the best among just actions? A: non-violence, B: mercy","A"), 3: ("What is faster than light? A: Nothing, B: Thought", "B")}

# #the riddle
# #what is printed as the question is separate from what's happening in the code.
Player = user(100)
Monster = monster(50)
Battle = TheFight(Player, Monster)

def ask_riddle():
	for k in riddles:
		print (riddles[k][0])
		response = raw_input("answer?")
		if response == riddles[k][1]:
			raw_input("you got the right answer")
		else:
			raw_input("Wonk! Wonk! wrong answer. Time to fight the monster!")
			Battle.fight()

			

ask_riddle()


