#problem to find the sum of all the amicable numbers under 10000
from tools import sum_of_divisors
def isAmicable(num1): # to check if number is amicable
    num2 = sum_of_divisors(num1)
    if num1 != num2 and sum_of_divisors(num2) == num1:
        return True
    return False

sum = 0

for i in range(1, 10000):
	if isAmicable(i):
		sum += i
print(sum)

