#problem to find sum of the most consecutive primes under 1 million
from tools import isprime

# Generate a list of all primes less than 1000000
primes = []
for i in range(2, 1000000):
    if isprime(i):
        primes.append(i)

# Variable to store the maximum number of consecutive primes
max_length = 0
result = 0

# Loop through the list of primes to find the longest sum of consecutive primes
for i in range(len(primes)):
    sum_primes = 0
    for j in range(i, len(primes)):
        sum_primes += primes[j]
        if sum_primes >= 1000000:
            break
        # Check if the current sum is prime and if the sequence is longer than the previous one
        if isprime(sum_primes):
            current_length = j - i + 1
            if current_length > max_length:
                max_length = current_length
                result = sum_primes

print(result)

			
			
