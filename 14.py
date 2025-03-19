#problem to find the number that produces the longest Collatz Sequence chain

def collatzSequence(N):
	count = 0
	while N != 1:
		if N % 2 == 0:
			N //= 2
		else:
			N = 3 * N + 1
		count += 1
	return count + 1

Biggest = 0
Biggest_number = 0
for i in range(100000):
	current_length = collatzSequence(i)
	if current_length > Biggest:
		Biggest = current_length
		Biggest_number = i

print(Biggest_number)