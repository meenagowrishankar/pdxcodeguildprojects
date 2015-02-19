import random
#motivation - get to the hidden treasure
#have points for the users and monsters.


#random monsters

class user(object):
	def __init__(self):
		self.points = 100
		return self.points
	def weapons(self, name, points):
		self.name = name
		self.points = points 

weapons_1 = user.weapons('scythe', 10)
weapons_2 = user.weapons('knife', 15)
weapons_3 = user.weapons('sword', 20)
weapons_c = random.choice([weapons_1.points, weapons_2.points, weapons_3.points])


#monsters and weapons assigned

class Monsters(object):

	def __init__(self, name, points):
		self.points = points
		self.name = name

	
a = Monsters('themummy', 100)
b = Monsters('dragon', 150)
c = Monsters('zombies', 75)
monsters_c = random.choice([a.points, b.points, c.points])
print monsters_c

	# def themummy(self):
	# 	self.points = 100
	# 	return self.points

	# def dragon(self):
	# 	self.points = 150
	# 	return self.points

	# def zombies(self):
	# 	self.points = 75
	# 	return self.points


#random weapons 

# class Weapons(object):
# 	def scythe(self):
# 		self.points = 10
# 		return self.points
# 	def sword(self): 
# 		self.points = 20
# 		return self.points
# 	def knife(self): 
# 		self.points = 15
# 		return self.points
# #first instance of Monsters class

# the_monster_mash = Monsters()
# #instances of Monsters class to separate the monsters based on points. 

# monster_1 = the_monster_mash.themummy()
# monster_2 = the_monster_mash.dragon()
# monster_3 = the_monster_mash.zombies()

# the_weapons_mash = Weapons()
# weapons_1 = the_weapons_mash.scythe()
# weapons_2 = the_weapons_mash.sword()
# weapons_3 = the_weapons_mash.knife()

# # list to pick a monster and weapon
# pick_a_monster = [monster_1, monster_2, monster_3]
# pick_a_weapon = [weapons_1, weapons_2, weapons_3]


# #function to fight monsters and weapons
# ##fight - user chooses attack vs defend - for user attack - monster loses points, monster attack - user loses points.  for every defense the monster gets points. Once monster points below 0, user wins, if user points less than 0, user loses. 
# #for points to change - attack_defend needs to access points of user, choose_monster and choose_weapon. the modified user points need to be accessed by monster_response. 
# class UserAttack(object):
# 	def __init__(self, monsters, weapons):
# 		self.monsters = pick_a_monster
# 		self.weapons = pick_a_weapon
# 		self.user = user
# 	def attack(self, monster):
# 		action = raw_input("attack or defend?")
# 		if action == "attack"
# 			self.monsters -= self.weapons
# 		return self.monsters

# class MonsterAttack(object):
# 	def __init__(self, monsters, weapons, user):
# 		self.monsters = pick_a_monster
# 		self.weapons = pick_a_weapon
# 		self.user = user
# 	def attack(self, user):
# 		self.user -= self.weapons
# 		return self.user

# class TheFight(object):

# 	def __init__(self, monsters, weapons, user):
# 		self.monsters = pick_a_monster
# 		self.weapons = pick_a_weapon
# 		self.user = user
# 		while self.monster > 0 and self.user > 0:
# 			if action ==  

# 		#randomizing the attack/defense choice of the monster using 1 and 2 as representatives of attack and defense. 
# 	def user_attack(self):
		
# 		# choose_weapon = random.choice(pick_a_weapon)
# 		attack_defend = raw_input("attack or defend? a/d")
# 		print attack_defend
# 		if self.choose_monster > 0 and attack_defend == "a":
# 			self.choose_monster -= self.choose_weapon
# 		elif self.choose_monster > 0 and self.attack_defend == "d":
# 			self.user += self.choose_weapon
# 		elif self.choose_monster <= 0 and self.user > 0:
# 			print "you win! Next question!"
		
# 		return user
# 	def monster_response(self):
# 		a = random.choice([1, 2])
		
# 		if user > 0 and a == 1:
# 			user -= choose_weapon
# 			attack_defend()
# 		elif user > 0 and a == 2:
# 			user += choose_weapon
# 			attack_defend()
# 		elif user <= 0:
# 			print "you lose!"
# 		return user

# the_fight = TheFight()




# riddles = {1: ("What is the best among things?", "A: knowledge, B:Money", "A"), 2: ("Which is the best among just actions?", "A: non-violence, B: forgiveness","A"), 3: ("What is faster than light?", "A: Nothing, B: Thought", "B")}

# #the riddle
# #what is printed as the question is separate from what's happening in the code.
# def ask_riddle():
# 	for k in riddles:
# 		print (riddles[k][0])
# 		response = raw_input("answer?")
# 		if response == riddles[k][2]:
# 			raw_input("you got the right answer")
# 		else:
# 			raw_input("Wonk! Wonk! wrong answer. Time to fight the monster!")

# 			the_fight.attack_defend()
# 			the_fight.monster_response()



# ask_riddle()

