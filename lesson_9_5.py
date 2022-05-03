# 5. Реализовать класс Stationery(канцелярская принадлежность):
# ● определить в нём атрибут title(название) и метод draw(отрисовка).Метод
# выводит сообщение «Запуск отрисовки»;
# ● создать три дочерних класса Pen(ручка), Pencil(карандаш), Handle(маркер);
# ● в каждом классе реализовать переопределение метода draw.Для каждого класса
# метод должен выводить уникальное сообщение;
# ● создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.


class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f'Отрисовка #1 начата. Инструмент - {self.title}.')

class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        print(f'Отрисовка #2 начата. Инструмент - {self.title}.')

class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)


    def draw(self):
        print(f'Отрисовка #3 начата. Инструмент - {self.title}.')

b = Stationery('ничего')
b.draw()

a = Pen('ручка')
a.draw()

c = Pencil('каранадаш')
c.draw()

d = Handle('маркер')
d.draw()
