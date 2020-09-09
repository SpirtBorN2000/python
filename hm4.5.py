from functools import reduce
def proizv(a,b):
    return a*b


my_list0 = [el for el in range(99,1001) if el % 2 == 0]
print(f"Произведение данного списка: {reduce(proizv,my_list0)}")