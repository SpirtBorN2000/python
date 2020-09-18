def my_func(n_1, n_2, n_3):
    try:
        if int(n_1) > int(n_3) and int(n_2) > int(n_3):
            return int(n_1) + int(n_2)
        elif int(n_1) > int(n_2) and int(n_3) > int(n_2):
            return int(n_1) + int(n_3)
        elif int(n_2) > int(n_1) and int(n_3) > int(n_1):
            return int(n_2) + int(n_3)
        elif int(n_1) == int(n_2) and int(n_1) == int(n_3) and int(n_2) == int(n_3):
            return int(n_2)+int(n_2)

    except ValueError:
        return print("Вы ввели не число")


n_1 = input("Введите первое число ")
n_2 = input("Введите второе число ")
n_3 = input("Введите третье число ")
print(my_func(n_1, n_2, n_3))
