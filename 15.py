# a problem to sum the digits of the number 2 to the power of 150
from math import pow
digit_sum = 0
result = int(pow(2,1000))
while result:
	#we find the last digit using result % 10 and then devide by 10 o get the next digit
	digit_sum += (result % 10)
	result //= 10
print(digit_sum)