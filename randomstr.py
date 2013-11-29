import random
start = 97
end = 122
count = 15
def makestr():
	print "".join([chr(random.randint(start,end)) for i in range(count)])
