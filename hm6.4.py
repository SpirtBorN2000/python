class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        print(f"Новая машина {self.name} в цвете {self.color} является полицейской") if is_police == True else print(
            f"Новая машина {self.name} в цвете {self.color}")

    def car_go(self):
        return f"Машина {self.name} поехала!"

    def car_stop(self):
        return f"Машина {self.name} остановилась!"

    def car_turn(self, direction):
        return f" Машина повернула налево" if direction == 0 else f"Машина повернула направо"

    def show_speed(self):
        return self.speed


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            return f"Автомобиль {self.name} превысил допустимую скорость! Ваша скорость {self.speed}"
        else:
            return f"Ваша скорость {self.speed} км/ч"


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            return f"Автомобиль {self.name} превысил допустимую скорость! Ваша скорость {self.speed}"
        else:
            return f"Ваша скорость {self.speed} км/ч"


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


car1 = WorkCar(41, "blue", "lada")
print(car1.show_speed())
print(car1.car_go())
print(car1.car_stop())
print(car1.car_turn(0))
car2 = PoliceCar(60, "Grey", "Bobik")
print(car2.show_speed())
print(car2.car_go())
print(car2.car_stop())
print(car2.car_turn(0))
