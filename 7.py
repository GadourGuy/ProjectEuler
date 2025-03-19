#problem to find the 10001 prime.
from tools import isprime as isprime

#we iterate through the real numbers until the prime #10001 occurs
count = 0
i = 1
while True:
	if isprime(i):
		count += 1
	if count == 10001:
		break
	i += 1
print(i)
