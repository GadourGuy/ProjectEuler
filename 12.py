#problem to find the first triangle number to have over five hundred divisors
from tools import isprime
from math import sqrt
import math


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

n = 0
i = 1
while (num_of_divisors(n) < 500):
    n += i
    i += 1

print(n)

