n = int(input("Введите месяц в виде целого числа от 1 до 12: "))
listm = ["Осень", "Лето", "Зима", "Весна"]
dictm = {1:"Осень", 2:"Лето", 3:"Зима", 4:"Весна"}
if n==12 or n==1 or n==2:
    print(listm[2])
    print(dictm.get(3))
elif 3<=n<=5:
    print(listm[3])
    print(dictm.get(4))
elif 6<=n<=8:
    print(listm[1])
    print(dictm.get(2))
elif 9<=n<=11:
    print(listm[0])
    print(dictm.get(1))
elif n<1 or n>12:
    print("Неверное значение")


