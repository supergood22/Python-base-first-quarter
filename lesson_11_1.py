# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Data:
    DAY = [i for i in range(1, 32)]
    MONTH = [i for i in range(1, 13)]
    YEAR = [i for i in range(2000, 2023)]

    def __init__(self, data):
        self.data = data

    @classmethod
    def data_num(cls, data):
        day = int(data[:2])
        month = int(data[3:5])
        year = int(data[6:])
        print(f'день: {day}')
        print(f'месяц: {month}')
        print(f'год: {year}')

    @staticmethod
    def true_data(day_t, month_t, year_t):
        if day_t not in Data.DAY:
            print('день указан не верно')
        elif month_t not in Data.MONTH:
            print('месяц указан не верно')
        elif year_t not in Data.YEAR:
            print('год указан не верно')
        else:
            print('данные указаны верно')


Data.data_num('10-05-2022')
Data.true_data(10, 5, 2022)
Data.true_data(10, 13, 2022)
