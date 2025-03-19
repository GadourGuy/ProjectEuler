#problem to find the smallest positive integer x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

L1 = [0,0,0,0,0,0,0,0,0]
L2 = L1.copy()

for i in range(1,1000000):
	for j in str(i):
		L1[int(j)] += 1
	for j in str(i * 2):
		L2[int(j)] += 1
	if L1 == L2:
		print(i)
		quit()

	