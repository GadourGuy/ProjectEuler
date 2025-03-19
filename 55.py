#problem to find the number of lychrel numbers under 10000
def isPalindromic(n): #function to check if palindromic
    return str(n) == str(n)[::-1]

def isLychrel(n):
    for _ in range(50):  # We use 50 iterations as stated
        n = n + int(str(n)[::-1])
        if isPalindromic(n):
            return False  # Not a Lychrel number if a palindrome is found
    return True  # If no palindrome is found in 50 iterations, it's a Lychrel number

count = 0
for i in range(1, 10000):
    if isLychrel(i):
        count += 1

print(count)
