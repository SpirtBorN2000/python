class Worker:
    def __init__(self, name, surname, position, price, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"price": price, "bonus": bonus}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_full_price(self):
        return f"{sum(self._income.values())}"


m1 = Position("Igor", "Troitskiy", "Manager", 20000, 5000)
print(m1.get_full_name())
print(m1.get_full_price())
print(m1.name, m1.position, m1._income.get("price"))
print(m1._income.values())
