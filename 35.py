#problem to find circular primes below one million
from  math import pow
from tools import isprime
def isCircular(N):
    digits = str(N)
    for i in range(len(digits)):
        #we rotate through every possible combination using slicing
        rotated = int(digits[i:] + digits[:i])
        if not isprime(rotated):
            return False
    return True

count = 0

for i in range(2,1000000):
	if isCircular(i):
		count += 1

print(count)
