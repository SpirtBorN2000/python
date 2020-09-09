def delete(a,b):
    try:
        res = int(a)/int(b)
        return print(res)
    except ValueError:
        return print("Введите число")
    except ZeroDivisionError:
        return print("На 0 делить нельзя")


a = input("Введите первое число для деления: ")
b = input("Введите второе число для деления: ")
delete(a, b)
