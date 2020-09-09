from itertools import count
from itertools import cycle

n = 0

try:
    maxtry = int(input("Введите желаемое колличество повторений: "))
    for el in count(int(input("Введите стартовое число: "))):
        if n <= maxtry:
            n += 1
            print(el)
        else:
            break
except ValueError:
    print("Вы ввели не число")
my_list = ['BCA', 'ABC', 'CBA', 'ACB']
n = 0
for el in cycle(my_list):
    if n <= maxtry:
        n += 1
        print(el)
    else:
        break
