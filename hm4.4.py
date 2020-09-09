my_list0 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list1 = [el for n, el in enumerate(my_list0) if my_list0.count(el) == 1]
print(my_list1)