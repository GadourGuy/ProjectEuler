#problem to find maximum digital sum
from math import pow


number = pow(99,99)
sum = 0
while number:
	sum += number % 10
	number //= 10
print(sum)