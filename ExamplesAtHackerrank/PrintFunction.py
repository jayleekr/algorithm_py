# Read an integer .
# Without using any string methods, try to print the following:
# 1~N
# Note that "" represents the values in between.

# n = int(input())
n = 11
total = list(range(1, n + 1))

import math

sumOfValues = total[0]
for value in total[1:]:
    figure = int(math.log10(value)) + 1
    sumOfValues = value + sumOfValues * (10 ** figure)
print(sumOfValues)
