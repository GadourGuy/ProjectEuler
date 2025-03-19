#problem to find number of triangular numbers in text file
import re

weights = {
	       "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
		   "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23, "X": 24, "Y": 25, "Z": 26
		   }

# Returns True if num is triangular. else False
def isTriangular(num):

    if (num < 0):
        return False
    sum = 0
    n = 1
	#itirate until the sum of numbers is more than the number to be checked
    while(sum <= num): 
    
        sum = sum + n
        if (sum == num):
            return True
        n += 1

    return False

sum = 0
count = 0
with open("0042_words.txt", "r") as file:
	file_content = file.read()
	#Remove punctuation and create a list of names
	names_list = sorted(re.findall(r'\b\w+\b', file_content))
	for i in range(len(names_list)):
		for j in range(len(names_list[i])):
			sum += weights[names_list[i][j]]
		if (isTriangular(sum)):
			count += 1
		sum = 0

print(count)
                                