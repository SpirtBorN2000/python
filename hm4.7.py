from itertools import count
from math import factorial

def fact():
    for el in count(1):
        yield factorial(el)

factorialn = fact()
n = 0
for i in factorialn:
    if n < 15:
        print(i)
        n += 1
    else:
        break