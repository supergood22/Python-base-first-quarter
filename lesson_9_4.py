# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.При значении скорости
# свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} go')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self):
        print(f'{self.name} turned')

    def show_speed(self):
        print(f'speed of {self.name} is {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'speed of {self.name} is {self.speed}')
        else:
            print(f'speed of {self.name} is {self.speed}, speed out limit')

    def is_pol(self):
        print(f'is {self.name} polis car? {self.is_police}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def is_pol(self):
        print(f'is {self.name} polis car? {self.is_police}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed < 60:
            print(f'speed of {self.name} is {self.speed}')
        else:
            print(f'speed of {self.name} is {self.speed}, speed out limit')

    def is_pol(self):
        print(f'is {self.name} polis car? {self.is_police}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def is_pol(self):
        print(f'is {self.name} polis car? {self.is_police}')


lada = TownCar(70, 'green', 'Lada', False)
lada.go()
lada.show_speed()
lada.stop()
lada.is_pol()

police = PoliceCar(70, 'white', 'Полиция', True)
police.go()
police.show_speed()
police.stop()
police.is_pol()
