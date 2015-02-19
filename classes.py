# class BaseCharacter(object):
# 	def __init__(self):
# 		self.name = name
# 	def printName(self):
# 		print self.name

# class NonPlayable_Character(BaseCharacter):
# 	pass

# class NPC_Friendly(NonPlayable_Character):
# 	pass
# class NPC_Enemy(NonPlayable_Character):
# 	def __init__(self):
# 		self.attackDamage = 5
		
# class weapon(object):
# 	pass
# class Playable_Character(BaseCharacter):
# 	def __init__(self):
# 		self.weapon = Weapon()
		
# class PC_Archer(Playable_Character):
# 	pass
# class PC_GreenLantern(Playable_Character):
# 	pass
# class PC_Butcher(Playable_Character):
# 	pass

class BaseClass(object):
	x = 5
	def printHam(self):
		print "ham"

class InClass(BaseClass):
	x = 17

a = InClass()
print a.x

class override(BaseClass):
	def printHam(self):
		print "ham2"
b = override()
print b

