#problem to find the sum of all Truncatable Primes
from tools import isprime

def isTruncatable(num):
	if num < 10:
		return False
	while num >= 2:
		if isprime(num) == False:
			return False
		num //= 10
	
	return True

print(isTruncatable(3797))
