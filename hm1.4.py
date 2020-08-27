number = int(input("Введите число: "))
maxnum=0
while number > 1:
    ordinaln = number % 10
    number //= 10
    if ordinaln > maxnum:
         maxnum = ordinaln
print(maxnum)