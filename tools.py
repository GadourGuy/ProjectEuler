#function to check if a number is prime or not
def isprime(n = 1):
	i = 2
	if n == 1:
		return False
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True

# Returns factorial of n
def fact(n):
    if n == 0 or n==1:
        return 1
    res = 1
    
    for i in range(2, n+1):
        res = res * i
        
    return res

#funtion to calculate the value of ncr
def nCr(n, r):

    return (fact(n) / (fact(r) 
                * fact(n - r)))

#function to find sum of divisors
def sum_of_divisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def isPalindromic(n): #function to check if palindromic
    return str(n) == str(n)[::-1]

#function to find number of divisors
def num_of_divisors(n):
    count = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
              
            # If number is square 
            # count only one 
            if (n / i == i) : 
                count = count + 1
            else : # Otherwise count both 
                count = count + 2
                  
    return count