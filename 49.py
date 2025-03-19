#problem to find 3  Prime Permutations in sequence
from itertools import permutations
from tools import isprime

#count = 0
#for i in range(1000, 9999):
#	number1 = str(i)
#	for j in range(len(number1)):
#	#we rotate through every possible combination using slicing
#		rotated = int(number1[j:] + number1[:j])
#		if  isprime(rotated) and isprime(int(number1)):
#			count += 1
#		if count >= 3:
#			print(rotated)
#		count = 0

print(list(permutations("1000")))