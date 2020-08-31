my_list = []
print(my_list)
numberofelements = int(input("Введите колличество элементов списка: "))
i = 0
n = 0
while i < numberofelements:
    i += 1
    my_list.extend(input("Введите значение элемента списка: "))
for el in range(int(len(my_list)/2)):
    my_list[n], my_list[n + 1] = my_list[n + 1], my_list[n]
    n += 2
print(my_list)
