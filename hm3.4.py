def my_func(x, y):
    return 1 / x ** abs(y)


print(my_func(5, -2))


def recurse(x, y):
    try:
        e = 0
        res = int(x)
        while e < abs((int(y))) - 1:
            res = res * int(x)
            e += 1
            return 1 / res
    except ValueError:
        return print("X должен быть числом")
    except TypeError:
        return print("Y должен быть отрицательным числом")


x = input("Введите число ")
y = input("Введите степень ")
if int(y)<0:
    print(recurse(x, y))
else:
    print(int(x)**int(y))

