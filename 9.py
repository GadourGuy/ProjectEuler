#problem to find abc result where a+b+c = 1000 and a,b,c are pythagorean triplet
from math import sqrt, pow

for a in range(1000):
	for b in range(1000):
		#we find C using Pythagorean theory
		c = sqrt(pow(a,2) + pow(b,2))
		if (a + b + c) == 1000:
			result = a * b * c
			print(result)