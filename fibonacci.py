# #fibonacci sequence
# # i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

k = [0, 1, 1]

# a = k[0] + k[1]

# k.append(a)

# b = k[1] + k[3-1]

# k.append(b)

# c = k[2] + k[4-1]

# k.append(c)

# print k

# d = k[2+1] + k[2+2]

# k.append(d)

# print k

# e = k[3+1] + k[3+2]

# k.append(e)

# print k
for i in range(len(k)):
	f = k[i+1] + k[i+2]
	k.append(f)
	i+=1
	print k