sum = 0
i = 0
j = 0
count_side = 0
count_up = 0
while i <= 2:
	while j <= 2:
		if i == 0 and j == 0:
			continue
		if count_side <= i and count_up >= j:
			sum += 1
		j += 1
	i += 1
print(sum)
