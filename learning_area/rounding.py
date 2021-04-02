#Copied from https://realpython.com/python-rounding/
########

'''
Round the number n to p decimal places by first shifting the decimal point
 in n by p places by multiplying n by 10ᵖ (10 raised to the pth power) to get a new number m.

Then look at the digit d in the first decimal place of m.
 If d is less than 5, round m down to the nearest integer. Otherwise, round m up.

Finally, shift the decimal point back p places by dividing m by 10ᵖ.
'''

def truncate(n):
    return int(n * 1000) / 1000

import random
random.seed(100)
actual_value, rounded_value = 100, 100

for _ in range(1000000):
    randn = random.uniform(-0.05, 0.05)
    actual_value = actual_value + randn
    rounded_value = round(rounded_value + randn, 3)


print(actual_value)


print(rounded_value)
#########