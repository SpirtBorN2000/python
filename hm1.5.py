proceeds = float(input("Введите вашу выручку: "))
lesion = float(input("Введите ваши издержки: "))

if proceeds > lesion:
    print(f"Ваша прибыль = {proceeds - lesion} рублей \nВаша рентабельность {proceeds/(proceeds-lesion):.2f}")
    nmembers = int(input("Введите кол-во сотрудников: "))
    print(f"Прибыль на одного сотрудника равна {(proceeds - lesion) / nmembers:.2f}")
elif proceeds == lesion:
    print("Ваша фирма работает в ноль")
else:
    print(f"Ваш убыток = {lesion - proceeds} рублей")

