#problem to find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
from math import pow
#function to check if the number is the sum of it's digits
def issumofpowers(n):
	sum = 0
	save = n
	while n:
		sum += pow(n % 10, 5)
		n //= 10
	if (sum == save):
		return True
	return False
sum = 0
#numbers cannot exceed 100000 that's why we loop and check
for i in range(2, 1000000):
	if (issumofpowers(i)):
		sum += i #we add the sum only if the number is equal to the sum of the power of it's digits
print(sum)