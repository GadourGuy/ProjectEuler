#problem to find the sum of the digits in the number 100!
from tools import fact
sum = 0
result = fact(100)
while result:
	sum += result % 10
	result //= 10
print(sum)