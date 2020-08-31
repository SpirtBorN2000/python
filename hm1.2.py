timesec = int(input("Введите время в секундах: "))
timehour = int(timesec / 3600)
timemin = int((timesec - timehour * 3600) / 60)
timesecnew = int(timesec - timehour * 3600 - timemin * 60)
timesecnew = int(timesecnew)
print("%02d:%02d:%02d" % (timehour, timemin, timesecnew))

