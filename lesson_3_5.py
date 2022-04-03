# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice

def get_jokes(count, flag):
    """Use flag 'True' to be repited or 'False' not to be repited """
    s = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if flag == True:
        for i in range(count):
            s.append(f'{choice(nouns)} {choice(adverbs)} {choice(adjectives)}')

        print(s)
    else:
        if count > 5:
            count = 5
        for _ in range(count):
            _nouns = choice(nouns)
            _adverbs = choice(adverbs)
            _adjectives = choice(adjectives)
            nouns.remove(_nouns)
            adverbs.remove(_adverbs)
            adjectives.remove(_adjectives)
            s.append(f'{_nouns} {_adverbs} {_adjectives}')

        print(s)
        # print(nouns)
        # print(adverbs)
        # print(adjectives)
get_jokes(6, False)

print(help(get_jokes))
