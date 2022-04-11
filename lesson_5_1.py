
def odd_to_n(set_num):
    for i in range(1, set_num + 1, 2):
        yield i


odd_to_5 = odd_to_n(5)
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))
print(next(odd_to_5))

odd_to_10 = odd_to_n(10)
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
print(next(odd_to_10))
