#problem to find  the sum of the numbers on the diagonals in a 1000 by 1000 spiral formed in the same way?
from math import ceil
#we form the spiral
for i in range (5):
	for j in range (5, 0,-1):
		if i == 5/2 and i == j:
			print(1, end = " ")
		else:
			print(i, end =" ")
	print()