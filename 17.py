#problem to find how many letters would be used If all the numbers from 1 to 1000 were written out in words

# Define the values for each digit
digit1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine"}

digit2 = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
         14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen",
         18: "eighteen", 19: "nineteen"}

digit3 = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}

#function to return number of letters in a word
def number_to_words(n):
    if 1 <= n < 10:
        return digit1[n]
    elif 10 <= n < 20:
        return digit2[n]
    elif 20 <= n < 100:
        return digit3[n // 10 * 10] + (digit1[n % 10] if n % 10 != 0 else "")
    elif 100 <= n < 1000:
        return digit1[n // 100] + "hundred" + ("and" + number_to_words(n % 100) if n % 100 != 0 else "")
    elif n == 1000:
        return "onethousand"
    return ""

# Calculate the total letter count
total_letters = 0
for i in range(1, 1001):
    word = number_to_words(i)
    total_letters += len(word)

print(total_letters)
