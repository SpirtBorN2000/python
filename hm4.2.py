from random import randrange
my_list0 = [1,1,1,1,1,1,1,1,1]
my_list1 = [randrange(0,300) for el in my_list0]
my_list2 = [el for n, el in enumerate(my_list1) if my_list1[n-1] < my_list1[n]]
print(my_list1)
print(my_list2)



