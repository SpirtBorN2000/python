class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f"Запуск отрисовки {self.title}"


class Pen(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title} с Pen"


class Pencil(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title} с Pencil"


class Handle(Stationery):
    def draw(self):
        return f"Запуск отрисовки {self.title} с Handle"


first = Stationery("Yoyo")
second = Pen("Yoyo")
third = Pencil("Yoyo")
fourth = Handle("Yoyo")
print(first.draw())
print(second.draw())
print(third.draw())
print(fourth.draw())
