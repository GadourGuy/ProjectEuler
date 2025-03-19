#problem to find the sum of all numbers which are equal to the sum of the factorial of their digits.
from tools import fact

factorials = {
	"1":fact(1), "2":fact(2), "3":fact(3),
	"4":fact(4), "5": fact(5), "6": fact(6),
	"6": fact(6), "7":fact(7), "8": fact(8),
	"9": fact(9), "0": 1
}
sum = 0
tricky_sum = 0
for i in range (10, fact(9) * 9): #value after 8 digits cannot be tricky number anymore
	for j in str(i):
		tricky_sum += factorials[j]
	if tricky_sum == i:
		sum += i
	tricky_sum = 0
print(sum)