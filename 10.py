#problem to find sum of primes under 2 million
from tools import isprime
#we check if the number is prime and add it to the sum
sum = 0
for i in range(2000000):
	if (isprime(i)):
		sum += i
print(sum)