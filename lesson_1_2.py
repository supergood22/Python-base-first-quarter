# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
#

arr = []
for i in range(1, 1000, 2):
    i_3 = i ** 3
    arr.append(i_3)
print(arr)

sum_end = 0
for i in arr:
    c = 0
    t = 1
    n = 1
    k = i
    m = 0
    sum = 0
    while t > 0:
        t = i // 10 ** n
        n += 1
    c = n - 1
    #    print(c, end=', ')

    for j in range(1, c + 1):
        m = k % 10
#        print(m, end='>')
        k = (k - m) / 10
        sum += m
#    print(sum, end=', ')
    if sum % 7 == 0:
        sum_end += i
#print()
print(sum_end)

sum_end_17 = 0
for i in arr:
    c = 0
    t = 1
    n = 1
    k = i + 17
    m = 0
    sum = 0
    while t > 0:
        t = k // 10 ** n
        n += 1
    c = n - 1
    #    print(c, end=', ')

    for j in range(1, c + 1):
        m = k % 10
#        print(m, end='>')
        k = (k - m) / 10
        sum += m
#    print(sum, end=', ')
    if sum % 7 == 0:
        sum_end_17 += (i + 17)
#print()
print(sum_end_17)