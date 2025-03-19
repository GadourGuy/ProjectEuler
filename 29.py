#problem to find the number of Distinct Powers under 100
from math import pow
from tools import isprime

count = 0
S = set()
for i in range(2,101):
	for j in range(2, 101):
			S.add(i ** j) #sets remove all duplicates
print(len(S))