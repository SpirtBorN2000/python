from sys import argv

name, time, sal, premium = argv
try:
    result = (int(time) * int(sal)) + int(premium)
    print(result)
except ValueError:
    print("Не число")
