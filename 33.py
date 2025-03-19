#problem to find the value of the denominator in the product of the four digit cancelling fractions

count = 0
multnum = 1
multdom = 1
for num in range(10, 100):
	for dom in range(10,100):
		# we compare each digit of the denominator against each digit of the numerater
		if (num % 10 == dom % 10 and num % 10 != 0 and dom % 10 != 0):
			if (num %100) // 10 / (dom %100) // 10 == (num / dom):
				#if the condition is valid we append the multiplaction of the num/dom
				multnum *= num
				multdom *= dom
		elif (num % 10 == ((dom %100) // 10) and dom % 10 != 0):
			if ((num %100) // 10) / (dom %10)== (num / dom):
				multnum *= num
				multdom *= dom
print(multnum)	
print(multdom)
