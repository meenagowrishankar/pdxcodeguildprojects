"""
The game - Motivation - there's a treasure at the end. Challenge - There are 3 questions to answer. two answer options are presented with each question. The correct answer leads you to the next question and the wrong answer leads to fight a monster. If you win the fight, you get to the next question. If you lose the fight, you die and the game ends. The same repeats after each question. 
"""
import random
class character(object):
	#assigns the points attributes to each character - monster or user. The points are provided when the subclass is instantiated.
	def __init__(self, points, name):
		self.points = points
		self.name = name
	#defines how the points are deducted based on attack or defense by the character. 
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
		#TODO either refresh points for the user or start with higher points and present a different monster each time. 
	

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
			print "You are dead and therefore, lost the game:( No treasure for you!"
			exit()
		elif self.monster.points<=0 and self.user.points > 0:
			print "You beat the monster! On to the next question!"
			self.user.points = 100
			self.monster.points = 50
#reset points of existing monster or provide a different monster for each wrong answer. 				
riddles = {1: ("What is the best among things? A: Knowledge, B:Money", "A"), 2: ("Which is the best among just actions? A: non-violence, B: mercy","A"), 3: ("What is faster than light? A: Nothing, B: Thought", "B")}

# #the riddle
# #what is printed as the question is separate from what's happening in the code.

Player = user(100, "Player")
Monster1 = monster(50, "themummy")
Monster2 = monster(80, "dragon")
Monster3 = monster(65, "elf")
Monster = (Monster1, Monster2, Monster3)
choose_monster = random.choice(Monster)
Battle = TheFight(Player, choose_monster)

def ask_riddle():
	for k in riddles:
		print (riddles[k][0])
		response = raw_input("answer?")
		if response == riddles[k][1]:
			raw_input("you got the right answer")
		else:
			raw_input("Wonk! Wonk! wrong answer. Time to fight the" + " " + choose_monster.name + "!")
			Battle.fight()

			
print '''Now Yudhishthira was clearly worried. Wondering about the possibilities of harm befalling his dear and powerful brothers, he decided to go in search of them. When he arrived at the lake, he could not believe the dreadful sight before him. All four brothers dead on the ground! Yudhishthira sat beside them and lamented. All his hopes were shattered now. How would he ever be able to recover his lost kingdom without the help of his able, powerful brothers? He grieved for a while and then began to look around to determine the reason for these deaths. He said to himself,
There are no signs of violence on their bodies, no foot-prints anywhere. The
killer must be a supernatural being.

'''
ask_riddle()


