# 1. Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах:
# до минуты: <s> сек; до часа: <m> мин <s> сек; до суток: <h> час <m> мин <s> сек; .
# * в остальных случаях: <d> дн <h> час <m> мин <s> сек

print('Введите количество секунд')

duration = int(input())
seconds = 0
minutes = 0
hours = 0
days = 0
# seconds
if duration // 60 == 0:
    seconds = duration
    print(str(seconds) + ' сек')
# minutes
elif duration // (60 * 60) == 0:
    minutes = duration // 60
    seconds = duration % 60
    print(str(minutes) + ' мин ' + str(seconds) + ' сек')
# hours
elif duration // (60 * 60 * 24) == 0:
    hours = duration // (60 * 60)
    minutes = (duration % (60 * 60)) // 60
    seconds = duration % 60
    print(str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')
# days
elif duration // (60 * 60 * 24) > 0:
    days = duration // (60 * 60 * 24)
    hours = (duration % (60 * 60 * 24)) // (60 * 60)
    minutes = (duration % (60 * 60)) // 60
    seconds = duration % 60
    print(str(days) + ' дн ' + str(hours) + ' час ' + str(minutes) + ' мин ' + str(seconds) + ' сек')
