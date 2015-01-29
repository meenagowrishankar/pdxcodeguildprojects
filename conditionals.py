a = 1
if a == 1:
	print "a is 1."

if a == 1:
	print "a is 2."

else:
	print "a is not 1 or 2."

proceed = raw_input ("You have reached a fork! which way do you want to proceed?: ")

if proceed == "right":
	print "oops! this is going to be challenging."
elif proceed == "left":
	print "I suppose you want to go the easy way.."
else:
	print "chicken!"
