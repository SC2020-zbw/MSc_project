from math import *
k = 0
sum = 0
a = int(input("Type the number of precision: "))


while k < a:
    sum = ((factorial(4 * k) * (1103 + 26390 * k)) / (pow(factorial(k), 4) * pow(396, 4 * k))) + sum
    k = k + 1
    
pi = (9801) / (2 * sqrt(2) * sum)
print('{:.100}'.format(pi))