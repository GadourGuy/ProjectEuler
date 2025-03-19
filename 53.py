#problem to find distinct, values of nCr which exceeds 1 million
from tools import nCr

count = 0
for n in range(1,101):
	for r in range(1,101):
		if nCr(n,r) > 1000000:
			count += 1
print(count)