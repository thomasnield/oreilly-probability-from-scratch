import random

heads = 0

for i in range(0,100):
	if random.uniform(0,1) <= .6:
		heads += 1 

print("# HEADS: {}/100".format(heads))
