# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту
# ситуацию и не завершиться с ошибкой.


class Zero_exception(Exception):
    def __init__(self, num):
        self.num = num

inp_data_A = int(input('Введите число А: '))
inp_data_B = int(input('Введите число B: '))

try:
  if inp_data_B == 0:
    raise Zero_exception("Невозможно деление на ноль!")
  else:
    res = inp_data_A / inp_data_B
except Zero_exception as err:
  print(err)
else:
  print(f'Результат: {res}')

