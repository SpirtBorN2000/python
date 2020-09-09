def int_sum():
    sum_res = 0
    i = True
    while i == True:
        numberstr = input("Введите числа или Q для выхода: ").split()
        res = 0
        for el in range(len(numberstr)):
            if numberstr[el] == "q" or numberstr[el] == "Q":
                i = False
                break
            else:
                res = res + int(numberstr[el])
        sum_res = sum_res + res
        print(f"Текущая сумма {sum_res}")
    print(f"Финальная сумма {sum_res}")


int_sum()
