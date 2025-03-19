#problem to find the sum of all Double-base Palindromes under 1 million

sum = 0
for i in range(1000000):
	if (str(i)[0:] == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]):
		sum += i

print(sum)
