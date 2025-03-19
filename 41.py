#problem to find the largest n-digit pandigital prime that exists.
from tools import isprime

for i in range(987654321, 0, -1):
	L = [0,0,0,0,0,0,0,0,0]
	if isprime(i):
		temp = i
		while temp:
			L[(temp % 10) - 1] += 1
			temp // 10
		if sum(L) == 9:
			print(i)
			quit()


