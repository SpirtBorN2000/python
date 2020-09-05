def data(name, surname, bdyear, city, email, phonen):
    return print(
        f"Имя {name} Фамилия {surname} Город {city} Год рождения {bdyear} Email {email} Номер телефона {phonen}")


data(name=input("Введите имя "), surname=input("Введите фамилию "), bdyear=input("Введите год рождения "),
     city=input("Введите город проживания "), email=input("Введите email "), phonen=input("Введите номер телефона "))
