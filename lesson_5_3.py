# 3. Есть два списка:
#
# Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ...
# Количество генерируемых кортежей не должно быть больше длины списка tutors.
# Если в списке klasses меньше элементов, чем в списке tutors,
# необходимо вывести последние кортежи в виде: (<tutor>, None), например:
# ('Станислав', None)
# Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
# Подумать, в каких ситуациях генератор даст эффект.


tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Петр', 'Сергей']
klasses = ['9А', '7В', '9Б']


def students_gen(key, value):
    delta = len(key) - len(value)
    for j in range(delta):
        klasses.append('None')
    for i in range(len(tutors)):
        student = (key[i], value[i])
        yield student

stud = students_gen(tutors, klasses)
print(next(stud))
print(next(stud))
print(next(stud))
print(next(stud))
print(next(stud))
print(next(stud))
